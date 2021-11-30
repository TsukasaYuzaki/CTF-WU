Code bruteforce:
```python
target = "E10a23t9090t9ae0140"

def returnString(a):
    #print(str(a))
    return str(int(a)*3)

def checking(a, b):
    #print(a, b)
    first = 0
    second = 0
    aa = 0
    key = ""
    while first < len(a) and second < len(b):
        if aa%3 == 0:
            key += b[second]
            second += 1
        else:
            key += a[first]
            first += 1
        aa += 1
    return key

def reversetheString(a):
    return a[::-1]
#999eat777
def ReverseAndPlus(a):
    return returnString(a[:3]) + reversetheString(a)

def return_val_a(a):
    return a

def addEATPlus9PlusFirst3Val(a):
    return "Eat" + str(len(a)) + a[:3]


flag = "eat"

for i in range(0, 999):
	for j in range(0, 999):
		debugi = str(i)
		debugj = str(j)
		if(i<10):
			debugi = "00" + str(i)
		if(j<10):
			debugj = "00" + str(j)
		if(i<100 and i>=10):
			debugi = "0" + str(i)
		if(j<100 and j>=10):
			debugj = "0" + str(j)

		aa = checking(ReverseAndPlus(debugi + flag + debugj), addEATPlus9PlusFirst3Val(return_val_a(reversetheString(debugi + flag + debugj ) )))
		#print("i = " + str(i) + "j = " + str(j), end = ": ")
		#print(aa)
		if(aa == target):
			print("Solve!: " + debugi + " " + debugj)
			print("flag: " + debugi + flag + debugj)
			break
```

