Hint 1 of 2
Would you be surprised to learn that there's a very famous dragon in cybersecurity?

Hint 2 of 2
How can the code within a compiled executable be analyzed?

Dùng lệnh ```file (Tên chương trình)``` trên linux, ta được: <br/>

```story2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1e3cbcc533556d3e4ce1edb0848a21cef1b10365, for GNU/Linux 3.2.0, not stripped```

Mở bằng IDA 64 bit:

Vào hàm ```main```, ta thấy 1 đoạn dài các lệnh ```[mov rbp+var_x], y```


![alt_text](https://i.imgur.com/bf6wpQH.png)
<br/>
(Trường hợp nếu bạn không có IDA pro (Chắc không xảy ra đâu ._.))

Chịu khó nhập từng giá trị hex được mov (ở bên phải) vào dòng IDC để chuyển nhanh sang từ hex sang dec <br/>

![alt_text](https://i.imgur.com/EyPWQjD.png)
<br/>

Lưu giá trị các bạn có được vao 1 mảng
