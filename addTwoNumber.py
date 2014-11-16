class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        sum, root = None, None
        add = 0
        while( l1!=None or l2!=None or add!=0 ):
            if l1!=None:
                add += l1.val
                l1 = l1.next
            if l2!=None:
                add += l2.val
                l2 = l2.next
            if sum==None:
                sum = ListNode(add%10)
                root = sum
            else:
                sum.next = ListNode(add%10)
                sum = sum.next
            add/=10
        return root
        return len(p)==0



if __name__ == '__main__':
    zgm = Solution()
    print zgm.addTwoNumbers(None,None)

