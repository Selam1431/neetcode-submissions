# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for lys in lists:
            while lys:
                nodes.append(lys.val)
                lys = lys.next

        nodes.sort()

        res = ListNode(0)
        cur = res

        for  node in nodes:
            cur.next = ListNode(node)
            cur = cur.next

        return res.next




        