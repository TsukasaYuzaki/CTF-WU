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

Nhưng tuy nhiên sau khi nhập, mình chỉ nhận được 1 phần nhỏ của flag cần tìm, được ném vào thanh rsi

![alt_text](https://i.imgur.com/TSvUk8P.png)

Giờ mình mới để ý đoạn code trong file chall.S:

```
   .string "\207\312\304\371\307m\2753&V\035A"
   .string "\231]\314~\025\345\225\343\177\013M\214\034SJG\246i\372\026\0323@\033jW\204\370\311}\221\350T\236pr"
```
 Có vẻ như hàm ```memcmp``` không so sánh đầy đủ 49 ký tự trong flag, mà chỉ dừng lại ở việc so sánh 12 kí tự đầu trong 49 ký tự của flag
 
 Để ý input chúng ta nhập vào được chứa trong thanh ```rdi```
 
 Nhưng sau đó mình thấy 1 vấn đề nhỏ
 
 ![alt_text](https://i.imgur.com/4Rpxp1k.png)
 
 Tái sao tác giả phải dùng tới ```strlen```, mặc dù đã biết flag có 49 ký tự? hay là do cái ```strlen``` này không phải 49, mà là của 1 trong 2 cái string trên kia
 
Như mình đã nói ở trên, input của chúng ta chứa trong thanh ```rdi```, đế ý trước lệnh ```call  strlen@PLT``` có lệnh ```movq %rax, %rdi``` (movq với thanh ghi 64bit, movl với thanh 32bit), tức là thanh rax giờ đang chứa input của chúng ta, nên giờ mình sẽ chuyển 49 kí tự trực tiếp vào thanh eax(1 nửa của thanh rax)

Giờ mình có thể bỏ lệnh ```call  strlen@PLT```, thay vào đó là lệnh ```movl $49, %eax```

OK! giờ compile lại file từ bước gcc, sau đó debug, đặt breakpoint là được flag!

![alt_text](https://i.imgur.com/IFrPzBH.png)

flag: picoCTF{dyn4m1c_4n4ly1s_1s_5up3r_us3ful_9266fa82}
