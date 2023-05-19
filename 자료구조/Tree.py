'''
- 루트 노드(Root): 트리의 시작 점 입니다.
- 정점 (Vertex): A,B,C와 같은 값을 갖고 나타내며, 노드로 표현됩니다.
- 간선 (Edge): 정점 간에 연결된 선입니다.

- 조상 (ancestor) 위쪽으로 간선을 따라가면 만나는 노드들 말합니다.
- 부모 노드 (Parent)
- 자식 노드 (Child)
- 자손 (descendant): 아래쪽으로 간선을 따라가면 만나는 노드들을 말합니다.

- 형제 노드(sibling): 같은 부모를 가진 노드를 말합니다.
- 리프 노드 (Leef): 더 이상 뻗어나갈 수 없는 마지막 노드를 일컫습니다.

- 차수 (degree): 각 노드가 갖는 자식의 수. 모든 노드의 차수가 n개 이하인 트리를 n진 트리라고 합니다.
- 높이 (height): 루트 노드에서 가장 멀리 있는 리프 노드 까지의 거리입니다.
- 레벨 (level): 루트 노드에서 떨어진 거리입니다.
'''

# 선형 자료구조인 배열과 리스트의 경우, 순회하는 법이 인덱스 0,1,2부터 n-1까지로 방법이 하나로 정해져 있기 때문에,
# 순회하는 방법을 따로 배우지 않았습니다. for문을 이용해서 쉽게 순회할 수 있기 때문이죠.
# * 하지만 트리는 비선형 자료구조이기에 순회하는 방법이 여러가지 존재합니다.


# * Level-order traversal (너비우선탐색)
# queue를 popleft하고 append함으로써 각 노드들을 방문하는 과정과 queue가 비워지면, 완전 탐색이 끝난다는 것이 핵심입니다.
# levelOrder의 시간복잡도는 어려울게 없습니다. 모든 정점의 개수가 n에 대해, popleft하고 append하는 과정이 n번 일어남으로 O(n)의 시간복잡도를 가집니다.
from collections import deque


def levelOrder(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    q.append(root)  # queue에 루트인 A 노드가 들어갑니다. 그 후, while문을 통해 모든 노드를 탐색할 것입니다.
    while q:
        cur_node = q.popleft()  # queue에 있는 A노드가 popleft되면, A 노드를 방문했다고 판단합니다.
        visited.append(cur_node.value)

        if cur_node.left:
            # A 노드의 자식 노드가 존재함으로, queue에 B 노드와 C 노드를 넣어줍니다.
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    # 이제 queue가 비어있으므로, while문을 빠져나온 후 visited를 return함으로써 level order traversal가 완료 됩니다.
    return visited

# * 전위 순회(preorder), 중위 순회(inorder), 후위 순회(postorder)
# 방문하다(visit) - 노드의 값을 접근하는 것(출력, 저장 등의 행위)
# 노드의 "방문 방식"에 따라 전위순회, 중위순회, 후위순회로 나누어 집니다.
# 순회하다(traversal) - 트리를 돌아 다니는 것


def traversal(root):
    if root is None:
        return
    traversal(root.left)
    traversal(root.right)

# * 전위 순회: A를 가장 "처음" 방문 하는 것
# 나를 먼저 방문하고 자식 노드들을 방문한다.
# 출력 순서: A(root), B(left), C(right)


def preorder(root):
    if root is None:
        return
    print(root)
    preorder(root.left)
    preorder(root.right)

# * 중위 순회: A를 "중간" 방문 하는 것
# 왼쪽 노드를 먼저 방문하고, 나를 방문한 후, 오른쪽 노드를 방문한다.
# 출력 순서: B(left), A(root), C(right)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)
# * 후위 순회: A를 가장 "끝" 방문 하는 것
# 자식노드들을 다 방문한 후, 나를 방문한다.
# 출력 순서: B(left), C(right), A(root)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root)

# 저희는 앞서서 재귀의 시간복잡도를 위와 같이 공부하였습니다. 전위, 중위, 후위 순회의 시간 복잡도도 마찬가지로 구할 수 있습니다.
# 재귀의 시간복잡도 = 재귀 함수 호출 횟수 x 재귀 함수 하나당 시간복잡도
# 전위, 중위, 후위 순회의 시간 복잡도는 O(n)입니다.
