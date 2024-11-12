board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

def solution(board, moves):
    basket = []  # 바구니 역할을 하는 스택
    count = 0  # 터트려져 사라진 인형 개수를 저장

    # moves를 순회하며 크레인 작동을 시뮬레이션
    for move in moves:
        col = move - 1  # 1부터 시작하므로 인덱스 조정을 위해 -1

        # 해당 열에서 가장 위에 있는 인형 찾기
        for row in range(len(board)):
            if board[row][col] != 0:  # 인형이 있는 경우
                picked = board[row][col]
                board[row][col] = 0  # 인형을 집어올린 후 해당 위치를 빈 칸으로 설정

                # 바구니에 쌓인 인형이 연속하는지 확인
                if basket and basket[-1] == picked:
                    basket.pop()  # 같은 인형이 연속되면 제거
                    count += 2  # 제거된 인형 개수 증가
                else:
                    basket.append(picked)  # 바구니에 인형 추가
                break  # 인형을 집었으면 다음 move로 넘어감

    return count

print(solution(board,moves))