Hint 1 of 2
Is it possible to modify the variable storing your points?

Hint 2 of 2
What does a program like GameConqueror or CheatEngine do?

Bài này mình tìm được 2 cách giải :D

Cách 1 là mình dùng IDA.
Dùng ```file (Tên chương trình)``` trên linux, ta được: <br/>
```Game.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows```

Mở bằng IDa 32bit (lưu ý mở bằng Microsoft.NET assembly nha, vì sao thì các bạn nhìn dòng trên ấy :D)

![alt text](https://i.imgur.com/nrhDQJc.png)

Ở trong hàm ```AFunGame.Game__Main```, trong IDA-View, kéo xuống dưới tìm được biến: ```aSr3tte10001Epy```

Vào vùng chứa của biến đó, ta được:  <br/>

![alt text](https://i.imgur.com/1X0spIO.png)

Có vẻ như tác giả lười mã hóa flag nên chỉ để flag dưới dạng bị đảo ngược, copy 2 dòng ```text``` mà ta tìm được, nối lại với nhau, rồi sau đó đảo ngược chuỗi lại là ra key!

https://codebeautify.org/reverse-string

![alt text](https://i.imgur.com/DEZiI2v.png)

key: bcactf{h0p3fu1ly_y0U_d1dNt_actUa1ly_tYpe_1000_1ett3rs}
