from itertools import count

N=5
stages=[2,1,2,6,2,4,3,3]
challenger=len(stages)
#result=[3,4,2,1,5]
fails = [0]*(N+1)

def solution(N, stages):
    total = len(stages)
    result=[]
    for i in range(1,N+1):
        if stages[i]==0:
            fails[i]=0
        else:
            fails[i]=stages[i]/total
            total-=stages.count(i)
            result.append(fails[i])


    print(sorted(result,key=lambda x:fails[x] ,reverse=True))

    print(result)

solution(N,stages)


