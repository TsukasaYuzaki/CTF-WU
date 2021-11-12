Tên bài là beginner....

Mở file bằng IDA thì thấy nó được viết khá đơn giản, ít function, và nhìn được ngay thấy hàm main.

Vào hàm main, ta thấy rõ flag có 15 kí tự, được nhập vào từ bàn phím.

![alt_text](https://i.imgur.com/GjXPJBC.png)

xmm0 sẽ là thanh ghi giữ flag mà chúng ta nhập vào, nhưng bài này hay ở chỗ nó so sánh flag chúng ta nhập với chính nó, sau khi đã qua 3 hàm là pshufb, paddd và pxor, nếu sau khi qua 3 hàm này mà flag trở lại như cũ, thì chúng ta thành công.

Giờ đi vào vùng nhớ của 3 hàm này: 

![alt_text](https://i.imgur.com/TV8jPsq.png)

Shuffle sẽ làm nhiệm vụ xáo trộn, add32 là cộng theo mod 2^32, còn XOR là thuật toán XOR thông thường

Giờ giải thích về add32:

