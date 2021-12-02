Code assembly dài quá nên mình không đọc nữa mà giải theo kiểu bruteforce:

![alt_Text](https://i.imgur.com/xnAjcSN.png)

Dễ thấy khi chạy chương trình thì nó sẽ báo ra mỗi kí tự chúng ta nhập sai

![alt_text](https://i.imgur.com/nuzygFV.png)

Đoạn này nghĩa là đến đoạn CTFlearn{+Fru thì mình đúng, còn đến chữ e là bắt đầu sai nên chương trình báo sai

Code bruteforce:

```python
  GNU nano 5.4                          bruteRas.py                                    
from pwn import *
import string
flag = "CTFlearn{"

context.log_level = "critical"
#testcase = string.uppercases = string.lowercases + string.digits + "{_}"
testcase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{_}1234567890+=-_!@#$%^&*()"

p = process(["./Raspberry", flag])

#readlin = p.recvuntil("{")
readlin = p.recv()
readlin = readlin.decode("utf-8")


#print(readlin)

while("}" not in flag):
        for i in testcase:
                p = process(["./Raspberry", flag + i])
                readlin = p.recv()
                readlin = readlin.decode("utf-8")
                if("Bad" not in readlin):
                        flag += i
                        print("flag here: "+ flag)
                        break
                p.close()
```

Chạy là ra flag

![alt_Text](https://i.imgur.com/ULZZDt6.png)
