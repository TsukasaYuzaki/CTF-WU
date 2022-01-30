```

func(0x16ec5c6e,0x1100101)

func:

<1>:  push ebp
<2>:  mov ebp,esp
<3>   mov esp,12s     // 3 dòng này tạo stack

<4>:  mov DWORD PTR[ebp-4],0    //Khởi tạo biến = 0 để chạy vòng lặp

<5>:  cmp [ebp-4],0x501
<6>:  jz  <func+13>		// So sánh biến chạy trong vòng lặp với 0x501( = 1281), nếu bằng thì kết thúc hàm và trả về giá trị

<7>:  mov ebx,[ebp+12]		// Chuyển giá trị thứ 2 trong hàm func vào ebx
<8>:  add [ebp+8],ebx		// cộng giá trị thứ 1 với giá trị thứ 2
<9>:  add [ebp+12],4		// cộng 4 vào giá trị thứ 2
<10>: add [ebp-4],1		// cộng 1 vào biến chạy vòng lặp
<11>: jmp <func+5>

<12>: eax,[ebp+8]  
<13>: pop ebp 			// Trả về kết quả
<14>: ret 
```

Nói đơn giản thì sẽ là thế này


```C++
#include <iostream>
//0x68336c6f
//0x69438174

int main(){
	int a = 0x16ec5c6e, b = 0x1100101;

	int ebp_4 = 0;
	while(ebp_4 != 1281){
	
		a = a + b;
		b = b + 4;
		ebp_4 += 1;
	}

	std::cout << "0x" <<std::hex << a;
}
```

flag: KCSC{0x68336c6f}


	
