Bài này mình dùng GDB và IDA

bài này khá đặc biệt là nó bắt input các bạn nhập vào phải có CTFlearn{}, nếu không chương trình sẽ báo lỗi

Trước tiên load file bằng IDA 64 bit, vào hàm ```main```, thu được mảng:

```0x57, 0x42, 0x4b, 0x45, 0xcc, 0xbb, 0x81, 0xcc, 0x71, 0x7a, 0x71, 0x66, 0xdf, 0xbb, 0x86, 0xcd, 0x64, 0x6f, 0x6e, 0x5c, 0xf2, 0xad, 0x9a, 0xd8, 0x7e, 0x6f```

Tiếp theo mình để ý chương trình gọi tới 2 hàm là ```encrypt``` và ```shuffle``` sau khi chúng ta nhập input.

![alt_text](https://i.imgur.com/tjO1Pth.png)

# => input của chúng ta sẽ được mã hóa bằng hàm ```encrypt```, sau đó hoán đổi vị trí bằng hàm ```shuffle```, cuối cùng là đem so sánh với 1 cái gì đó, tạm gọi cái đó là zflag.

vậy việc chúng ta cần làm là lấy cái zflag đó, đi ngược lại ```shuffle```, rồi giải mã qua ```encrypt```

# Đầu tiên, mình dùng GDB để tìm cái zflag đó là gì:

Để ý trong hàm main có đoạn ```cmp dl, al```

![alt_text](https://i.imgur.com/RIY50NZ.png)

chuyển view bằng phím space, mình thu được địa chỉ của lệnh đó, có 3 kí tự cuối là: ```A8D```, các kí tự đầu sẽ là các kí tự của hàm ```main``` có thể tìm được qua GDB

ok giờ load file vào GDB, dùng lệnh ```disassemble main```, mình thấy địa chỉ các lệnh thuộc ```main``` sẽ bắt đầu là: ```0x0000555555400```

ok giờ đặt breakpoint ở lệnh ```cmp``` đã nói bên trên

![alt_text](https://i.imgur.com/Il7ectJ.png)

giờ tiến hành chạy chương trình bằng lệnh ```run```, nhập bừa 1 flag (phải bắt đầu bằng CTFlearn{})

Chương trình sẽ dừng ở ```cmp dl, al```, dùng ```info register```, thu được 0x57 trong rax, trùng giá trị đầu tiên ở mảng mình thu được bên trên.
Tiếp tục một hai lần nữa, mình có tất cả các giá trị đều trùng với mảng => zflag chính là mảng chúng ta thu được ban đầu

Đó chính là flag, sau khi đã được ```encrypt``` và ```shuffle```

giờ ta đi ngược lại, lấy mảng này shuffle, rồi giải mã ngược là được flag.

Trước tiên là hàm ```Shuffle``` được viết khá đơn giản

![alt_text](https://i.imgur.com/u0gcmvf.png)

mình viết một đoạn code đơn giản: (đổi hết hex qua dec nha :D)

```C
include <iostream>
using namespace std;

int main(){
        int arr[26] = {87, 66, 75, 69, 204, 187, 129, 204, 113, 122, 113, 102, 223, 187, 134, 2>
        int flag[26];
        int i, j;
        for(i = 0; i<26; i = i + 2){
                flag[i] = arr[i + 1];
        }
        for(j = 1; j < 26; j = j + 2){
                flag[j] = arr[j - 1];
        }
        for(i = 0; i<26; i++){
                cout << flag[i] << ", ";
        }
        return 0;
}
```

chạy chương trình, được 
```66, 87, 69, 75, 187, 204, 204, 129, 122, 113, 102, 113, 187, 223, 205, 134, 111, 100, 92, 110, 173, 242, 216, 154, 111, 126```

đó chính là flag sau khi qua hàm ```encrypt```

ok giờ xem hàm ```encrypt```

![alt_text](https://i.imgur.com/7Z40Ksf.png)

chỉ là mã hóa bằng 1 lệnh XOR đơn giản

Code giải mã: 

```python
flagde = [66, 87, 69, 75, 187, 204, 204, 129, 122, 113, 102, 113, 187, 223, 205, 134, 111, 100,>

v5 = [1, 3, 3, 7 ,222, 173, 190, 239]

for i in range(26):
        print(chr(flagde[i] ^ v5[i % 8]), end = '')

```

Chạy là ra flag

flag: CTFLearn{reversing_is_fun}
