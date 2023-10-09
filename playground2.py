import heapq

MAX_P = 2000
n, m, p = 0, 0, 0
pid = [0] * (MAX_P + 1)  # 각 토끼의 id 기록
pw = [0] * (MAX_P + 1)  # 각 토끼의 이동거리 기록
jump_cnt = [0] * (MAX_P + 1)  # 각 토끼의 점프횟수 기록
result = [0] * (MAX_P + 1)  # 각 토끼의 점수 기록
point = [(0, 0) * (MAX_P + 1)]  # 각 토끼의 현재 위치(좌표) 기록
id_to_idx = {}  # 각 토끼의 pid를 인덱스 번호로 변환
is_runned = [0] * (MAX_P + 1)  # 각 토끼가 달렸는지 여부 기록
total_sum = 0


class Rabbit:
    def __init__(self, x, y, j, pid):
        self.x = x  # 행
        self.y = y  # 열
        self.j = j  # 점프횟수
        self.pid = pid  # 토끼 고유번호

    def __lt__(self, other):
        if self.j != other.j:
            return self.j < other.j
        if self.x + self.y != other.x + other.y:
            return self.x + self.y < other.x + other.y
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.pid < other.pid


def compare(a, b):
    if a.x + a.y != b.x + b.y:
        return a.x + a.y < b.x + b.y
    if a.x != b.x:
        return a.x < b.x
    if a.y != b.y:
        return a.y < b.y
    return a.pid < b.pid


def init(inp):
    global n, m, p

    n, m, p, *rabbits = inp
    for i in range(1, p+1):
        pid[i] = rabbits[i*2-2]
        pw[i] = rabbits[i*2-1]

        id_to_idx[pid[i]] = i
        point[i] = (1, 1)


def get_up_rabbit(cur_rabbit, dis):
    up_rabbit = cur_rabbit
    dis %= 2 * (n-1)

    if dis >= up_rabbit.x - 1:
        dis -= (up_rabbit.x - 1)
        up_rabbit.x = 1
    else:
        up_rabbit.x -= dis
        dis = 0

    if dis >= n - up_rabbit.x:
        dis -= (n - up_rabbit.x)
        up_rabbit.x = n
    else:
        up_rabbit.x += dis
        dis = 0

    up_rabbit.x -= dis

    return up_rabbit


def get_down_rabbit(cur_rabbit, dis):
    down_rabbit = cur_rabbit
    dis %= 2 * (n-1)

    if dis >= n - down_rabbit.x:
        dis -= (n - down_rabbit.x)
        down_rabbit.x = n
    else:
        down_rabbit.x += dis
        dis = 0

    if dis >= down_rabbit.x - 1:  # 상단경계를 넘어가면
        dis -= down_rabbit.x - 1
        down_rabbit.x = 1
    else:
        down_rabbit.x -= dis
        dis = 0

    down_rabbit.x += dis

    return down_rabbit


def get_left_rabbit(cur_rabbit, dis):
    left_rabbit = cur_rabbit
    dis %= 2 * (m-1)

    if dis >= left_rabbit.y - 1:  # 왼쪽경계를 넘어가면
        dis -= left_rabbit.y - 1
        left_rabbit.y = 1
    else:
        left_rabbit.y -= dis
        dis = 0

    if dis >= m - left_rabbit.y:  # 오른쪽경계를 넘어가면
        dis -= m - left_rabbit.y
        left_rabbit.y = m
    else:
        left_rabbit.y += dis
        dis = 0

    left_rabbit.y -= dis

    return left_rabbit


def get_right_rabbit(cur_rabbit, dis):
    right_rabbit = cur_rabbit
    dis %= 2 * (m-1)

    if dis >= m - right_rabbit.y:  # 오른쪽경계를 넘어가면
        dis -= m - right_rabbit.y
        right_rabbit.y = m
    else:
        right_rabbit.y += dis
        dis = 0

    if dis >= right_rabbit.y - 1:  # 왼쪽경계를 넘어가면
        dis -= right_rabbit.y - 1
        right_rabbit.y = 1
    else:
        right_rabbit.y -= dis
        dis = 0

    right_rabbit.y += dis

    return right_rabbit


def copy_rabbit(rabbit):
    return Rabbit(rabbit.x, rabbit.y, rabbit.j, rabbit.pid)


def start_round(inp):
    global total_sum

    k, bonus = inp
    rabbit_pq = []

    for i in range(1, p+1):
        is_runned[i] = False

    for i in range(1, p+1):
        x, y = point[i]
        new_rabbit = Rabbit(x, y, jump_cnt[i], pid[i])
        heapq.heappush(rabbit_pq, new_rabbit)

    for _ in range(k):
        cur_rabbit = heapq.heappop(rabbit_pq)

        dis = pw[id_to_idx[cur_rabbit.pid]]
        nex_rabbit = copy_rabbit(cur_rabbit)
        nex_rabbit.x = 0
        nex_rabbit.y = 0

        up_rabbit = get_up_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, up_rabbit):
            nex_rabbit = up_rabbit

        down_rabbit = get_down_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, down_rabbit):
            nex_rabbit = down_rabbit

        left_rabbit = get_left_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, left_rabbit):
            nex_rabbit = left_rabbit

        right_rabbit = get_right_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, right_rabbit):
            nex_rabbit = right_rabbit

        nex_rabbit.j += 1
        heapq.heappush(rabbit_pq, nex_rabbit)

        nex_idx = id_to_idx[nex_rabbit.pid]
        point[nex_idx] = (nex_rabbit.x, nex_rabbit.y)
        jump_cnt[nex_idx] += 1

        is_runned[nex_idx] = True

        result[nex_idx] -= (nex_rabbit.x + nex_rabbit.y)
        total_sum += (nex_rabbit.x + nex_rabbit.y)

    bonus_rabbit = Rabbit(0, 0, 0, 0)
    while rabbit_pq:
        cur_rabbit = heapq.heappop(rabbit_pq)

        if not is_runned[id_to_idx[cur_rabbit.pid]]:
            continue

        if compare(bonus_rabbit, cur_rabbit):
            bonus_rabbit = cur_rabbit

    result[id_to_idx[bonus_rabbit.pid]] += bonus


def power_up(inp):
    pid, t = inp
    idx = id_to_idx[pid]

    pw[idx] *= t


def print_result():
    ans = 0
    for i in range(1, p + 1):
        ans = max(ans, result[i] + total_sum)

    print(ans)


q = int(input())
for _ in range(q):
    query, *inp = list(map(int, input().split()))

    if query == 100:
        init(inp)
    if query == 200:
        start_round(inp)
    if query == 300:
        power_up(inp)
    if query == 400:
        print_result()
