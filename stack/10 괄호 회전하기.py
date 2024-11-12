s="}]()[{"
a=[]
#a.append(s)
b=len(s)
stack=[]
count1=0
count2=0
count3=0

for i in range(b):
    stack.append(s[i])

for i in range(b):
    stack.append(s[i])
    stack.pop(0)
    print(stack)
    print("-----------------------------")
    if stack[i]=='(':
        for j in range(1,b):
            if stack[j]==')':
                count1+=1
            else: count1=0

    elif stack[i]=='{':
        for j in range(1,b):
            if stack[j]=='}':
                count2+=1
            else: count2=0

    elif stack[i]=='[':
        for j in range(1,b):
            if stack[j]==']':
                count3+=1
            else: count3=0
    else:
        continue




print(count1+count2+count3)