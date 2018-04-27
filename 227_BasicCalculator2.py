class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        key 1: use stack,
         case '+': simply add the number to the stack
         case '-': simply add the negative number to the stack
         case '*': pop the last one, then multiply it by the number and add to the stack
         case '/': pop the last one, then devide it by the number and add to the stack
        key 2: if space, simply skip. if digit, find the 'complete number' 
        """
        # corner case
        if len(s) == 0:
            return 0

        # repeat till the end
        num = 0
        stack = []
        sign_prev = '+'
        for i in range(len(s)):
            # 1. if space, skip
#            if s[i].isspace() is True:
#                continue

            # 2. if digit, add the num
            if s[i].isdigit() is True:
                num = 10*num + (ord(s[i]) - ord('0'))

            # 3. if next digit is comfirmed
            if ((s[i].isspace() is False and s[i].isdigit() is False)
                or (i == (len(s)-1))):
            
                # if sign '+'
                if sign_prev == u'+':
                    stack.append(+num)
                    sign_prev = s[i]
                    num = 0

                # 4. if sign '-'
                elif sign_prev == u'-':
                    stack.append(-num)
                    sign_prev = s[i]
                    num = 0

                # 5. if sign '*'
                elif sign_prev == u'*':
                    prev = stack.pop()
                    stack.append(prev*num)
                    sign_prev = s[i]
                    num = 0

                # 6. if sign '/'
                elif sign_prev == u'/':
                    prev = stack.pop()
#                    print('/', prev, num, stack)
                    if prev < 0 and prev%num != 0:
                        stack.append(prev // num +1)
                    else:
                        stack.append(prev // num)                   
                    sign_prev = s[i]
                    num = 0
#                print('debug', i, stack, sign_prev)

        return sum(stack)
