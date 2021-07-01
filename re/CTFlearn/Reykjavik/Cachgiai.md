Good beginning Reversing challenge - jump into gdb and start looking for the flag!

Vì một lý do nào đó mà bài này được xếp vào mục easy, trong khi đó 1 bài dễ hơn hẳn [PIN](https://github.com/TsukasaYuzaki/CTF-WU/tree/main/re/CTFlearn/PIN) lại ở trong mục medium :l

![alt_text](https://i.imgur.com/JjUWURn.png)

Dùng IDA 64 bit mở file, vào hàm ```main```, thu được 1 cờ fake là: CTFlearn{Is_This_A_False_Flag?}

Tiếp theo đó mình để ý đoạn: 

![alt_text](https://i.imgur.com/g1QJtS2.png)

Có biến lạ là: ```data```, ```qword_4018```, ```qword_4020```, ```qword_4028```,  ```qword_4029```,  ```qword_402A```

Vào vùng nhớ của các biến này, được các giá trị hex:

![alt_text](https://i.imgur.com/6mvps1t.png)

Giờ quay lại đoạn:

![alt_text](https://i.imgur.com/g1QJtS2.png)

ta để ý lệnh: ```mov     rax, 0ABABABABABABABABh``` (Chữ h cuối cùng không quan tâm, đó chỉ là biểu thị của hex(cơ số 16))

thanh ```rax``` giờ đang giữ giá trị 0xABABABABABABABAB, và sau đó được XOR liên tiếp với các biến lạ trên kia.

Nhưng tại sao lại cần đến một chuỗi AB dài như vậy, giờ để vùng nhớ của các biến lạ cũng được định nghĩa rất dài

```
0000000000004010                 public data
.data:0000000000004010 data            dq 0C5D9CACEC7EDFFE8h   ; DATA XREF: main+5D↑r
.data:0000000000004018 qword_4018      dq 0DD9BE7F4CED2EED0h   ; DATA XREF: main+83↑r
.data:0000000000004020 qword_4020      dq 0C5CAC7CEC8E2F4CEh   ; DATA XREF: main+8D↑r
.data:0000000000004028 byte_4028       db 0CFh                 ; DATA XREF: main+99↑r
.data:0000000000004029 byte_4029       db 0F4h                 ; DATA XREF: main+AC↑r
.data:000000000000402A byte_402A       db 0D6h                 ; DATA XREF: main+BA↑r
```

Chuyển về dạng 0x(chữ số)(chứ số) thì được độ dài bằng đúng chuỗi 0xAB...B

```python
data =       [0xC5, 0xD9, 0xCA, 0xCE, 0xC7, 0xED, 0xFF, 0xE8]
qword_4018 = [0xDD, 0x9B, 0xE7, 0xF4, 0xCE, 0xD2, 0xEE, 0xD0]    
qword_4020 = [0xC5, 0xCA, 0xC7, 0xCE, 0xC8, 0xE2, 0xF4, 0xCE]    
byte_4028 = 0xCF    
byte_4029 = 0xF4    
byte_402A = 0xD6
```
=> Chúng ta cần XOR từng giá trị có được với 0xAB, sau đó chuyển sang kiểu ```char```, đó chính là flag cần tìm, nhưng lại phát sinh một vấn đề nhỏ, đó là mỗi chuỗi sau khi XOR đều bị đảo ngược, chúng ta chỉ cần đảo ngược chuỗi một lần nữa là được!

code ```python```: (sorry mới học python nên code hơi ngáo)

```python
data = [0xC5, 0xD9, 0xCA, 0xCE, 0xC7, 0xED, 0xFF, 0xE8]
qword1 = [0xDD, 0x9B, 0xE7, 0xF4, 0xCE, 0xD2, 0xEE, 0xD0]
qword2 = [0xC5, 0xCA, 0xC7, 0xCE, 0xC8, 0xE2, 0xF4, 0xCE]
byte28 = 0xCF
byte29 = 0xF4
byte2a = 0xD6

key = 0xAB

flag1 = ''
flag2 = ''
flag3 = ''
flag = ''
for i in data:
        flag1 += chr (i ^ key)

for i in qword1:
        flag2 += chr(i ^ key)

for i in qword2:
        flag3 += chr(i ^ key)
        
print(flag1[::-1])
print(flag2[::-1])
print(flag3[::-1])

print(chr(byte28 ^ key))
print(chr(byte29 ^ key))
print(chr(byte2a ^ key))

```
chạy chương trình là ra flag

![alt_text](https://i.imgur.com/DS4Mgvg.png)

flag: CTFlearn{Eye_L0ve_Iceland_}
