We have recovered a binary and a text file. Can you reverse the flag.

Chúng ta có 2 file là [rev](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev) và [rev_this](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this)

file rev là chương trình C:

![alt_text](https://i.imgur.com/912Pax3.png)

và file rev_this là file text:

![alt_text](https://i.imgur.com/1xsuSwz.png)

Dùng IDA mở file rev lên, vào hàm main: 

![alt_text](https://i.imgur.com/oRecg4Y.png)

Có vẻ như chương trình kiểm tra 2 file là: flag.txt và rev_this, nếu thiếu 1 trong 2 thì sẽ không chạy được chương trình.

=> đây là chương trình mã hóa flag, và rev_this chính là flag sau khi bị mã hóa 1 bước.

Thuật toán mã hóa khá đơn giản: 

kiểm tra biến chạy j (from 8 to 22), nếu j & 1 != 0 thì flag[j] -= 2, nếu không thì flag[j] -= 5

dễ thấy quá trình and(&) từ 8 đến 22 với 1 giống với từ 1 đến 14 với 1

Code giải mã: 

```
from z3 import *

#picoCTF{w1{1wq85jc=2i0<} 

flag = "w1{1wq85jc=2i0<"

#r3v3rs37ee84d27

a = []

for i in range(0, len(flag)):
	a.append(ord(flag[i]))

s = Solver()

s1 = [BitVec("x%i" %i, 8) for i in range(15)]

con = 0

while(con < 15):
	if((con & 1) != 0):
		s.add(s1[con] - 2 == a[con])
	else:
		s.add(s1[con] + 5 == a[con])
	con += 1

s.check()

m = s.model()

for i in range(15):
	print(chr(m[s1[i]].as_long()), end = '')
```

Flag: picoCTF{r3v3rs37ee84d27}

