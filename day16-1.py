import random
import math


class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    while True:
        current = current.link
        x, y = current.data[1:]
        print(f'{current.data[0]} 편의점, 거리: {math.sqrt(x**2 + y**2)}')
        if current.link == head:
            break
    print()


def sort_List(conbi):
    global head, current, pre

    node = Node()
    node.data = conbi

    if head == None:
        head = node
        node.link = head
        return

    X, Y = node.data[1:]
    distance = math.sqrt(X ** 2 + Y ** 2)
    hX, hY = head.data[1:]
    hdist = math.sqrt(hX ** 2 + hY ** 2)

    if hdist > distance:  # 헤드 앞에 삽입
        node.link = head
        last = head

        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        cX, cY = current.data[1:]
        cdist = math.sqrt(cX ** 2 + cY ** 2)
        if cdist > distance:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__":

    storearray = []
    storeName = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    for i in range(10):
        store = (storeName[i], random.randint(1, 100), random.randint(1, 100))
        storearray.append(store)

    for store in storearray:
        sort_List(store)

    print_nodes(head)
