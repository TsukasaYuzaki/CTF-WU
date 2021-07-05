# Riyadh

Another entry level Reversing challenge, if you are new to Reversing you probably want to try my Reyjkavik challenge before attempting this challenge. Good Luck! The flag is hidden inside the Riyadh program. Solve the Challenge, get the flag, and I have included the encrypted sources used to create the challenge in the Riyadh.zip file. If you do to the work of solving the Challenge, I'm providing the Challenge source code (C++ and Python) if you are interested in studying the sources after solving the challenge. I think this is a great way to improve your Reversing skills when learning. Please don't share the sources or flag after you solve the challenge.


Sau khi biết sử dụng GDB, bài này trở nên dễ hơn hẳn, mình không phải phụ thuộc nhiều vào các trình dịch ngược như IDA hay Ghidra nữa.

Trước tiên, mình dùng IDA 64bit mở chương trình, chạy vào hàm ```main```, sau đó đẻ ý lệnh:

![alt_text](https://i.imgur.com/1qljbJA.png)

từ lệnh ```cmp     rax, 1Eh``` mình rút ra được độ dài của flag là 0x1E ký tự (đổi ra hex thì là 30 ký tự)

(Thực ra đến đây là xong việc của IDA rồi, nhưng mình muốn phân tích thêm 1 chút nữa)

Nếu bê nguyên cách giải của [bài trước](https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/CTFlearn/Reykjavik/Cachgiai.md) cho bài này, thì chúng ta phải viết code để XOR từng này mảng:

![alt_text]((https://i.imgur.com/b2tFq3A.png)

Mỗi một hàm (bên trái) sẽ tương đương với từng đó lần XOR

![alt_Text](https://i.imgur.com/JtY1AMV.png)

Ngồi tạo mảng để XOR cái đống này thì hết ngày :V

OK! giờ là lúc dùng GDB:

#GDB

![alt_text](https://i.imgur.com/iihNpHe.png)

Sau đó mình xem code assembly của hàm ```main``` bằng lệnh:

![alt_text](https://i.imgur.com/wL1lF4d.png)
