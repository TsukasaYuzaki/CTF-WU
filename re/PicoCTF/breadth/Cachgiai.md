Load cả 2 file vào IDA thì thấy cả 2 đều có hơn 16000 function

Hàm main trong 2 hàm chả làm gì ngoài việc in ra 2 dòng chữ

![alt_text](https://i.imgur.com/PiynBLcmp x.png)

=> Không phải nhập flag, mà phải tìm flag được giấu trong chương trình

Trong 16k function thì cái nào cũng trả về 1 flag giả

Trông thì có vẻ giống nhau, nhưng cuối cùng mình cũng tìm được điểm khác nhau bằng lệnh ```cmp``` trên linux

![alt_text](https://i.imgur.com/elPYCNq.png)

dùng thêm tùy chọn ```-l``` 

![alt_text](https://i.imgur.com/oiXhmYd.png)

Thấy số 610380 khá giống 1 địa chỉ, đổi ra hex thì là 0x9504C

Giờ tìm địa chỉ này trong file bằng IDA

![alt_text](https://i.imgur.com/4yxUqhJ.png)

vào function này là được flag

flag: picoCTF{VnDB2LUf1VFJkdfDJtdYtFlMexPxXS6X}
