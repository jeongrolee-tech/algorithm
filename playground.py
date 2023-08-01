# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 두 변수는 하나의 ListNode 객체를 공유
        start_node_of_merged_list = ListNode(-1)
        last_node_of_merged_list = start_node_of_merged_list

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
        #
        last_node_of_merged_list.next = list1 if list1 is not None else list2

        return start_node_of_merged_list.next

