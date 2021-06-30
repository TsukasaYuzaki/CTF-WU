Can you crack my pin?

https://mega.nz/#!PXYjCKCY!F2gcs83XD6RxjOR-FNWGQZpyvUFvDbuT-PTnqRhBPGQ

![alt_text](https://i.imgur.com/KgmtRbz.png)

Mở bằng IDA 64 bit, chạy vào hàm ```main```:

Trong hàm ```main``` có gọi tới 4 hàm khác là ```printf```, ```scanf``` , ```puts``` và 1 hàm lạ là ```cek```

![alt_text](https://i.imgur.com/VWq7890.png)

Tìm vào hàm ```cek```:

![alt_text](https://i.imgur.com/6sl5Q1K.png)

Để ý lệnh ```mov     eax, cs:valid```

Đi vào vùng nhớ của biến ```valid```:

![alt_text](https://i.imgur.com/QJ38wLE.png)

Chúng ta thu được 1 key là: ```51615h``` (chữ h biểu thị của hex)

Thường chúng ta sẽ làm việc vối hệ cơ số 10, nên chúng ta cần convert nó từ ```hex``` sang ```dec```: https://www.rapidtables.com/convert/number/hex-to-decimal.html

![alt_text](https://i.imgur.com/IJXcuyy.png)

Được số: 333333, và đó cũng chính là flag.

flag: CTFlearn{333333}
