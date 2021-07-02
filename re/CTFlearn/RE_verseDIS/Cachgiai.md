# RE_verseDIS 

Could you find the hidden password?

https://mega.nz/#!XOwVmCSC!ut_5r6b32j2kD6EvlvsvJhmm58pbswusUXF08yI93Zo

Mở bằng IDA 64 bit, chạy vào hàm ```main```, mình để ý vùng code:

![alt_text](https://i.imgur.com/bGEpt0h.png)

Chúng ta thu được key là: IdontKnowWhatsGoingOn

tiếp theo đó để ý ```str``` được ```lea``` vào trong rax, và thanh ecx thì đang giữ chuỗi key, và sau đó chúng được XOR lại với nhau.

Thanh ecx chứa key đã biết (```IdontKnowWhatsGoingOn```)

Giờ chỉ cần tìm xem ```str``` chứa gì, say đó XOR với chuỗi key là được.

Vào vùng nhớ của ```str```:

![alt_text](https://i.imgur.com/z4iYBtV.png)

Chúng ta thu hết các giá trị khác 0, sau đó lập thành 1 mảng:

```C
int a[30]  =    { 8, 6, 44, 58, 50,  48,  28, 92, 1, 50,  26, 18,  69,  29, 32,  48, 13,  27, 3, 124, 19, 15};
```

Nhớ đổi các giá trị có kết thúc bằng chữ h (hex) sang ```dec``` (cơ số 10)

OK! giờ chỉ cần XOR các giá trị này với mảng key ở trên là được.

code C++:

```C++
#include <iostream>

using namespace std;

int main(){
    char s[30] = "IdontKnowWhatsGoingOn";
    int a[30]  =    { 8, 6, 44, 58, 50,  48,  28, 92, 1, 50,  26, 18,  69,  29, 32,  48, 13,  27, 3, 124, 19, 15};

    for (int i = 0; i<21; i++)
        cout << (char)((int)s[i] ^ a[i]) << "" ;

    return 0;
}
```

Chạy chương trình, ta được flag: AbCTF{r3vers1ng_dud3}

Các bạn submit AbCTF{r3vers1ng_dud3} hay CTFlearn{r3vers1ng_dud3} đều được
