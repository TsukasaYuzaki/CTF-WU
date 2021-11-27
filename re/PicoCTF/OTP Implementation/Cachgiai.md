# OTP Implementation

## Description
Yay reversing! Relevant files: [otp](https://jupiter.challenges.picoctf.org/static/929a56f71d3918fc903c68b3ea4a76da/otp) [flag.txt](https://jupiter.challenges.picoctf.org/static/929a56f71d3918fc903c68b3ea4a76da/flag.txt)

Bài này cần chú ý 3 hàm là main, valid_char và jumble

![alt_text](https://i.imgur.com/FhkR3wN.png)

Mở file bằng IDA, vào hàm ```main```

Input của chúng ta cần nhập phải có 0x64 (=100) kí tự

![alt_text](https://i.imgur.com/ghQY63z.png)

Sau đó hàm valid_char sẽ kiểm tra các kí tự hợp lệ trong input:

![alt_text](https://i.imgur.com/MriMtnj.png)

Nghĩa là tất cả các kí tự trong input chỉ được nằm trong khoảng ASCII từ 48 đến 57 hoặc từ 97 đến 102, nghĩa là chỉ có 0123456789 và abcdef

Sau khi chúng ta nhập input thì sẽ qua hàm jumble

![alt_text](https://i.imgur.com/3Jp8xav.png)

Sau đó sẽ đem input mới có được sau hàm jumble để đem so sánh với chuỗi: "lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl"

![alt_text](https://i.imgur.com/3s5g7f1.png)

Nếu đúng thì ta chỉ cần XOR input đó với file [flag.txt](https://jupiter.challenges.picoctf.org/static/929a56f71d3918fc903c68b3ea4a76da/flag.txt) để có được flag.

Vậy việc chúng ta cần làm là lấy chuỗi "lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl" đi ngược lại hàm jumble.

Nhưng có vẻ hơi khó vì trong hàm jumble có chia dư nên dò các kí tự sẽ lâu hơn.

Vì thế mình làm theo cách khác, để ý hàm jumpble chỉ mã hóa từng kí tự riêng biệt, nên dù nhập input thế nào thì sau cùng các kí tự trong input đó đều bị mã hóa như nhau,
khá giống bài [easy as GDB](https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/PicoCTF/easy%20as%20GDB/Cachgiai.md)

Nên mình chỉ cần đặt breakpoint ở lệnh ```call _strncmp``` trong hàm main:

![alt_text](https://i.imgur.com/8NSPKsb.png)

Rồi đem so sánh input (Sau khi bị jumble mã hóa) với key có trong bài

![alt_text](https://i.imgur.com/Xx0NtAf.png)

Ok, giờ ```run``` và nhập đủ 100 kí tự vào và thấy được cách các kí tự bị mã hóa rồi so sánh với chuỗi trong bài.

Có thể chây lỳ làm thế, hoặc có thể bruteforce bằng code:

```python
from pwn import *

p = process(["gdb", "./otp"])
p.recvuntil("gef➤  ")
#p.sendline("break *0x0000555555400630")


p.sendline("break *0x0000555555400630")
p.recvuntil("gef➤  ")

testcase="0123456789abcdef"
key=""
"""
first = (p.recvuntil("gef➤  "))
print(first)
"""

for j in range(0, 100):
        first = 0
        second = 0
        print("Trying: " + key)
        for i in testcase:
                p.sendline("run " + key + i + "1"* (99-j) ) #input cần có đủ 100 kí tự, nên dò được bao nhiêu thì bỏ bấy nhiêu kí tự fake
                p.recvuntil("gef➤  ")
                p.sendline("x/s $rsi")
                first = (p.recvuntil("gef➤  "))
                print(first)
                #print(first[31])
                p.sendline("x/s $rdi")
                second = (p.recvuntil("gef➤  "))
                print(second)
                if ((first[31+j]) == (second[31+j])):
                        #print(chr(first[48+j]))
                        print(" ")
                        #print(chr(second[48+j]))
                        key += i
                        break
print("Solved! key: " +key)

```

ok việc còn lại là chạy và đợi vài phút để chương trình bruteforce flag, khá lâu vì cần bruteforce 100 kí tự lận.

![alt_text](https://i.imgur.com/LZ5Ecf8.png)

Ok giờ đem XOR cái này với flag.txt (http://xor.pw/#)

![alt_text](https://i.imgur.com/xgcaQWu.png)

flag: picoCTF{cust0m_jumbl3s_4r3nt_4_g0Od_1d3A_e3647c08}

