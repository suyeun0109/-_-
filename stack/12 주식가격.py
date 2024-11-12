def solution(prices):
    n=len(prices)
    answer=[0]*n

    stack=[0]
    for i in range(1,n):
        while stack and prices[i]<prices[-1]:
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)

    while stack:
        j=stack.pop()
        answer[j]=n-1-j
    return answer

prices=[1,2,3,2,3]
print(solution(prices))