class Node:
    def __init__(self, data):
        self._data = data
        self._nextval = None
    
    def data(self, d=None):
        if d: self._data = d
        return self._data
    
    def nextval(self, n=None):
        if n: self._nextval = n
        return self._nextval
        

class HeadNode:
    def __init__(self) -> None:
        self._headval = None

    def headval(self, h=None):
        if h: 
            self._headval = h
        return self._headval

    def traverseLinkedlist(self):
        printval = self.headval()
        while printval is not None:
            print(printval.data())
            printval = printval.nextval()

def main():
    l = HeadNode()
    e1 = Node('Facebook')
    e2 = Node('Twitter')
    e3 = Node('LinkedIn')
    e1.nextval(e2)
    e2.nextval(e3)
    l.headval(e1)
    l.traverseLinkedlist()

if __name__ == '__main__':
    main()
