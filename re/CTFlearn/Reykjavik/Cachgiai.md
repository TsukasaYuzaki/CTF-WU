Good beginning Reversing challenge - jump into gdb and start looking for the flag!

Vì một lý do nào đó mà bài này được xếp vào mục easy, trong khi đó 1 bài dễ hơn hẳn [PIN](https://github.com/TsukasaYuzaki/CTF-WU/tree/main/re/CTFlearn/PIN) lại ở trong mục medium :l

![alt_text](https://i.imgur.com/JjUWURn.png)

Dùng IDA 64 bit mở file, vào hàm ```main```, thu được 1 cờ fake là: CTFlearn{Is_This_A_False_Flag?}

Tiếp theo đó mình để ý đoạn: 

![alt_text](https://i.imgur.com/g1QJtS2.png)

Có biến lạ là: ```data```, ```qword_4018```, ```qword_4020```, ```qword_4028```,  ```qword_4029```,  ```qword_402A```

Vào vùng nhớ của các biến này, được các giá trị hex:

![alt_text](https://i.imgur.com/6mvps1t.png)
