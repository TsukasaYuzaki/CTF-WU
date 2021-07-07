there's crypto in here but the challenge is not crypto... 🤔

Mọi chuyện trở nên thật ez khi sử dụng GDB

bài này mình chỉ dùng tới 2 công cụ là GDB và IDA

Đầu tiên, bằng lệnh ```file [ten chuong trình]```, mình phát hiện loại file để dùng bản IDA phù hợp

![alt_text](https://i.imgur.com/1YoirB0.png)

Giờ mình sẽ mở file bằng IDA 64 bit, vào hàm ```main``` mở hàm ```main``` thì thực sự ngáo luôn

![alt_text](https://i.imgur.com/zHnLir3.png)

Nếu làm như các bài trước thì mình phải tạo mảng để XOR một đống giá trị ```hex``` tìm được, như vậy thì rất lâu mà còn chưa chắc đã chính xác, vì mình để ý trong bài này có rất hiện hàm gán và lệnh XOR

Giờ mình để ý hàm:

![alt_text](https://i.imgur.com/WmZ1pgE.png)

# Từ đây thấy được flag sẽ có 0x40 ký tự (chuyển ra thì là 64 ký tự)

Xong việc của IDA

# GDB

Trước tiên, mình chạy chương trình để gdb nạp bộ nhớ (bước này cần thiết đấy)

nhập đúng 64 ký tự nhé, vì có vẻ như nếu nhập ít hơn thì chương trình sẽ không thoát mà tiếp tục chạy

![alt_text](https://i.imgur.com/4FSoOV6.png)

Tuy nhiên mình không tìm được hàm ```main```

# mấu chốt ở đây là tìm các hàm ```cmp```(compare), sau đó đặt breakpoint ở đó

Sau đó mình dùng lệnh ```info functions``` để xem tất cả các hàm

Lag máy luôn, bài này sử dụng quá nhiều hàm, có vẻ như là đẻ tránh dịch ngược.

nhưng sau đó may mắn là mình cũng tìm được ```memcmp``` ở địa chỉ 0x0000555555555060

ok đặt breakpoint ở đây là xong hết rồi

![alt_text](https://i.imgur.com/FzUAxKe.png)

chạy chương trình bằng lệnh ```run```, sau đó nhập đủ 64 ký tự vào, và sau đó lấy flag đang được cất trong ```rdi```!

![alt_text](https://i.imgur.com/HvFz6C4.png)

flag: picoCTF{c0mp1l3r_0pt1m1z4t10n_15_pur3_w1z4rdry_but_n0_pr0bl3m?}
