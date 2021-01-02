class Node(object):
    def __init__(self, val='0', next=None):
        self.val = val
        self.next = next
    
        
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    result = ""
    pr = []
    
    for i in range(numRows):
        pr.append(Node())

    header = pr.copy()
    # If given AttributeError: 'list' object has no attribute 'copy'
    # header = list(pr)
    
    for i in range(len(s)):
        index = next_index(i, numRows)
        pr[index].next = Node(s[i])
        pr[index] = pr[index].next
    
    for p in header:
        while p.next is not None:
            p = p.next
            result += p.val
    
    return result
        
def next_index(i, numRows):
    if numRows == 1:
        return 0
    step = numRows - 1
    remain = i % step
    if (i // step) % 2 == 0:
        return remain
    else:
        return - (remain + 1)
