# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 두 변수는 하나의 ListNode 객체를 공유
        dummy_node_of_merged_list = ListNode(-1)
        last_node_of_merged_list = dummy_node_of_merged_list

        # 이 ListNode 객체의 next 속성을 업데이트하는 것이 결국은 두 리스트를 병합하는 결과를 만들어내는 것
        while list1 and list2:
            # 오름차순으로 병합
            if list1.val <= list2.val:
                last_node_of_merged_list.next = list1
                list1 = list1.next
            else:
                last_node_of_merged_list.next = list2
                list2 = list2.next
            # mergedList의 head 갱신
            last_node_of_merged_list = last_node_of_merged_list.next
        # 마지막 남은 노드 병합
        last_node_of_merged_list.next = list1 if list1 is not None else list2

        return dummy_node_of_merged_list.next


'''
### 시간복잡도와 공간복잡도

- 시간 복잡도: O(n), 여기서 n은 두 리스트의 총 길이입니다. 병합 과정에서 각 노드를 한 번씩 확인하기 때문입니다.
- 공간 복잡도: O(1), 임의의 더미 노드를 사용하므로 공간 복잡도는 O(1)입니다.
### 한줄평

"Merge Two Sorted Lists" 문제는 두 개의 정렬된 연결 리스트를 병합하여 하나의 정렬된 리스트를 만드는 것입니다.

### 키워드

- 연결 리스트
- 병합
- 재귀
- 반복문
- 더미 노드

이 문제는 연결 리스트에 대한 기본적인 이해와 그 조작법을 잘 알고 있는지를 묻는 문제입니다. 또한, 반복문과 재귀에 대한 이해도 묻고 있습니다.

### 문제 설명

이 문제는 두 개의 정렬된 연결 리스트 `l1`과 `l2`가 주어졌을 때, 이 두 리스트를 병합하여 새로운 정렬된 리스트를 반환하는 것입니다. 새 리스트는 `l1`과 `l2`의 노드만 사용해야하며, 원래의 리스트의 순서는 유지되어야 합니다.

### 접근 방법

1. **재귀적인 방법**을 사용하여 두 리스트의 머리(head)를 비교하고 더 작은 값을 가진 노드를 새로운 리스트의 노드로 선택하는 방법이 있습니다. 그리고 선택한 노드의 다음 노드는 나머지 노드들 중에서 다시 가장 작은 값을 가진 노드가 되도록 재귀적으로 함수를 호출합니다.
2. *반복문(Iteration)**을 사용하는 방법도 있습니다. 더미 노드(dummy node)를 만들고, 두 리스트의 노드를 순서대로 비교하면서 더 작은 값을 가진 노드를 더미 노드의 다음 노드로 만드는 과정을 반복합니다.
'''
