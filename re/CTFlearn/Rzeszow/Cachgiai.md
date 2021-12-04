Bài này tác giả cố tình cho thêm tùy chọn "-v" để chương trình dễ đi, và có thể lợi dụng điều đó để Brute force một cách dễ dàng

Mình sẽ giải theo 2 cách, cách 1 là Brute force (Vét cạn)

# Cách 1: Brute force

Mở file bằng IDA, vào hàm main, thấy được đoạn code:

![alt_text](https://i.imgur.com/qtHDrBd.png)

Tức là nếu người dùng thêm "-v" vào input thì chương trình sẽ setb cho r15b, trong đó r15b đang = 0 do đã được XOR với chính mình ở đoạn code bên trên

Và sau đó sẽ kiểm tra r15b

![alt_text](https://i.imgur.com/IaPKuiC.png)

Nói dễ hiểu sẽ là như thế này:

![alt_text](https://i.imgur.com/OrVvclp.png)

Tức là chương trình sẽ kiểm tra từng kí tự chúng ta nhập vào với 1 cái gì đó chưa biết, nếu trùng thì sẽ có thông báo để kiểm tra kí tự tiếp theo, và các kí tự không liên quan đến nhau

![alt_text](https://i.imgur.com/6HpNcSt.png)

Đoạn này thể hiện từ chữ "K" thì mình đúng, còn sau đó là sai

Lợi dụng điều này để brute force flag:

Code brute force:

```python
  GNU nano 5.4                                            Brute.py                                                      
from pwn import *

testcase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+=_{}?./"

flag = "CTFlearn{"

context.log_level = "critical"

p = process(["./Rzeszow", flag + "K034567890}", "-v"])
readline = p.recv()
readline = readline.decode("utf-8")

countVal = 1

for i in range(10):
        for j in testcase:
                p = process(["./Rzeszow", flag + j + "."*(18-len(flag)) + "}", "-v"])
                print("./Rzeszow", flag + j + "."*(18 - len(flag)) + "}", " -v")
                readline = p.recv()
                readline = readline.decode("utf-8")
                if (readline.count("Woow") == countVal):
                        countVal += 1
                        flag += j
                        p.close()
                        break

print("Solved, flag: " + flag + "}")

```

Chạy là ra flag:

![alt_text](https://i.imgur.com/etcodjW.png)

flag: CTFlearn{K0nstancj}

# Cách 2: Decompile

Ok giờ không sử dụng tùy chọn -v nữa.

Đọc code Decompile thì thấy phần bên trong CTFlearn{} sẽ được check thế này:

![alt_text](https://i.imgur.com/PQ3JUT7.png)

trong đó ```kernelenc``` chính là đoạn string dài ngoằng:

![alt_text](https://i.imgur.com/ZpI2tRZ.png)

Ok giờ viết code kiểm tra là được

## Lưu ý 1 chút là n % 2^i = n & (2^i - 1), nên mình viết %512 thay vì %0x1FF

```python
target = "W8Hj?1VESL^g4xwcvtW%humtEosd$Fq^dXPvi$#sSEe@o618Zl9.5PFrvC%O_E*LB%Igl8qur9SuLAp4MkK#pRzwJHI*Fn9mUs%mGK^RQKO.G*JFJvV%?VJpCpVF9eJuz5&kB!&_VF5DrF?U?jfm&x^9aC7X2(&cGGzbLbOsSOuBeq*ZT%fpc&9riTDO5X%RuTKI@vCqu#CsTAp$Q9WoXJv96.ySdB2EfMK*$NX?.U*aDrfPQQPhFB9cC6y0hMGvbgjBogSux65gTL#Cm9TQt7nTayu9Vr%thh2GnnikE8JnIwlHfreZep^sZ6IrnXT#qu50Lv.Rd_XPDfgwzWcJ3ISjKM!ftRllVyF$?RE_dcJT5&uKZJ!WsqR853uLzcs!8&VyRuTDsiq#6PdmBNlPI$tPi?wZ5$ACCf9yda!OkP.Dc73Nx.Nt1Rj0O.?P!sZDB^d0LN1qXR31!t?OZ#mm7SfZHPO*4gx1J0nyC^d2EKeq^f4h7mSqaIcMv0ZT@G0M"

kernelenc1 = []
kernelenc2 = []

for i in range(len(target)):
	kernelenc1.append(ord(target[i]))
	kernelenc2.append(ord(target[i]))


#n % 2^i = n & (2^i - 1)

v21val = 0xBAADF00D
v22val = 0xBAADF010
v23val = 0xBAADF013
v24val = 0xBAADF016
v25val = 0xBAADF019
v26val = 0xBAADF01C
v27val = 0xBAADF01F
v28val = 0xBAADF022
v29val = 0xBAADF025
v30val = 0xBAADF028 

o = ""

char1 = 0 #Đếm xem mình đã có kí tự thứ 1 hay chưa, có thì mới ktra kí tự tiếp theo
char2 = 0
char3 = 0
char4 = 0
char5 = 0
char6 = 0
char7 = 0
char8 = 0
char9 = 0
char10 = 0

count = 0

for i in range (len(target)):
	if(char1 == 0 and kernelenc1[i] == kernelenc2[v21val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i]) % 512]):
			char1 += 1
			o += target[i]
for i in range (len(target)):
	if(char1 == 1 and char2 == 0 and kernelenc1[i] == kernelenc2[v22val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i]  + 3 ) % 512]):
			char2 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 0 and kernelenc1[i] == kernelenc2[v23val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 6) % 512]):
			char3 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 0 and kernelenc1[i] == kernelenc2[v24val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 9) % 512]):
			char4 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 0 and kernelenc1[i] == kernelenc2[v25val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 12) % 512]):
			char5 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 0 and kernelenc1[i] == kernelenc2[v26val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 15) % 512]):
			char6 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 0 and kernelenc1[i] == kernelenc2[v27val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 18) % 512]):
			char7 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 1 and char8 == 0 and kernelenc1[i] == kernelenc2[v28val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 21) % 512]):
			char8 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 1 and char8 == 1 and char9 == 0 and kernelenc1[i] == kernelenc2[v29val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 24) % 512]):
			char9 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 1 and char8 == 1 and char9 == 1 and char10 == 0 and kernelenc1[i] == kernelenc2[v30val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 27) % 512]):
			char10 += 1
			o += target[i]
			break

print(o)
```

Chạy là ra thôi

![alt_text](https://i.imgur.com/2Z54dWA.png)

flag: CTFlearn{K0nstancj}
