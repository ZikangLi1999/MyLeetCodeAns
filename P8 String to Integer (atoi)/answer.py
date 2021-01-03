class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ""
        sign = ''
        for ch in s:
            if ch == ' ':
                if num == "" and sign == '':
                    continue
                else:
                    break
            elif ch in ['+', '-']:
                if num == "":
                    if sign == '':
                        sign = ch
                    else:
                        break
                else:
                    break
            elif ch < '0' or ch > '9':
                break
            else:
                num += ch
        if num == "":
            return 0
        elif sign == '-':
            n = int(num)
            if n > 2 ** 31:
                return -1 * (2 ** 31)
            else:
                return -1 * n
        else:
            n = int(num)
            if n > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return n
