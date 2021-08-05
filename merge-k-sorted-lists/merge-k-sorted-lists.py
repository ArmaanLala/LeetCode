import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        heap = []
        
        for li in lists:
            while li:
                heapq.heappush(heap,li.val)
                li = li.next
        print (heap)
        
        ans = head = ListNode(-1)
        
        while(heap):
            ans.next = ListNode(heapq.heappop(heap))
            ans = ans.next
    
        return(head.next)
    