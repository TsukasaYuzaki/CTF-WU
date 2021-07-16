# Recklinghausen 

This is the 4th in a series of Beginner Reversing Challenges. If you are new to Reversing, you may want to solve Reykjavik, then Riyadh then Rangoon before solving this challenge. This is a 20 point challenge and is different in two ways from the previous 10 point challenges. Once you get into gdb, b *main+offset is your friend! Good Luck!

Once you solve the challenge you can use the flag to decrypt the souces.zip.enc file provided, if you are interested in seeing the source programs used to create the challenge.

The readme file includes some online resources if you are new to Reversing and Assembler.

https://ctflearn.com/challenge/download/995

----------------------------------------------------------------------

Bài này mình dùng 2 tool là IDA và GDB

![alt_text](https://i.ibb.co/2cGbQmJ/New-Bitmap-Image.png)

Trước tiên là mở file bằng IDA, vào hàm ```main```, 

![alt_text](https://i.ibb.co/BBz8Ywr/New-Bitmap-Image.png)

# Mục đích của mình là đi được vào hàm ```_Z8CheckMsgPKc``` khi chạy chương trình.

Theo hầu hết các challenge của tác giả này, flag phải được nhập trực tiếp trong lời chạy chương trình

![alt_text](https://i.ibb.co/nRWSKqg/New-Bitmap-Image.png)

Giờ là lúc dùng GDB, mình đặt breakpoint ở hàm ```main``` bằng lệnh ```break main``` để chương trình không thoát ngay sau khi chạy

![alt_text](https://i.ibb.co/RP1Cxmv/New-Bitmap-Image.png)

Giờ mình chạy chương trình bằng cách nhập bừa 1 flag vào.

Chương trình sẽ dừng ở hàm ```main```, sau đó cứ ```ni``` hoặc jump đến địa chỉ 0x5555555550fb chứa lệnh ```cmp ebx, 1``` (jump *0x5555555550fb)

![alt_text](https://i.ibb.co/6ZYYnDW/New-Bitmap-Image.png)

ở đây nếu muốn đến được hàm ```_Z8CheckMsgPKc``` thì ta không được thực hiện bước nhày ```jz      loc_11BE```, do đó ```ebx``` phải khác 1, mình dùng lệnh ```info registers``` để xem giá trị đang có trong thanh ghi này

![alt_text](https://i.ibb.co/G2P7nby/New-Bitmap-Image.png)

Ok, thanh ```rbx``` đang chứa giá trị 0x2 do đó ebx = 0x2 (vì là 32 bit đầu của rbx), do đó bước nhảy sẽ không được thực hiện.

cứ ```ni``` cho đến khi gặp lệnh ```cmp     rax, 2```, để đến được hàm ```_Z8CheckMsgPKc``` bên trên thì ta không được thực hiện bước nhày này, do đó mình dùng lệnh ```set $rax = 0x1```, và cứ ```ni``` là vào được hàm ```_Z8CheckMsgPKc```

![alt_text](https://i.ibb.co/fD7tntQ/New-Bitmap-Image.png)

Mình đặt breakpoint ở đầu hàm này để tránh lỗi khi ta step vào hàm

![alt_text](https://i.ibb.co/XLDZhwD/New-Bitmap-Image.png)

Sau đó mình dùng lệnh ```step``` để vào hàm này.

sau đó mình thấy hàm ```strlen```, tiếp tục ```ni``` đến hàm này

![alt_text](https://i.ibb.co/GJQ2fr7/New-Bitmap-Image.png)

Mình không cần step vào trong hàm ```strlen``` này, do đó chỉ cần ```ni``` là đi tiếp được

Cứ ```ni``` cho đến khi gặp lệnh ```cmp    rdx, r8```

dùng ```info registers```, mình thấy được 

![alt_text](https://i.ibb.co/9Tm7tBp/New-Bitmap-Image.png)

Thanh ```r8``` đang giữ độ dài chuỗi nhập của chúng ta, còn thanh ```rdx``` giữ giá trị 0x21( = 33), so sánh 2 thanh này, ta thấy được độ dài flag mà chương trình yêu cầu chúng ta nhập vào

# => flag có 33 ký tự
=> flag sẽ có dạng CTFlearn{ooooooooooooooooooooooo}

Ok giờ chạy lại chương trình, nhập đủ 33 ký tự vào, sau đó làm đúng lại các bước bên trên, chúng ta sẽ thấy khi đến lệnh ```cmp rdx, r8```, 2 thanh này đều giữ giá trị 0x21, nghĩa là chúng ta có thể đi tiếp

![alt_text](https://i.ibb.co/yy6yhKD/New-Bitmap-Image.png)

ok giờ trở lại với IDA, chúng ta thấy được 1 vòng lặp: 

![alt_text](https://i.ibb.co/4dfNsYv/New-Bitmap-Image.png)

# Đến đây thì mình cũng nhìn ra thuật toán kiểm tra của bài này, nó không kiểm tra cả chuỗi, mà kiểm tra mã hex (sau khi được XOR với 1 key là ```esi```) của từng ký tự một, nếu đúng thì rax = rax + 1, cho đến khi rax = rcx, với rcx = độ dài chuỗi ( = 33), thì sẽ dừng hàm check lại

Các bạn có thể tiếp tục giải bằng GDB, bằng cách tìm giá trị của [rdi + rax] (với rax++), lặp đi lặp lại 33 lần, hoặc có thể giải nhanh bằng code python

Lệnh lea (load effecitive)(chuyển các giá trị có tác dụng) mình để ý đoạn 

![alt_text](https://i.ibb.co/6t7HS3P/New-Bitmap-Image.png)

lấy tất cả các giá trị != 0 trong này, tạo thành 1 mảng để XOR, với key là thanh ```esi``` = 0x7e

![alt_text](https://i.ibb.co/YPxwndC/New-Bitmap-Image.png)

code python:

```python
 GNU nano 5.4                                                               Rec.py                                                                        
key = 0x7e
xorval = [0x3d, 0x2a, 0x38, 0x12, 0x1b, 0x1f, 0x0c, 0x10, 5, 0x2c, 0x0b, 0x16, 0x0c, 0x18, 0x1b, 0x0d, 0x0a, 0x0d, 0x0e, 0x17, 0x1b, 0x12, 0x1b, 0x21, 0x3>


for i in xorval:
        print(chr(i ^ key))

```

chạy chương trình, được flag:

CTFlearn{Ruhrfestspiele_Festival}
