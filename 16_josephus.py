
# def josephus_problem(n, k):
#     person = [ i for i in range(1, n+1) ]
#     j_permutation = []
#     j = 0
#     while len(person) != 0:
#         j = (j + k - 1) % len(person)
#         j_permutation.append(str(person.pop(j)))

#     return j_permutation

# n, k = map(int, input().split())
# answer = josephus_problem(n,k)
# print("<%s>" %(", ".join(answer)))


# print("<",", ".join(answer)[:], ">", sep=' ')
# print("<%s>" %(", ".join(answer)))



# Recursion

def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n-1, k) + k - 1) % n + 1

n, k = map(int, input().split())
print(josephus(n, k))

'''
# 동적 계획법의 적용 : 재귀에서 반복으로

def findTheWinner(n, k):
    s = 1
    for n in range(1, n+1):
        s = ((s + k - 1) % n) + 1

    return s

n, k = map(int, input().split())
print(findTheWinner(n, k))
'''