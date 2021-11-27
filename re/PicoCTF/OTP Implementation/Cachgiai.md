# OTP Implementation

## Description
Yay reversing! Relevant files: [otp](https://jupiter.challenges.picoctf.org/static/929a56f71d3918fc903c68b3ea4a76da/otp) [flag.txt](https://jupiter.challenges.picoctf.org/static/929a56f71d3918fc903c68b3ea4a76da/flag.txt)

Bài này cần chú ý 3 hàm là main, valid_char và jumble

![alt_text](https://i.imgur.com/FhkR3wN.png)

Mở file bằng IDA, vào hàm ```main```

Input của chúng ta cần nhập phải có 0x64 (=100) kí tự

![alt_text](https://i.imgur.com/ghQY63z.png)

Sau đó hàm valid_char sẽ kiểm tra các kí tự hợp lệ trong input:

![alt_text](https://i.imgur.com/MriMtnj.png)

Nghĩa là tất cả các kí tự trong input chỉ được nằm trong khoảng ASCII từ 48 đến 57 hoặc từ 97 đến 102, nghĩa là chỉ có 0123456789 và abcdef

Sau khi chúng ta nhập input thì sẽ qua hàm jumble

![alt_text](https://i.imgur.com/3Jp8xav.png)

Sau đó sẽ đem input mới có được sau hàm jumble để đem so sánh với chuỗi: "lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl"

![alt_text](https://i.imgur.com/3s5g7f1.png)

Nếu đúng thì ta chỉ cần XOR input đó với file [flag.txt](https://jupiter.challenges.picoctf.org/static/929a56f71d3918fc903c68b3ea4a76da/flag.txt) để có được flag.

Vậy việc chúng ta cần làm là lấy chuỗi "lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl" đi ngược lại hàm jumble.

Nhưng có vẻ hơi khó vì trong hàm jumble có chia dư nên dò các kí tự sẽ lâu hơn.

Vì thế mình làm theo cách khác, để ý hàm jumpble chỉ mã hóa từng kí tự riêng biệt, nên dù nhập input thế nào thì sau cùng các kí tự trong input đó đều bị mã hóa như nhau,
khá giống bài [easy as GDB](https://github.com/TsukasaYuzaki/CTF-WU/blob/main/re/PicoCTF/easy%20as%20GDB/Cachgiai.md)
