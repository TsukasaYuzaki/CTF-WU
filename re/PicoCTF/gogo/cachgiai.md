Hmmm this is a weird file... enter_password. There is a instance of the service running at mercury.picoctf.net:20140.

Mở file bằng IDa 32 bit, đi vào hàm ```main.checkPassword```:

![alt_text](https://i.imgur.com/DFiQFe2.png)

Decompile hàm này, thu được key ```861836f13e3d627dfa375bdb8389214e```

```C
oid __cdecl main_checkPassword(string input, bool _r1)
{
  __int32 v2; // eax
  int v3; // ebx
  uint8 key[32]; // [esp+4h] [ebp-40h] BYREF
  char v5[32]; // [esp+24h] [ebp-20h]
  void *retaddr; // [esp+44h] [ebp+0h] BYREF

  while ( (unsigned int)&retaddr <= *(_DWORD *)(*(_DWORD *)(__readgsdword(0) - 4) + 8) )
    runtime_morestack_noctxt();
  if ( input.len < 32 )
    os_Exit(0);
  sub_8090B18();
  qmemcpy(key, "861836f13e3d627dfa375bdb8389214e", sizeof(key));
  sub_8090FE0();
  v2 = 0;
  v3 = 0;
  while ( v2 < 32 )
  {
    if ( (unsigned int)v2 >= input.len || (unsigned int)v2 >= 0x20 )
      runtime_panicindex();
    if ( (key[v2] ^ input.str[v2]) == v5[v2] )
      ++v3;
    ++v2;
  }
}
```
Để ý lệnh: ``` if ( (unsigned int)v2 >= input.len || (unsigned int)v2 >= 0x20 )```

key chúng ta nhập vào sẽ có độ dài >= 0x20 (CHuyển từ ```hex``` sang ```dec``` thì là 32) kí tự, nếu nhập ngắn hơn thì chương trình sẽ thoát luôn mà không xử lý gì

Tiếp sau đó mình để ý trong danh sách có các hàm:

![alt_text](https://i.imgur.com/RrFShpu.png)

Quay sang tab IDA view(vẫn đang trong hàm ```main.checkPassword```), có đoạn code:

![alt_text](https://i.imgur.com/JKpf785.png)

Lệnh ```xor     ebp, esi``` sẽ xor giá trị của 2 thanh ghi ebp và esi, trong đó mình đoán key bên trên chúng ta thu được (861836f13e3d627dfa375bdb8389214e) nằm trong thanh esi, còn thanh base pointer(ebp) sẽ là giá trị hex nằm trong ngăn xếp (stack) (Vì bên trên mình thấy mấy hàm encode hex)

Mình quyết định đặt breakpoint(f2) ở đây

![alt_text](https://i.imgur.com/bRudzdK.png)

Chuyển sang chế độ xem bằng phím [space], mình thu được địa chỉ của lệnh: 0x80D4B28(Nhớ để dấy x ở sau số 0 đầu tiên)

![alt_text](https://i.imgur.com/LdVIksY.png)

Mình không debug bằng IDA vì nó dễ dính virus :v thay vào đó mình dùng GDB trên linux

(Máy mình có cài thêm cái gef rồi, nhưng không có cũng chả sao)

![alt_text](https://i.imgur.com/4YUUsXw.png)

Sau đó đặt breakpoint bằng lệnh:

![alt_text](https://i.imgur.com/Lb3htjg.png)

chạy chương trình bằng lệnh ```run```

Như đã nói ở trên :V key phải có ít nhất 32 ký tự nên mình nhập đúng 32 cái vào

![alt_text](https://i.imgur.com/zo9v27k.png)

Giờ chương trình đã dừng đúng sau lúc xor 2 thanh ebp và esi

Quay lại 2 hàm hex bên trên, thấy được key của chúng ta sẽ được mã hóa từ 2 chuỗi hex sau đó xor lại với nhau

chuỗi đầu tiên là chuỗi key: 861836f13e3d627dfa375bdb8389214e

chuỗi tiếp theo là chuỗi chúng ta đang tìm

Sau khi đặt breakpoint, mình muốn xem hexdump của thanh esp (stack pointer)

Để ý lệnh ```movzx   esi, [esp+eax+44h+var_20]``` sau lệnh xor.

Mình sẽ xem mã hex trong [esp+20]

![alt_text](https://i.imgur.com/wpvhb7R.png)
