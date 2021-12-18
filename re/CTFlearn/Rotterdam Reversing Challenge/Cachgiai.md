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

=> flag: Rotterda

![alt_text](https://i.imgur.com/nJDNuR6.png)

# Step 2: đơn giản chỉ là kiểm tra ký tự tiếp theo có phải là "_" hay không

=> flag: Rotterda_

![alt_text](https://i.imgur.com/bQcbOvO.png)

# Step 3: Thuật toán add

rax = rax + rbx trong đó, rbx là input của chúng ta, giá trị rax sau khi add so sánh với 0x15764FF46

-> lấy giá trị khi so sánh trừ rax trước khi add là được input đúng

![alt_text](https://i.imgur.com/MeXTmcj.png)

![New Bitmap Image (3)](https://user-images.githubusercontent.com/84331340/146403244-73cd9ef6-d308-4f9b-b38f-2c80215ac4a4.png)

=> flag: Rotterda_P0rt

# Step 4: Thuật toán and

Đây là step mình mất nhiều thời gian nhất vì nó sử dụng thuật toán chía dư 

(n % 2^i = n & (2^i - 1))

Nhưng sau vài tiếng loáy hoáy thì mình nhận ra mấu chốt không nằm ở đây, tại vì cái so sánh của nó là jb chứ không phải je hay jne (jb: jump below, je: jump equal, 
jne: jump not equal), nên nhìn đoạn sau thì dễ hẳn, chỉ là thuật toán sub

![alt_text](https://i.imgur.com/8JhScw7.png)

![alt_text](https://i.imgur.com/oi6yGyT.png)

Nên việc còn lại quá đơn giản

![alt_text](https://i.imgur.com/1OjOsY9.png)

=> flag: Rotterda_P0rt_Rh1ne

Tiếp theo là kiểm tra ký tự "_"

=> flag: Rotterda_P0rt_Rh1ne_

# Step 5: Thuật toán mul

Đây là một thuật toán khá hay vì nó ảnh hưởng đến 2 thanh ghi

Sau khi mul, thì dó số quá to, nên sẽ chia ra làm 2 phần: 

Trước khi mul:

![alt_text](https://i.imgur.com/XSYKhwy.png)

Sau khi mul:

![alt_text](https://i.imgur.com/I4eHjGo.png)

=> Giá trị nhân ra đầy đủ của chúng ta là: 0x6A8754493837F7D400A77B9BE0

Nên lấy cái này chia lại cho 0xdeb4fa4d998c32ff là được 

Mình dùng python, tại IDA số to quá k chia được :V

Code: 

```python
a = 0x6A8754493837F7D400A77B9BE0

b = 0xdeb4fa4d998c32ff

print(hex(int(a/b)))
```

![alt_text](https://i.imgur.com/uY0c64G.png)

Bước tiếp theo là ktra "_"

=> flag: Rotterda_P0rt_Rh1ne_Bl1tz_

# Step 6: Thuật toán div

Đoạn này sẽ xem ký tự cuối trong flag của chúng ta có phải là 5 kí tự không, nếu nhiều hơn sẽ thoát chương trình

![alt_text](https://i.imgur.com/tUtrpGt.png)

Thuật toán này khá là giống thuật toán nhân mul bên trên, nhưng lúc này rdx giữ phần dư của phép chia

![alt_text](https://i.imgur.com/Th0LKte.png)

=> đáp số của chúng ta là số bị chia, sao cho khi lấy rax (= 0x1f6ff5218c40de9c) chia cho số đó thì được thương 0x4F5352 và dư 0x55930DBBE

=> lấy rax trừ đi số dư rồi chia cho thương là được input cần nhận

![alt_Text](https://i.imgur.com/tZSCieN.png)

=> flag: CTFlearn{Rotterda_P0rt_Rh1ne_Bl1tz_W1tte}
