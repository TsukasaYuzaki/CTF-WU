# Rangoon

This is the third in a series of introductory Reversing Challenges; Reyjkavik, Riyadh and Rangoon. These are designed for people new to Reversing. A little gdb, C and Assembler knowledge should be enough to solve this challenge. Good Luck!

Note that once you solve the challenge, you can use the flag to decrypt the source file used to create the challenge if you are interested in seeing the original C program.

The LiveOverflow channel on YouTube has some great tutorials on reversing, this video has almost everything you need to solve this challenge: https://www.youtube.com/watch?v=VroEiMOJPm8

Đầu tiên mình dùng IDA 64bit mở file lên, chạy vào hàm ```main```:

Để ý cách sử dụng các hàm thì nhận ra bài này khá tương tự [bài trước](https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/CTFlearn/Ramada/Cachgiai.md)

Chuỗi ```CTFlearn{}``` sẽ chiếm 10 ký tự, sau đó mình để ý tập lệnh: <br/>

![alt_text](https://i.imgur.com/ncLdLu9.png)

Từ lệnh ```cmp rax, 1Ch``` mình rút được độ dài flag bài này là 0x1c (đổi sang ```dec``` thì là 28 ký tự)

# => Chúng ta cần tìm 18 ký tự còn lại
(10 ký tự đã biết là chuỗi CTFlearn{})
=> key của chúng ta có dạng:<br/>
key = "CTFlearn{ooooooooooooooooo}"

Tiếp theo đó mình thu được vị trí của các dấu ```_``` ngăn cách giữa các tự:

![alt_text](https://i.imgur.com/Cayzk9I.png)

Đó là vị trí key[17] và key[22]

=> Được key có dạng:

key = "CTFlearn{oooooooo_oooo_oooo}"

Đó là tất cả những mình có thể làm với IDA.

Đọc qua IDa-view, mình có thể chắc chương trình này được viết bằng C => chắc chắn phải có hàm ```main```

OK giờ mình sẽ sử dụng GDB(linux) để debug

![alt_text](https://i.imgur.com/oDtVfyk.png)

GDB của mình có cài thêm GEF rồi, nhưng không có cũng chả sao

Đầu tiên mình chạy để chương trình nạp bộ nhớ trước

![alt_text](https://i.imgur.com/xggEQfd.png)

Phát hiện ra 1 điều là chương trình bắt chúng ta nhập flag trực tiếp trong lệnh mở luôn, chứ không đợi vào chương trình mới yêu cầu nhập.

Giờ mình sẽ nhập key bên trên thu được vào chương trình

![alt_text](https://i.imgur.com/SE5AOui.png)

ok giờ bắt đầu tiến hành Debug

Mình dùng lệnh ```x/300i``` để xem 300 lệnh đầu của hàm ```main```, sau đó phát hiện ```strcmp``` 

![alt_text](https://i.imgur.com/YXNcizt.png)

Mình sẽ đặt breakpoint ở đây

![alt_text](https://i.imgur.com/HZOMer7.png)

Ok giờ mình chạy chương trình bằng dạng key tìm được trên kia.

![alt_text](https://i.imgur.com/95emq4w.png)

Sau khi chạm breakpoint, chjuowng trình dừng lại, chúng ta có thể dễ dàng thấy được input của chúng ta được lưu trong ```rdi```

![alt_text](https://i.imgur.com/2Wc19Zz.png)

Còn chuỗi được so sánh sẽ nằm trong ```rsi```

![alt_text](https://i.imgur.com/N08ag3P.png)

flag: CTFlearn{Princess_Maha_Devi}

