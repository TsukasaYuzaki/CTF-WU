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

Vì key chúng ta cần nhập có 32 ký tự, nên chúng ta lấy 2 dòng 1 thử, và trong lần thử thứ 2 bằng 2 dòng:

```4a 53 47 5d 41 45 03 54 5d 02 5a 0a 53 57 45 0d
   05 00 5d 55 54 10 01 0e 41 55 57 4b 45 50 46 01
   ```
Thì cho ra string có nghĩa:

(Cách làm):

Đầu tiên mình chuyển hết 2 chuỗi ra ```bin```:

![alt_text](https://i.imgur.com/ICEfMDe.png)

String đầu tiên ```861836f13e3d627dfa375bdb8389214e``` chuyển sang  ```bin``` là: http://string-functions.com/string-binary.aspx
```python
0011100000110110001100010011100000110011001101100110011000110001001100110110010100110011011001000011011000110010001101110110010001100110011000010011001100110111001101010110001001100100011000100011100000110011001110000011100100110010001100010011010001100101
```
Mã hex tiếp theo ```4a 53 47 5d 41 45 03 54 5d 02 5a 0a 53 57 45 0d 05 00 5d 55 54 10 01 0e 41 55 57 4b 45 50 46 01 ``` chuyển sang ```bin``` là: https://www.binaryhexconverter.com/hex-to-binary-converter

```python
0100101001010011010001110101110101000001010001010000001101010100010111010000001001011010000010100101001101010111010001010000110100000101000000000101110101010101010101000001000000000001000011100100000101010101010101110100101101000101010100000100011000000001
```
Ok! giờ xor 2 cái với nhau: http://xor.pw/#

![alt_text](https://i.imgur.com/4jh28Wk.png)

Có được key là: reverseengineericanbarelyforward

ok giờ chạy chương trình: 

![alt_text](https://i.imgur.com/Nj9atPc.png)

Để ý cái string mà ta thu được ban đầu là mã hash md5, lên mạng convert nó về string thường: https://md5hashing.net/hash

![alt_text](https://i.imgur.com/WI3LqYS.png)

Ok done! 

![alt_text](https://i.imgur.com/P5VrV1v.png)

flag: picoCTF{p1kap1ka_p1c02720c216}

