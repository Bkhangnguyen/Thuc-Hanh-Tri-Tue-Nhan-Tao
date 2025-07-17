#  Nhận diện chữ số viết tay với CNN (PyTorch)

Dự án sử dụng mạng nơ-ron tích chập (CNN) để phân loại ảnh chữ số viết tay từ tập dữ liệu MNIST.

---

##  Công nghệ sử dụng

- **PyTorch**: Framework học sâu mạnh mẽ, hỗ trợ GPU.
- **Torchvision**: Hỗ trợ tải và xử lý dữ liệu ảnh.
- **NumPy, Matplotlib**: Dùng để xử lý và trực quan hóa dữ liệu.

---

## Mô hình và thuật toán

- **Mạng CNN**: Bao gồm các tầng convolution, pooling, fully connected để trích xuất đặc trưng và phân loại.
- **Loss Function**: `CrossEntropyLoss` – dùng cho bài toán phân loại nhiều lớp.
- **Optimizer**: `SGD` (Stochastic Gradient Descent) kết hợp momentum để tăng tốc độ hội tụ.

---

##  Cách hoạt động

1. **Convolution**: Tìm đặc trưng cơ bản như cạnh, góc.
2. **ReLU Activation**: Loại bỏ giá trị âm, làm nổi bật đặc trưng.
3. **Pooling**: Giảm kích thước ảnh, giữ thông tin chính.
4. **Fully Connected**: Tổng hợp đặc trưng để phân loại.
5. **Training**: Tối ưu trọng số qua nhiều vòng lặp (epoch).
6. **Learning Rate**: Điều chỉnh tốc độ cập nhật trọng số.

---

##  Các Bài tập 

###  Câu 1: Thay đổi số lượng epoch
- **Thay đổi**: Tăng số epoch từ 5 lên 10.
- **Kết quả**: Mô hình học kỹ hơn, loss giảm đều, accuracy tăng.
- **Lưu ý**: Epoch quá nhiều có thể gây overfitting.

---

###  Câu 2: Thêm tầng tích chập
- **Thay đổi**: Thêm tầng `conv3`, điều chỉnh các layer phía sau.
- **Kết quả**: Mô hình học đặc trưng phức tạp hơn, độ chính xác tăng.
- **Lưu ý**: Cần cân bằng độ phức tạp với lượng dữ liệu để tránh overfitting.

---

### Câu 3: Thử nghiệm learning rate
- **Thử nghiệm**: 
  - `lr = 0.001`: Học chậm, ổn định.
  - `lr = 0.1`: Học nhanh, dễ dao động.
- **Kết luận**: Learning rate quá cao có thể làm mô hình không hội tụ.

---

###  Câu 4: Hiển thị feature map tầng conv2
- **Thay đổi**: Hiển thị thêm feature map từ tầng `conv2`.
- **Kết quả**:
  - `conv1`: Hiển thị nét đơn giản (cạnh, đường).
  - `conv2`: Nét trừu tượng hơn (mảng, vùng).
- **Giải thích**: Các tầng sau học đặc trưng tổng hợp từ tầng trước.

---

##  Tổng kết

Mô hình CNN hoạt động hiệu quả trên bài toán phân loại chữ số MNIST. Các thí nghiệm cho thấy ảnh hưởng rõ rệt của số epoch, cấu trúc mạng và learning rate đến kết quả cuối cùng. Việc trực quan hóa feature map giúp hiểu rõ hơn cách CNN học từ dữ liệu.

