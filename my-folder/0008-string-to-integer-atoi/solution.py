class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        t = ''
        if not s:
            return 0
        
        l1 = [i for i in s]
        l3 = [str(i) for i in range(10)]

        l2 = l3 + ['+','-']

        if l1[0] not in l2:
            return 0
        elif l1[0] in ['+','-'] and (len(l1) == 1 or l1[1] in ['+','-']):
            return 0
        elif l1[0] in ['+','-'] and l1[1] not in l3:
            return 0
        else:
            t = t+l1[0]
        for i in range(1,len(s)):
            if l1[i] not in l3:
                break
            else:
                t += l1[i]
        
        t = int(t)
        if t < (-1*(2**31)):
            return (-1*(2**31))
        elif t > ((2**31)-1):
            return ((2**31)-1)
        else:
            return t



