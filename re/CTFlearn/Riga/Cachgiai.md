Mở file bằng IDA, vào hàm main:

Điều đặc biệt ở bài này là chương trình có đến 2 hàm check không cần đến, và nhiệm vụ của chúng ta làm tìm ra 2 hàm này trong 3 hàm

![alt_text](https://i.imgur.com/PbioIyA.png)

Đó là HerbalTea2, HerbalTea1 và HerbalTea0

Và để biết chương trình sẽ vào hàm nào thì mình để ý lệnh 


```
sub     eax, 1
jz      short loc_11A1
```

jz sẽ nhảy đến hàm HerbalTea0 nếu có zflag, tức là ở đây eax == 0

Trên đó có lệnh sub eax cho 1

vậy thì trước đó eax phải == 1.


![alt_text](https://i.imgur.com/DSz8OXw.png)

Trước đó có 1 vòng loop để đưa input của chúng ta qua hàm ```BlackRyeBread```

Dễ thấy eax đã được chuyển vào đó giá trị 1

![alt_text](https://i.imgur.com/lEIxU22.png)

Đây là hằng số => dù thế nào thì chương trình chắc chắn cũng chỉ có thể đi qua hàm HerbalTea0

Decompile hàm này

![alt_text](https://i.imgur.com/OJP6u8s.png)

Từ đoạn code trên có thể thấy flag của chúng ta có 30 kí tự

Sau đó, chương trình đem XOR flag với 0xDE, rồi qua 1 số thuật toán if else và XOR 1 lần nữa với 0xCB, sau đó đem kết quả có được so sánh với mảng pickles0

Vào mảng pickles0, thu được 1 dãy giá trị hex:

![alt_text](https://i.imgur.com/TSJ3yy3.png)

Ok giờ lấy mảng này đi ngược lại các thuật toán trên là ra flag

Code giải mã:

```python
pickles0 = [0x9f, 0xae, 0x9c, 0xb6, 0xbd, 0xb9, 0xef, 0xeb, 0xe6, 0x9e, 0xb9, 0xec, 0xb3, 0xb9, 0xe3, 0xb9, 0xbb, 0xa8, 0x89, 0xe3, 0xbd, 0xef ,0xbb, 0x96, 0xb9, 0xed, 0xe3, 0x89, 0xb9, 0xe4]
xorval = 0xde

a = []

for i in pickles0:
	a.append(i ^ 0xcb)

for i in range(len(a)):
	if(a[i] + 78 - 17 < 0x7e):
		a[i] = a[i] + 78
	else:
		y = a[i] - 112
		z = a[i] - 17
		if(z<0x20):
			z = y
		a[i] = z

for i in range(len(a)):
	print(chr(a[i]), end = "")

```

Flag: CTFlearn{Daugava_R1ver_Latv1a}
