Can you tell what this file is reading? chall.S
Hints:
Running this in a debugger would be helpful

Lần này mình không dùng tới IDA

Chương trình này rõ ràng được viết bằng C và sau đó chuyển sang assembly

mở file chall.S lên, mình để ý có đoạn code:

![alt+text](https://i.imgur.com/NjLp3QW.png)

Thấy ```fget``` và ```stdin``` (Standard Input) => flag được nhập từ bàn phím và có 49 ký tự.
