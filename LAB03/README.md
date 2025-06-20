#  LAB 02 – ARTIFICIAL INTELLIGENCE  
##  THỰC HÀNH 06 & 07: Bài toán N-Queens

##  Nội dung thực hành

### 1. Bài toán 4-Queens (TH06)

- **Đề bài mô tả**:  
  Đặt 4 quân hậu lên bàn cờ 4x4 sao cho không có 2 quân hậu nào tấn công lẫn nhau.  
  Quân hậu có thể tấn công theo:
  - Cùng hàng (ngang)
  - Cùng cột (dọc)
  - Đường chéo chính và phụ

- **Yêu cầu đề bài**:
  - Sinh tất cả các cấu hình có thể cho 4 quân hậu.
  - Kiểm tra tính hợp lệ của từng cấu hình.
  - In ra các lời giải thỏa mãn và hiển thị theo cả dạng bảng và tọa độ.

- **Kết quả**:
  - Kết quả bài toán `1` :


backtracking from: [0, 2]
backtracking from: [0, 3, 1]
backtracking from: [0, 3]
backtracking from: [0]
backtracking from: [1, 3, 0, 2]
backtracking from: [1, 3, 0]
backtracking from: [1, 3]
backtracking from: [1]
backtracking from: [2, 0, 3, 1]
backtracking from: [2, 0, 3]
backtracking from: [2, 0]
backtracking from: [2]
backtracking from: [3, 0, 2]
backtracking from: [3, 0]
backtracking from: [3, 1]
backtracking from: [3]
[['-' '-' '-' '-']
 ['-' '-' '-' '-']
 ['-' '-' '-' '-']
 ['-' '-' '-' '-']]
backtracking from: [0, 2]
backtracking from: [0, 3, 1]
backtracking from: [0, 3]
backtracking from: [0]
backtracking from: [1, 3, 0, 2]
...
[['-' '-' 'Q' '-']
 ['Q' '-' '-' '-']
 ['-' '-' '-' 'Q']
 ['-' 'Q' '-' '-']]

---

### 2. Bài toán 8-Queens (TH07)

- **Mô tả**:  
  Mở rộng từ bài toán 4-Queens lên bàn cờ 8x8. Đặt 8 quân hậu sao cho không quân nào tấn công quân khác.

- **Yêu cầu**:
  - Cài đặt thuật toán backtracking để tìm mọi lời giải.
  - In ra tổng số lời giải tìm được.
  - In ra một vài lời giải mẫu minh họa (dưới dạng ma trận bàn cờ và danh sách tọa độ).

- **Kết quả **:
  - Kết quả bài toán `2` :
  - Ví dụ lời giải:


Solution: [0, 4, 7, 5, 2, 6, 1, 3]
[['Q' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' 'Q' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' 'Q']
 ['-' '-' '-' '-' '-' 'Q' '-' '-']
 ['-' '-' 'Q' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' 'Q' '-']
 ['-' 'Q' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' 'Q' '-' '-' '-' '-']]

Solution: [0, 5, 7, 2, 6, 3, 1, 4]
[['Q' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' 'Q' '-' '-']
 ['-' '-' '-' '-' '-' '-' '-' 'Q']
 ['-' '-' 'Q' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' 'Q' '-']
 ['-' '-' '-' 'Q' '-' '-' '-' '-']
 ['-' 'Q' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' 'Q' '-' '-' '-']]

Solution: [0, 6, 3, 5, 7, 1, 4, 2]
[['Q' '-' '-' '-' '-' '-' '-' '-']
 ['-' '-' '-' '-' '-' '-' 'Q' '-']
 ['-' '-' '-' 'Q' '-' '-' '-' '-']
...
 ['-' '-' '-' '-' '-' '-' 'Q' '-']
 ['-' '-' '-' '-' 'Q' '-' '-' '-']]

 Tổng số lời giải tìm được: 92


---




