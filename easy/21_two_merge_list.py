from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_mas = []
        while True:
            if list1 == None and list2 == None:
                break
            elif list1 == None:
                val = list2.val
                list2 = list2.next
            elif list2 == None:
                val = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                val = list2.val
                list2 = list2.next
            else:
                val = list1.val
                list1 = list1.next
            result_mas.append(val)
        if result_mas == []:
            return ListNode(val='')
        else:
            last_index = len(result_mas) - 1
            result_list = ListNode(val=result_mas[last_index])
            for i in range(len(result_mas)-2, -1, -1):
                result_list = ListNode(val=result_mas[i], next=result_list)
            return result_list
