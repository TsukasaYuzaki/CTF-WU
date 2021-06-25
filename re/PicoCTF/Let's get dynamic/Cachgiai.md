Can you tell what this file is reading? chall.S
Hints:
Running this in a debugger would be helpful

Lần này mình không dùng tới IDA

Chương trình này rõ ràng được viết bằng C và sau đó chuyển sang assembly

mở file chall.S lên, mình để ý có đoạn code:

![alt+text](https://i.imgur.com/NjLp3QW.png)

Thấy ```fget``` và ```stdin``` (Standard Input) => flag được nhập từ bàn phím và có 49 ký tự.

Ngoài ra còn có ```memcmp```, ```strlen``` và ```puts```

![alt_text](https://i.imgur.com/AK6LPIC.png)

Thấy có ```memcmp```, mình sẽ tìm địa chỉ và đặt breakpoint ở đây

Trước tiên là phải compile file đã, vì đây mới là file code.

Mình dùng gcc:

```gcc -c chall.S``` <br/>
```gcc chall.o -o chall```

Giờ mình đã có file có thể xử lý được.

![alt_text](https://i.imgur.com/5XFAflF.png)

(Đương nhiên 123 không phải là flag chúng ta đang tìm rồi)

Ok! giờ sử dụng GDB

![alt_text](https://i.imgur.com/HI0eFNl.png)

Trước tiên mình chạy để GDB nạp bộ nhớ

![alt_text](https://i.imgur.com/fnvC6St.png)

(Thứ chúng ta cần tìm giờ là địa chỉ của ```memcmp```)

Vì đã xác định đây là chương trình C, nên chắc chắn phải có hàm ```main```, mình dùng lệnh: ```x/100i main``` để xác định 100 lệnh sau hàm ```main```

Phát hiện ```memcmp``` nằm ở địa chỉ: ```0x5555555552e9```

![alt_text](https://i.imgur.com/Xvy20C5.png)

Giờ đặt breakpoint ở đây:

![alt_text](https://i.imgur.com/mkfzSCi.png)

và tiến hành chạy chương trình: (bằng lệnh ```run```)

![alt_text](https://i.imgur.com/73k1HFM.png)

Nhưng tuy nhiên sau khi nhập bừa vài key, mình chỉ nhận được 1 phần nhỏ của flag cần tìm, được ném vào thanh rsi

![alt_text](https://i.imgur.com/TSvUk8P.png)
