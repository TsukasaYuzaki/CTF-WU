Hint 1 of 4
I don't think that's the whole story.

Hint 2 of 4
How can you look into a compiled executable file?

Hint 3 of 4
Maybe a command line tool will help?

Hint 4 of 4
What can you make with wool?

Đầu tiên mình dùng lệnh ```file (Tên chương trình)``` trong linux:<br/>
```story: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ccea544c84172f60a939819e4416fdd108982090, for GNU/Linux 3.2.0, not stripped```

Dùng IDA 64bit mở file.

Mở xong chả cần làm gì flag nó hiện lên trước mặt luôn. :D <br/>
![alt text](https://i.imgur.com/7enw5lf.png)
<br/>
flag: bcactf{w0ol_m4k3s_str1ng_ziv4mk3ca91b}
