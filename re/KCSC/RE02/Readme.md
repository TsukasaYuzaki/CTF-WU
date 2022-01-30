Đây là bài mã hóa file, với thuật toán mã hóa: 

![Untitled](https://user-images.githubusercontent.com/84331340/151706894-73664fb2-7200-43ce-ab40-277368d976e5.png)

Nói đơn giản thì sẽ là thế này

f[0] = f[2] ^ 0xc0
f[1] = f[3] ^ 1
f[2] = f[1] ^ 0xf0
f[3] = f[0] ^ 0xd

Với f[] là chuỗi kí tự đọc được từ file, cứ luân phiên như vậy đến khi hết chuỗi kí tự đọc được.

Giờ đi ngược lại là được file ban đầu

```python
f = open("ASCII_Art_Flag_By_KCSC.txt.EncryptByKCSC", "rb")

flag = f.read()
v5 = 0

#print(len(flag))

def fun(a):
	return bytearray(a)


flag = fun(flag)

#print(flag[3])

v5 = 0

while(v5 < len(flag)):

	flag[v5+0] = flag[v5 + 3] ^ 0xD
	flag[v5+1] = flag[v5 + 2] ^ 0xf0
	flag[v5+2] = flag[v5 + 0] ^ 0xc0
	flag[v5+3] = flag[v5 + 1] ^ 1
	
	
	v5 += 4

f2 = open("decode.txt", "wb")
f2.write(flag)

```

Có vẻ như bước khó nhất của bài này là căng mắt ra mà đọc flag :(

![Untitled](https://user-images.githubusercontent.com/84331340/151707091-030d6fab-fec1-45e1-b904-07824a62920e.png)

flag: KCSC{w3llc0m3_t0_KCSC_<3} (hình như z)
