Tên bài là beginner....

Mở file bằng IDA thì thấy nó được viết khá đơn giản, ít function, và nhìn được ngay thấy hàm main.

Vào hàm main, ta thấy rõ flag có 15 kí tự, được nhập vào từ bàn phím.

![alt_text](https://i.imgur.com/GjXPJBC.png)

xmm0 sẽ là thanh ghi giữ flag mà chúng ta nhập vào, nhưng bài này hay ở chỗ nó so sánh flag chúng ta nhập với chính nó, sau khi đã qua 3 hàm là pshufb, paddd và pxor, nếu sau khi qua 3 hàm này mà flag trở lại như cũ, thì chúng ta thành công.

Giờ đi vào vùng nhớ của 3 hàm này: 

![alt_text](https://i.imgur.com/TV8jPsq.png)

Shuffle sẽ làm nhiệm vụ xáo trộn, add32 là cộng theo mod 2^32, còn XOR là thuật toán XOR thông thường

Giờ giải thích về add32:

uint32_t add32(uint32_t x, uint32_t y) // returns (x+y)%(2^32); any carry out is lost

shuffle sẽ làm nhiệm vụ dịch trái i * 8 bit với (i++)

do đó mình chia mảng theo add32:

```
XOR =   [0xAAF986EB, 0x34F823D4, 0x385F1A8D, 0x49B45876][::-1]
add32 = [0x67637466, 0x13371337, 0xFEE1DEAD, 0xDEADBEEF][::-1]

SHUFFLE =  0x000D0C0A08040F030E090B0501070602

```

(Còn tại sao chia mảng như vậy: 2^32 = 4294967296, do đó mã hex chỉ có tối đa 8 kí tự sau 0x)

Giờ dùng z3:

mình sẽ tạo 3 list, 1 list sử là input ban đầu, 1 list cho input sau khi qua 3 thuật toán trên, dùng z3 Solver để tìm giá trị thỏa mãn

code python giải cả bài:

```python
from z3 import *

XOR =   [0xAAF986EB, 0x34F823D4, 0x385F1A8D, 0x49B45876][::-1]
add32 = [0x67637466, 0x13371337, 0xFEE1DEAD, 0xDEADBEEF][::-1]

SHUFFLE =  0x000D0C0A08040F030E090B0501070602

s1 = [BitVec("x%i" % i, 8) for i in range(16)]
s2 = []

for i in range(16):
	idx = (SHUFFLE >> (i * 8)) & 0xff
	s2.append(s1[idx])
	#print(s2[i])

#he = Concat(1, 2)

w0 = (Concat(s2[3], s2[2], s2[1], s2[0]) + add32[0]) ^ XOR[0]
w1 = (Concat(s2[7], s2[6], s2[5], s2[4]) + add32[1]) ^ XOR[1]
w2 = (Concat(s2[11], s2[10], s2[9], s2[8]) + add32[2]) ^ XOR[2]
w3 = (Concat(s2[15], s2[14], s2[13], s2[12]) + add32[3]) ^ XOR[3]

u0 = Concat(s1[3], s1[2], s1[1], s1[0])
u1 = Concat(s1[7], s1[6], s1[5], s1[4])
u2 = Concat(s1[11], s1[10], s1[9], s1[8])
u3 = Concat(s1[15], s1[14], s1[13], s1[12])

s = Solver()
s.add(w0 == u0)
s.add(w1 == u1)
s.add(w2 == u2)
s.add(w3 == u3)

s.check()
m = s.model()

for i in range(16):
	print((m[s1[i]]))

```


Chạy là ra flag

![alt_text](https://i.imgur.com/inmcOul.png)
