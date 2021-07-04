# Rangoon

This is the third in a series of introductory Reversing Challenges; Reyjkavik, Riyadh and Rangoon. These are designed for people new to Reversing. A little gdb, C and Assembler knowledge should be enough to solve this challenge. Good Luck!

Note that once you solve the challenge, you can use the flag to decrypt the source file used to create the challenge if you are interested in seeing the original C program.

The LiveOverflow channel on YouTube has some great tutorials on reversing, this video has almost everything you need to solve this challenge: https://www.youtube.com/watch?v=VroEiMOJPm8

Đầu tiên mình dùng IDA 64bit mở file lên, chạy vào hàm ```main```:

Để ý cách sử dụng các hàm thì nhận ra bài này khá tương tự [bài trước](https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/CTFlearn/Ramada/Cachgiai.md)

Chuỗi ```CTFlearn{}``` sẽ chiếm 10 ký tự, sau đó mình để ý tập lệnh: <br/>

![alt_text](https://i.imgur.com/ncLdLu9.png)
