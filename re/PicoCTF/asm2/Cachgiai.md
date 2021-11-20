```
asm2(0x4,0x21) 



asm2: 
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] // eax = 0x21
	<+9>:	mov    DWORD PTR [ebp-0x4],eax // [ebp-0x4] = 0x21
	<+12>:	mov    eax,DWORD PTR [ebp+0x8] // rax = 0x4
	<+15>:	mov    DWORD PTR [ebp-0x8],eax // [ebp-0x8] = 0x4
	<+18>:	jmp    0x509 <asm2+28>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0x74 //add 116
	<+28>:	cmp    DWORD PTR [ebp-0x8],0xfb46 //cmp 4, 64236
	<+35>:	jle    0x501 <asm2+20>
	<+37>:	mov    eax,DWORD PTR [ebp-0x4]
	<+40>:	leave  
	<+41>:	ret    

```

chuyển thành code C sẽ là:
```
int a = 4;
int b = 33;

do{
    a += 116;
    b += 1;
}
While(a < 64236)

return b;
```


Flag: 0x24C
