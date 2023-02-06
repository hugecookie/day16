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


SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1
data = ["빨강", "파랑", "초록", "노랑", "보라", "주황"]


if __name__ == "__main__":
    random.shuffle(data)

    for i in data:
        push(i)
        print(f'{i}-->', end='')
    print('과자집')
    while True:
        back = pop()
        print(f'{back}-->', end='')
        if is_stack_empty():
            break
    print('우리집')
