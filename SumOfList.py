n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

answer = 0
for i in range(n):
    answer += lst[i]

print(answer)   
