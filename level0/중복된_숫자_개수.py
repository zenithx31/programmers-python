def solution(array, n):
    a = []
    for i in array:
        if i == n:
            a.append(n)
            answer = len(a)
    return answer
