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

Tiếp sau đó mình để ý trong danh sách có các hàm:

![alt_text](https://i.imgur.com/RrFShpu.png)

Quay sang tab IDA view(vẫn đang trong hàm ```main.checkPassword```), có đoạn code:

![alt_text](https://i.imgur.com/JKpf785.png)

Lệnh ```xor     ebp, esi``` sẽ xor giá trị của 2 thanh ghi ebp và esi, trong đó mình đoán key bên trên chúng ta thu được (861836f13e3d627dfa375bdb8389214e) nằm trong thanh esi, còn thanh base pointer(ebp) sẽ là giá trị hex nằm trong ngăn xếp (stack) (Vì bên trên mình thấy mấy hàm encode hex)

Mình quyết định đặt breakpoint(f2) ở đây

![alt_text](https://i.imgur.com/bRudzdK.png)

Chuyển sang chế độ xem bằng phím [space], mình thu được địa chỉ của lệnh:

![alt_text](https://i.imgur.com/LdVIksY.png)

Mình không debug bằng IDA vì nó dễ dính virus :v thay vào đó mình dùng GDB trên linux

(Máy mình có cài thêm cái gef rồi, nhưng không có cũng chả sao)

![alt_text](https://i.imgur.com/4YUUsXw.png)

