'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        newn = Node(x)

        temp = head
        if(head is None):
            return newn
        while(temp.next is not None):
            temp = temp.next
        temp.next = newn
        return head