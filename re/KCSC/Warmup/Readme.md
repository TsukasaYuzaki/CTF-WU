func(0x16ec5c6e,0x1100101)

func:

	<1>:  push ebp
	<2>:  mov ebp,esp
	<3>   mov esp,12s     // 3 dòng này tạo stack

	<4>:  mov DWORD PTR[ebp-4],0    //Khởi tạo biến =0 hạy vòng lặp

	<5>:  cmp [ebp-4],0x501
	<6>:  jz  <func+13>

	<7>:  mov ebx,[ebp+12]
	<8>:  add [ebp+8],ebx
	<9>:  add [ebp+12],4
	<10>: add [ebp-4],1
	<11>: jmp <func+5>


	<12>: eax,[ebp+8] 
	<13>: pop ebp 
	<14>: ret 


	
