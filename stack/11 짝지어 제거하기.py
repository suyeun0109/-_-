s = "baabaa"
stack = []
l = len(s)

for i in s:
    print(stack)
    if stack and stack[-1]==i:
        print('-----------------')
        print(stack[-1])
        print("----****************----")
        stack.pop()
    else:
         stack.append(i)
# 최종적으로 스택이 비어 있으면 모든 문자가 제거된 것이므로 1을 출력
if not stack:
    print("1")
else:
    print("0")
