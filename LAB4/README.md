### Bài 1 – GA cơ bản cho hàm một biến
- Mục tiêu: Tối ưu hàm:  
  
  h(x) = \sin(x) + \cos(x),\quad x \in [0, 2\pi]

- Sử dụng mã hóa nhị phân 16-bit cho biến `x`.
- Vẽ biểu đồ thể hiện sự hội tụ theo thế hệ.



### Bài 2 – GA có tham số linh hoạt
- Mở rộng từ Bài 1, cho phép điều chỉnh các tham số:
  - population_size : (kích thước quần thể)
  - generations : (số thế hệ)
  - crossover_rate : (tỷ lệ lai ghép)
  - mutation_rate : (tỷ lệ đột biến)



### Bài 3 – So sánh các cấu hình thuật toán
- Chạy nhiều cấu hình GA và so sánh tốc độ hội tụ.
- Vẽ biểu đồ thể hiện giá trị tốt nhất theo thời gian với từng cấu hình.



### Bài 4 – So sánh phương pháp chọn lọc
- So sánh 3 chiến lược chọn cá thể cha mẹ trong GA:
  - Roulette Wheel (vòng quay xác suất)
  - Tournament (đấu giải mini)
  - Random Selection (chọn ngẫu nhiên)
- Hiển thị sự khác biệt trong kết quả và tốc độ hội tụ.



### Bài 5 – Tối ưu hàm ba biến và trực quan hóa 3D
- Bài toán:  
  f(x, y, z) = - (x^2 + y^2 + z^2),\quad x, y, z \in [-5, 5]
- Mã hóa mỗi biến bằng 16 bit → mỗi cá thể dài 48 bit.
- Vẽ đồ thị 3D thể hiện sự phân bố của quần thể qua các giai đoạn:
  - Thế hệ đầu tiên
  - Giữa quá trình
  - Thế hệ cuối cùng

