
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       node = []
    
       for head in lists:
        while head:
            node.append(head.val)
            head= head.next

       node.sort()

       dummy = ListNode(0)
       cur = dummy

       for value in node:
            cur.next = ListNode(value)
            cur = cur.next
       return dummy.next