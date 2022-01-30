Đây là bài mã hóa file, mở file challenge 2.py lên thì được hàm mã hóa: 

```python
def bR(c):
    result = 0
    for i in range(0, 8):
        result <<= 1
        b1 = c & 0x01
        result |= b1
        c >>= 1
    return result
```

file flag.txt.enc là file flag đã bị mã hóa, sau đó đem kết quả xor với key là 0x4b rồi nhập vào file.

Giờ việc chúng ta cần làm là đọc file, lấy kết quả có được xor lại với key, rồi đi cho lại qua hàm mã hóa bên trên

Mình sửa lại code 1 tý để print ra list mã hóa trước khi bị xor

```python
import sys 

def bR(c):
    result = 0
    for i in range(0, 8):
        result = result * 2
        b1 = c & 0x01 # 1 or 0
        result |= b1
        c = int(c / 2)
    return result

def main():
	if(len(sys.argv) == 0 or len(sys.argv) == 1):
		print("[+] Attach agrument [FileName]")
		exit(0)
	f = open(sys.argv[1],"r")
	data = f.read()
	f.close()
	key = 0x4b
	encrypt = []

	encrypt0 = []
	for d in data:
		encrypt0.append(ord(d))

	print(encrypt0)


if __name__ == "__main__":
    main()

```




![c](https://user-images.githubusercontent.com/84331340/151705008-38e09388-7a5e-41b9-99dc-06d63ce49388.jpg)

Rồi cho list này xor 1 lần nữa với key, và qua hàm bR() là được flag ban đầu

```python
def bR(c):
    result = 0
    for i in range(0, 8):
        result <<= 1
        b1 = c & 0x01
        result |= b1
        c >>= 1
    return result

lit = [165, 237, 125, 141, 215, 253, 237, 177, 101, 215, 177, 253, 213, 177, 141, 93, 205, 125, 125, 135, 61, 173, 135, 177, 237, 205, 133, 213, 177, 13, 213, 101, 237, 177, 5, 237, 37, 237, 5, 133, 237]

xorval = 0x4b

for i in range(len(lit)):
	lit[i] = lit[i] ^ xorval
	print(chr(bR(lit[i])), end = "")

```


![c](https://user-images.githubusercontent.com/84331340/151705146-5e5cd9fa-e272-4b9d-a034-bf3a935dea75.jpg)

flag: KCSC{welc9me_t9_my_chall3ng3_easy_byte_reverse}

