def solution(s1, s2):
    a = []
    s1 = list(s1)
    s2 = list(s2)
    for i in s1:
        for j in s2:
            if i == j:
                a.append(i)
    return len(a)
