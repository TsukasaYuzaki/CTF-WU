**Digitally Encrypted 1**


link download:
[circuit_1.dig](https://objects.bcactf.com/bcactf2/digital1/circuit_1.dig)
[encrypted.txt](https://objects.bcactf.com/bcactf2/digital1/encrypted.txt)

Hint: https://github.com/hneemann/Digital

Dùng cái link trong phần Hint, mở file circuit.dig, được cái hình này:

![alt text](https://i.imgur.com/cx2ohPP.jpg)

Có được key và 5 plain.

Đó là kí hiệu của Xor! mình dùng Xor chuỗi có trong file encrypyed.txt (lưu ý chuyển về dạng 0x nhá!).

Code python: 


```ruby
key = [0xD4, 0xC7, 0x0F, 0x8A, 0x67, 0xD5, 0x45, 0x6D]
f1 = [0xB6, 0xA4, 0x6E, 0xE9, 0x13, 0xB3, 0x3E, 0x19]
f2 = [0xBC, 0xA6, 0x7B, 0xD5, 0x10, 0xB4, 0x36, 0x32]
f3 = [0xA4, 0xB5, 0x6A, 0xFE, 0x13, 0xAC, 0x1A, 0x1E]
f4 = [0xBD, 0xAA, 0x7F, 0xE6, 0x02, 0xE4, 0x77, 0x5E]
f5 = [0xED, 0xF6, 0x3A, 0xB8, 0x50, 0xE6, 0x70, 0x10]

j = 0
for tu in key:
    print (tu ^ f1[j])
    j = j + 1
    
j = 0
for tu in key:
    print (tu ^ f2[j])
    j = j + 1
    
j = 0
for tu in key:
    print (tu ^ f3[j])
    j = j + 1
    
j = 0
for tu in key:
    print (tu ^ f4[j])
    j = j + 1
    
j = 0
for tu in key:
    print (tu ^ f5[j])
    j = j + 1

```
Chạy chương trình, ta được chuỗi:
```
98
99
97
99
116
102
123
116
104
97
116
95
119
97
115
95
112
114
101
116
116
121
95
115
105
109
112
108
101
49
50
51
57
49
53
50
55
51
53
125
```

Convert nó từ ```dec``` sang ```string``` là được! 


![alt text](https://i.imgur.com/cx2ohPP.jpg)
