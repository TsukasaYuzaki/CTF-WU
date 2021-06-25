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


