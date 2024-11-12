
def solution():
    numbers = list(map(int,input().split()))
    a =[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            a.append(numbers[i]+numbers[j])
    a.sort()
    a=set(a)
    print(a)

solution()