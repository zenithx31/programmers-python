def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        answer = (a * a) + (b * b)
    elif a % 2 == 0 and b % 2 == 0:
        answer = abs(a - b)
    else:
        answer = 2 * (a + b)
    return answer
