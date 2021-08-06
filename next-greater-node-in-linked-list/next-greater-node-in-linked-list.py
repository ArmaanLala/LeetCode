# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        # Variables
        answer = []
        stack = []
        currentIndex = 0
        
        # O(N)
        while (head):
            
            while stack and stack[-1][1] < head.val:
                #This sets the values for any smaller values to the right
                answer[stack.pop()[0]] = head.val
                
            # Add our current value to the stack
            stack.append((currentIndex,head.val))
            # Increment Index
            currentIndex += 1
            # Give a temporary value that will be replaced when a larger value is found
            answer.append(0)
            # Move to next value in list
            head = head.next
            
        return answer
            