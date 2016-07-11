
def _downheap(buff, n):
    size = len(buff)
    while True:
        c = 2 * n + 1
        if c >= size: break
        if c + 1 < size:
            if buff[c] > buff[c + 1]: c += 1
        if buff[n] < buff[c] or buff[n] == buff[c] : break
        temp = buff[n]
        buff[n] = buff[c]
        buff[c] = temp
        n = c

def _upheap(buff, n):
    while True:
        p = (n - 1) // 2
        if p < 0 or buff[p] < buff[n] or buff[p] == buff[n]: break
        temp = buff[n]
        buff[n] = buff[p]
        buff[p] = temp
        n = p

class PQueue(object):
    def __init__(self, buff=[]):
        self.buff = buff[:]
        for n in range(len(self.buff) // 2 - 1, -1, -1):
            _downheap(self.buff, n)

    def push(self, data):
        self.buff.append(data)
        _upheap(self.buff, len(self.buff) - 1)

    def pop(self):
        if len(self.buff) == 0 : raise IndexError
        value = self.buff[0]
        last = self.buff.pop()
        if len(self.buff) > 0:
            self.buff[0] = last
            _downheap(self.buff, 0)
        return value

    def peek(self):
        if len(self.buff) == 0 : raise IndexError
        return self.buff[0]

    def isEmpty(self): return len(self.buff) == 0