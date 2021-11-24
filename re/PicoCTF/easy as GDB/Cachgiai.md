The flag has got to be checked somewhere... File: [brute](https://mercury.picoctf.net/static/84a60a8ccee38ac906f28075221fa2e6/brute)

Mờ file bằng IDA, tìm tới hàm main:

![alt_main](https://i.imgur.com/C0xAg9S.png)

Trong chương trình đã chứa sẵn flag (sau khi qua các thuật toán khác nhau)

![alt_text](https://i.imgur.com/MBVMrSo.png)

Có vẻ như flag chúng ta nhập vào phải đi qua đến 3 giai đoạn khác nhau (mình đã rename lại là first, second và third cho dễ đọc)

![alt_text](https://i.imgur.com/q7w1cmQ.png)

Có thể thấy từ flag đúng, trải qua 3 giai đoạn first, second và third thì flag sẽ trở thành Encrypted_flag như ảnh thứ 2, vậy nên muốn có lại flag đúng ban đầu phải đi ngược lại 3 giai đoạn theo thứ tự third, second và first

Nhưng như vậy có vẻ hơi khó khăn, bởi trong chính giai đoạn (hàm) third lại gọi chính lại giai đoạn (hàm) second

![alt_text](https://i.imgur.com/14uAeRp.png)

Vậy nên mình đã tìm ra một cách khác: 

Sau 1 hồi debug với GDB, mình tìm ra được công dụng của 2 lệnh ```cmp``` trong hàm third:

![alt_text]([img]https://i.imgur.com/yxySVYB.png[/img])

(Đương nhiên ở lệnh ```cmp``` thứ 2 là decrypt theo một cách khác nên dù có các giá trị cũng không suy ra flag được)

Từ đó thấy được từ lệnh ```cmp dl, al```, nếu bằng thì giá trị ```eax += 1```, sau đó đem giá trị ```eax``` đó so sánh độ dài của flag đúng

Vậy chương trình Encrypt từng kí tự một, các kí tự trong input lẫn độ dài của input đều không liên quan đến nhau, nghĩa là chỉ cần mình để input là một kí tự bất kì như ```u``` thì sau khi Encrypt vẫn là 1 kí tự cố định nào đó, cho dùng input là ```uasdausd``` hay ```u```

Mình viết 1 đoạn script lợi dụng điều này để bruteforce flag:

```python               
from pwn import *

p = process(["gdb", "./brute"])
p.recvuntil("gef➤  ")
p.sendline("b *0x5655598e")
p.recvuntil("gef➤  ")
testcase = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ>
flag = ""
c = len(flag)
while "}" not in flag:
        for i in testcase:
                p.sendline("run")
                p.sendline(flag+i)
                p.recvuntil("gef➤  ")
                e = 0

                while(e < c):
                        p.sendline("c")
                        p.recvuntil("gef➤  ")
                        e+=1 #tạo vòng lặp để next qua các kí tự đã có trong flag

                p.sendline("x/c $al")
                first = (p.recvuntil("gef➤  "))
                p.sendline("x/c $dl")
                second = (p.recvuntil("gef➤  "))

                 if(first[13] == second[13] and first[14] == second[14] and first[15] == second[15] and first[16] == second[16]):
                        flag += i
                        print(flag)
                        c += 1
                        break

```

Chạy là ra flag:
![alt_text](https://i.imgur.com/lXsGoxz.png)

flag: picoCTF{I_5D3_A11DA7_358a9150}
