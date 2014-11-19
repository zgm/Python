class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        index = n-2
        while 0<=index and num[index]>=num[index+1]:
            index-=1
        if index<0:
            num.reverse()
        else:
            right = index+1
            while right<=n-2 and num[index]<num[right+1]:
                right+=1
            num[index],num[right] = num[right],num[index]
            for i in range(index+1,(index+1+n-1)/2+1):
                num[i],num[n-1+index+1-i] = num[n+index-i],num[i]
        return num



if __name__ == '__main__':
    zgm = Solution()
    num = [1]
    zgm.nextPermutation(num)
    print num

