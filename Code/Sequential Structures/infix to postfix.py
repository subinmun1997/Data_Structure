infix = ['2', '+', '3', '*', '4']
postfix = []
stack = []
operator = ['*', '/', '+', '-']
bracket = ['(', ')']


def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False


def pref(x):
    if x is '*' or x is '/':
        return 1
    elif x is '+' or x is '-':
        return 0


for c in infix:
    if is_number(c):
        postfix.append(c)
    elif c in operator:
        p = pref(c)
        while len(stack) > 0:
            top = stack[-1]
            if pref(top) <= p: # 우선순위가 낮은것이 우선순위가 높은것의 위에 있는 경우
                break
            postfix.append(stack.pop()) # 스택에 우선순위 낮->높 순서로 쌓여있는 경우
        stack.append(c)

    elif c == '(':
        stack.append(c)
    elif c == ')':
        while True:
            x = stack.pop()
            if x == '(':
                break
            postfix.append(x)

while len(stack) > 0:
    postfix.append(stack.pop())

print(postfix)