# Cài dặt thư viên vào
import numpy as np
import random
# Kiểm tra trạng thái hiện tại là giải pháp hợp lệ hay không
def is_valid_state(state, num_queens):
    return len(state) == num_queens
#Hàm lấy các cọt để tiếp tục đặt các quân hậu tiếp theo
def get_candidates(state, num_queens):
    if not state:
        return range(num_queens)

    position = len(state)
    candidates = set(range(num_queens))

    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates
# Quay lùi hay gọi là đệ quy tìm kiếm giải pháp khác lúc này chúng ta có thuật toán backtrackinng 
def search(state, solutions, num_queens):
    if is_valid_state(state, num_queens):
        solutions.append(state.copy())
        return

    for candidate in get_candidates(state, num_queens):
        state.append(candidate)
        search(state, solutions, num_queens)
        state.pop()  
# Gói toàn bộ quá trình giải trong một hàm
def solve(num_queens):
    solutions = []
    state = []
    search(state, solutions, num_queens)
    return solutions
# Tương  tự viết Hàm main nhé.
if __name__ == "__main__":
    num_queens = int(input("Nhap vao so quan hau N = "))
    solutions = solve(num_queens)   
    i=0
    for solution in solutions:
        i=+1
        board = np.full((num_queens,num_queens),"-")
        for row, col in enumerate(solution):
            board[row][col]='Q'
        print(f'\nSolution: {solution}')
        print(board)
    
    print(f"\n Tổng số lời giải tìm được: {len(solutions)}")
     # in theo tọa độ nhé 
       