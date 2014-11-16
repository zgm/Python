class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0:
            return len(s)==0
        if len(p)==1 or (len(p)>1 and p[1]!='*'):
            return len(s)>0 and (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:],p[1:])
        if self.isMatch(s,p[2:]):
            return True
        while( len(s)>0 and (p[0]=='.' or p[0]==s[0]) ):
            if self.isMatch(s[1:],p[2:]):
                return True
            s = s[1:]
        return False

    def isMatch2(self, s, p):
        pre, ss = [], []
        while len(s)>0:
            if len(p)>0 and (p[0]=='?' or s[0]==p[0]):
                s = s[1:]
                p = p[1:]
                continue
            if len(p)>0 and p[0]=='*':
                pre = p
                p = p[1:]
                ss = s
                continue
            if len(pre)>0:
                p = pre
                s = ss[1:]
                continue
            return False
        while len(p)>0 and p[0]=='*':
            p = p[1:]
        return len(p)==0



if __name__ == '__main__':
    zgm = Solution()
    print zgm.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")

