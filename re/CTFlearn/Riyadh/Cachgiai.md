# Riyadh

Another entry level Reversing challenge, if you are new to Reversing you probably want to try my Reyjkavik challenge before attempting this challenge. Good Luck! The flag is hidden inside the Riyadh program. Solve the Challenge, get the flag, and I have included the encrypted sources used to create the challenge in the Riyadh.zip file. If you do to the work of solving the Challenge, I'm providing the Challenge source code (C++ and Python) if you are interested in studying the sources after solving the challenge. I think this is a great way to improve your Reversing skills when learning. Please don't share the sources or flag after you solve the challenge.


Sau khi biết sử dụng GDB, bài này trở nên dễ hơn hẳn, mình không phải phụ thuộc nhiều vào các trình dịch ngược như IDA hay Ghidra nữa.

Trước tiên, mình dùng IDA 64bit mở chương trình, chạy vào hàm ```main```, sau đó đẻ ý lệnh:

![alt_text](https://i.imgur.com/1qljbJA.png)

từ lệnh ```cmp     rax, 1Eh``` mình rút ra được độ dài của flag là 0x1E ký tự (đổi ra hex thì là 30 ký tự)

(Thực ra đến đây là xong việc của IDA rồi, nhưng mình muốn phân tích thêm 1 chút nữa)

Nếu bê nguyên cách giải của [bài trước](https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/CTFlearn/Reykjavik/Cachgiai.md) cho bài này, thì chúng ta phải viết code để XOR từng này mảng:

![alt_text](https://i.imgur.com/b2tFq3A.png)

Mỗi một hàm (bên trái) sẽ tương đương với từng đó lần XOR

![alt_Text](https://i.imgur.com/JtY1AMV.png)

Ngồi tạo mảng để XOR cái đống này thì hết ngày :V

OK! giờ là lúc dùng GDB:

#GDB

![alt_text](https://i.imgur.com/iihNpHe.png)

(Nhớ chạy chương trình bằng lệnh ```run``` trước để nó nạp bộ nhớ)

Sau đó mình xem code assembly của hàm ```main``` bằng lệnh:

![alt_text](https://i.imgur.com/wL1lF4d.png)

Thấy hàm ```strcmp```

![alt_text](https://i.imgur.com/9wopALo.png)

ok giờ đặt breakpoint ở đây:

![alt_text](https://i.imgur.com/F7UQdpo.png)

 Mình thử chạy chương trình luôn (bằng lệnh ```run``` )mà không nhập flag vào 
 
 ![alt_text](https://i.imgur.com/LJshsfB.png)
 
 flag của chúng ta chứa trong thanh ```rsi```, ngoài ra còn thu được 1 flag giả trong ```rdx```
 
 ![alt_text](https://i.imgur.com/Oxa6RJo.png)
 
 (Vì flag của chúng ta thu được bên trên có 30 ký tự, nhưng chuỗi "CTFlearn{Reversing_Is_Easy}" chỉ có 27 ký tự)
 
 Nhưng giờ là lúc các hàm XOR (thu được khi phân tích file bằng IDA) làm việc:
 
 ![alt_text](https://i.imgur.com/l6Y0fuC.png)
 
 Mình để ý khi phân tích hàm ```main``` ra code assembly (lệnh ```disassemble main```), chúng ta có 1 số hạm lạ là: ```_Z4Msg2Pc```, ```_Z4Msg4Pc```,...
 
 Đây chính là các hàm XOR
 
 Giờ mình sẽ chạy lại từ đầu, nhưng là nhập đủ 30 ký tự
 
 ![alt_text](https://i.imgur.com/rDWjRdy.png)
 
Mình tiếp tục cho chương trình chạy bằng lệnh ```ni```

Cứ tiếp tục ```ni``` cho đến khi chương trình chạy đến địa chỉ:

![alt_text](https://i.imgur.com/cmBKzNK.png)

Có thể thấy được sau bước này, input của chúng ta được đẩy xuống ```r13```

![alt_text](https://i.imgur.com/YpnImQK.png)

và flag sau khi được XOR nằm trong ```rdx```

![alt_text](https://i.imgur.com/VNHCO6U.png)

flag: CTFlearn{Masmak_Fortress_1865}
