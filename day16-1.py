import random

def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    return False


def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is EMPTY~")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp


SIZE = 300
stack = [None for _ in range(SIZE)]
top = -1
song = """ 약이라도 타놓은 걸까
Yeah (I said it's true)
평범한 네 목소리에
(I said it's true)
냉수를 들이켜도
쓴 커피를 마셔봐도
너무 달아, 이거 왜이래
(I said it's) killin' me softly
"""

if __name__ == "__main__":

    for i in song:
        push(i)
    print(song)

    while True:
        word = pop()
        print(word, end='')
        if is_stack_empty():
            break
