Bài này tác giả chia làm 6 step để dễ giải hơn, mình sẽ giải từng step một

# Step 0:
Cái này không tính là 1 step, mà chỉ xem ta có nhập password vào đầu file phần args không

![alt_text](https://i.imgur.com/KMxcJmM.png)

# Step 1:

input bài này được lưu trong r8, trước tiên là tìm xem input của chúng ta có dài quá 0x40 = 64 ký tự hay không

![alt_text](https://i.imgur.com/omzzmdv.png)

Tiếp theo là XOR, xor input của chúng ta với giá trị trong rbx, sau đó lấy giá trị đó so sánh với 0x4B227FF781D59A56

![alt_text](https://i.imgur.com/gXFvxT6.png)

Giá trị trong rbx có thể tìm được bằng cách debug bằng GDB

![alt_text](https://i.imgur.com/Am9WzjK.png)

Ok giờ chỉ việc lấy giá trị này xor ngược lại với 0x4B227FF781D59A56 là ra step1

![alt_text](https://i.imgur.com/nJDNuR6.png)

# Step 2: đơn giản chỉ là kiểm tra ký tự tiếp theo có phải là "_" hay không

![alt_text](https://i.imgur.com/bQcbOvO.png)

# Step 3: Thuật toán add

rax = rax + rbx trong đó, rbx là input của chúng ta, giá trị rax sau khi add so sánh với 0x15764FF46

-> lấy giá trị khi so sánh trừ rax trước khi add là được input đúng
