import sys 

def bR(c):
    result = 0
    for i in range(0, 8):
        result <<= 1
        b1 = c & 0x01
        result |= b1
        c >>= 1
    return result

def main():
	if(len(sys.argv) == 0 or len(sys.argv) == 1):
		print("[+] Attach agrument [FileName]")
		exit(0)
	f = open(sys.argv[1],"rb")
	data = f.read()
	f.close()
	for d in data:
		print(d, end = ', ')

	key = 0x4b
	encrypt = []
	for d in data:
		encrypt.append(bR(ord(d)) ^ key)
	f = open(sys.argv[1]+ ".enc","wb")
	f.write(bytes(encrypt))
	f.close()
	print("[+] Done")

if __name__ == "__main__":
    main()
