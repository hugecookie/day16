
class two_ways_node:
    def __init__(self):
        self.plink = None
        self.data = None
        self.nlink = None


def printNodes(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 --> ", end=' ')
    print(current.data, end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()
    print("역방향 --> ", end=' ')
    print(current.data, end=' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["꼬부기", "피카츄", "라이츄", "거북왕", "어니부기"]

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = two_ways_node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node
        node = two_ways_node()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    printNodes(head)
