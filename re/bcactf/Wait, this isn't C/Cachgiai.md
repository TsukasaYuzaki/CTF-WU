This just looks like a binary...

Lets try to decompile it...

Wait, this isn't C...

Hint 1 of 2
What is the original language, maybe look into that language?

Hint 2 of 2
What do arrays start at? ;)

Đầu tiên mình dùng lệnh ```file (Tên chương trình)``` trong linux để xem đây là file gì.

```flag_checker_1: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=44db315a94752488b3ace72816fef8393c9db3fd, for GNU/Linux 3.2.0, not stripped```

Dùng IDA 64bit mở file

Thấy có đến 2 hàm ```main```:

![alt_text](https://i.imgur.com/8TRsRjC.png)

<br/>Hàm ```main``` chính chỉ làm nhiệm vụ là gọi 3 hàm:

```python
call    __gfortran_set_args
call    __gfortran_set_options
call    MAIN__
```
Đọc code của 2 hàm ```__gfortran_set_args``` ```__gfortran_set_options``` thì thấy nó chỉ trả về chính giá trị được truyền vào => Vứt :D

Vào hàm ```MAIN_```, thì thấy 1 loạt các lệnh ```mov```

Mình bắt đầu Decompile ở đoạn này, thu được mảng: <br/>

```ruby
__int64 MAIN__()
{
  int v1; // [rsp+0h] [rbp-2B0h] BYREF
  int v2; // [rsp+4h] [rbp-2ACh]
  const char *v3; // [rsp+8h] [rbp-2A8h]
  int v4; // [rsp+10h] [rbp-2A0h]
  __int16 v5[32]; // [rsp+210h] [rbp-A0h]
  char v6[32]; // [rsp+250h] [rbp-60h] BYREF
  __int16 v7[31]; // [rsp+270h] [rbp-40h]
  __int16 i; // [rsp+2AEh] [rbp-2h]

  v7[0] = 99;
  v7[1] = 101;
  v7[2] = 100;
  v7[3] = 103;
  v7[4] = 121;
  v7[5] = 108;
  v7[6] = 130;
  v7[7] = 110;
  v7[8] = 57;
  v7[9] = 124;
  v7[10] = 127;
  v7[11] = 126;
  v7[12] = 65;
  v7[13] = 92;
  v7[14] = 110;
  v7[15] = 121;
  v7[16] = 70;
  v7[17] = 113;
  v7[18] = 118;
  v7[19] = 68;
  v7[20] = 132;
  v7[21] = 101;
  v7[22] = 71;
  v7[23] = 132;
  v7[24] = 150;
  v3 = "flag_checker_1.f90";
  v4 = 33;
  v1 = 128;
  v2 = 6;
  _gfortran_st_write(&v1);
  _gfortran_transfer_character_write(&v1, "Please enter a flag: Sorry, flag does not match.", 21LL);
  _gfortran_st_write_done(&v1);
  v3 = "flag_checker_1.f90";
  v4 = 34;
  v1 = 128;
  v2 = 5;
  _gfortran_st_read(&v1);
  _gfortran_transfer_character(&v1, v6, 25LL);
  _gfortran_st_read_done(&v1);
  for ( i = 1; i <= 25; ++i )
    v5[i - 1] = *((unsigned __int8 *)&v5[31] + i + 1);
  for ( i = 1; i <= 25; ++i )
  {
    v5[i - 1] += i;
    if ( v5[i - 1] != v7[i - 1] )
    {
      v3 = "flag_checker_1.f90";
      v4 = 43;
      v1 = 128;
      v2 = 6;
      _gfortran_st_write(&v1);
      _gfortran_transfer_character_write(&v1, "Sorry, flag does not match.", 27LL);
      _gfortran_st_write_done(&v1);
      _gfortran_exit_i4(&unk_2054);
    }
  }
  v3 = "flag_checker_1.f90";
  v4 = 48;
  v1 = 128;
  v2 = 6;
  _gfortran_st_write(&v1);
  _gfortran_transfer_character_write(&v1, "Congrats, that was the flag!", 28LL);
  return _gfortran_st_write_done(&v1);
}
```
Khá giống bài trước (https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/bcactf/Storytime:%20The%20Tragic%20Interlude/Cachgiai.md) nhưng lần này tác giả cho thêm 1 đống lệnh lung tung vào, và còn cái ```v3``` với thay đổi giá trị các biến ```v4``` và ```v2```.

Sau đó mình để ý đoạn
```C
  for ( i = 1; i <= 25; ++i )
    v5[i - 1] = *((unsigned __int8 *)&v5[31] + i + 1);
```

Rõ ràng Flag được mã hóa từ mảng ```v7```, nhưng vấn đề là tác giả không gán giá trị gì cho ```v5```, nhưng lại có đoạn code ```v5[i - 1] = *((unsigned __int8 *)&v5[31] + i + 1);```, (mảng ```v5``` mới chỉ được định nghĩa chứ chưa được gán giá trị)<br/>
Đọc đoạn code trên thấy rõ flag chúng ta nhập vào được lưu trong mảng ```v5```, và lệnh ``` if ( v5[i - 1] != v7[i - 1] )``` so sánh ```strings``` nhập vào (sau đó chuyển sang ```dec``` (decimal)) rồi so sánh với ```v7```<br/>

Để ý ```v5[i - 1] += i;``` trước lệnh so sánh với mảng ```v7``` => flag của ta sẽ là các phần tử của ```v7 - i```


Code C++:

```C
#include <iostream>

using namespace std;

int main(){
    char v7[30];
  v7[0] = 99;
  v7[1] = 101;
  v7[2] = 100;
  v7[3] = 103;
  v7[4] = 121;
  v7[5] = 108;
  v7[6] = 130;
  v7[7] = 110;
  v7[8] = 57;
  v7[9] = 124;
  v7[10] = 127;
  v7[11] = 126;
  v7[12] = 65;
  v7[13] = 92;
  v7[14] = 110;
  v7[15] = 121;
  v7[16] = 70;
  v7[17] = 113;
  v7[18] = 118;
  v7[19] = 68;
  v7[20] = 132;
  v7[21] = 101;
  v7[22] = 71;
  v7[23] = 132;
  v7[24] = 150;
  int i, k = 1;;
     for (i = 0; i<25; i++){
        v7[i] = ((int)v7[i] - k);
        k++;
        cout << v7[i] << "";
     }
    return 0;
}
```
(Ở đây mình để mảng v7 kiểu ```char``` để nó tự convert từ ```dec``` sang ```string``` luôn :D)
Chạy chương trình, ta được:

![alt_text](https://i.imgur.com/x5UXxBz.png)

flag: bcactf{f0rtr4N_i5_c0oO0l}
