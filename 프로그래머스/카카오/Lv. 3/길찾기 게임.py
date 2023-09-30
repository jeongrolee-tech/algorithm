'''
https://school.programmers.co.kr/learn/courses/30/lessons/42892

- 시간복잡도 = (O(n log n) + O(n^2) + O(n) + O(n) = O(n^2))
    1. **construct_tree 함수**:
        - **`nodes.sort(key=lambda x: (-x[1],x[0]))`**: 이 부분은 노드를 정렬하는데 O(n log n)의 시간복잡도를 가집니다.
        - 이후 for 루프에서 각 노드를 트리에 추가하는데, 최악의 경우 트리가 한쪽으로 치우친 경우 O(n)의 시간이 걸릴 수 있습니다. 따라서, for 루프 전체는 O(n^2)의 시간복잡도를 가질 수 있습니다.
    2. **traverse_preorder 및 traverse_postorder 함수**:
        - 각 함수는 트리의 모든 노드를 한 번씩 방문하므로 O(n)의 시간복잡도를 가집니다.
    3. **solution 함수**:
        - **`nodeinfo`**에 노드 번호를 추가하는 부분은 O(n)의 시간복잡도를 가집니다.
        - **`construct_tree`** 함수 호출은 위에서 언급한대로 최대 O(n^2)의 시간복잡도를 가질 수 있습니다.
        - **`traverse_preorder`** 및 **`traverse_postorder`** 함수 호출은 O(n)의 시간복잡도를 가집니다.
    
    최종적으로, 시간복잡도는 O(n^2)이 됩니다.
    
- 공간복잡도 = O(n)
    - **`nodeinfo`** 배열에 노드 번호를 추가하는 부분은 O(n)의 공간복잡도를 가집니다.
    - 트리를 구성하는 부분은 O(n)의 공간복잡도를 가집니다.
    - **`preorder_result`** 및 **`postorder_result`** 배열은 O(n)의 공간복잡도를 가집니다.
    
    따라서, 공간복잡도는 O(n)입니다.
'''

import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def add_node(parent_node, child_value):
    if child_value[0] < parent_node.value[0]:  # x 좌표가 작으면 왼쪽 서브트리로
        if parent_node.left is None:
            parent_node.left = Node(child_value)
        else:
            add_node(parent_node.left, child_value)
    else:  # x 좌표가 크면 오른쪽 서브트리로
        if parent_node.right is None:
            parent_node.right = Node(child_value)
        else:
            add_node(parent_node.right, child_value)


def construct_tree(nodes):
    if not nodes:
        return None

    # y 좌표가 높은 순서대로(내림차순), y 좌표가 같다면 x 좌표가 작은 순서대로 정렬(오름차순)
    nodes.sort(key=lambda x: (-x[1], x[0]))
    root = Node(nodes[0])

    for node in nodes[1:]:
        add_node(root, node)

    return root


def traverse_preorder(node, visit_list):
    if node is None:
        return
    visit_list.append(node.value[2])  # 노드 방문
    traverse_preorder(node.left, visit_list)  # 왼쪽 서브트리 방문
    traverse_preorder(node.right, visit_list)  # 오른쪽 서브트리 방문


def traverse_postorder(node, visit_list):
    if node is None:
        return
    traverse_postorder(node.left, visit_list)  # 왼쪽 서브트리 방문
    traverse_postorder(node.right, visit_list)  # 오른쪽 서브트리 방문
    visit_list.append(node.value[2])  # 노드 방문


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)  # [x좌표, y좌표, 노드번호]

    root_node = construct_tree(nodeinfo)  # 이진트리 구성

    preorder_result, postorder_result = [], []  # 전위 순회, 후위 순회 결과를 담을 배열 초기화

    traverse_preorder(root_node, preorder_result)
    traverse_postorder(root_node, postorder_result)

    return [preorder_result, postorder_result]
