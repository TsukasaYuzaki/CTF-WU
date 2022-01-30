Vì lý do nào đó mà máy mình nó hiện file này có Trojan...

Load file vào IDA, thì mình thấy entry point của file này không phải hàm main()

![s](https://user-images.githubusercontent.com/84331340/151705865-fbda7825-1ffa-4e2e-8b5f-1b7ac3621b0c.jpg)

Bởi rõ ràng khi chạy thì file sẽ in ra box Hi <3 đầu tiên :D

![s](https://user-images.githubusercontent.com/84331340/151705908-7bc2fefb-92ca-427e-9288-7c454d3f36ad.jpg)

Bài yêu cầu chúng ta nhập tên và 1 số nào đó, nếu số đó đúng thì sẽ có flag

Thường thì mấy bài kiểu này mình debug rồi đặt breakpoint vào chỗ ```cmp``` là được flag ngay, nhưng bài này hơi khác chút

Trong môi trường Debug thì file này có thêm 2 box mà khi chạy thường không có

![s](https://user-images.githubusercontent.com/84331340/151706086-2d97e512-7abd-48bf-b77b-fc177fa3bf6f.jpg)

![s](https://user-images.githubusercontent.com/84331340/151706200-81bef6b1-d97d-44b9-89d9-933cf12a8085.jpg)

Ok giờ xem lại code thì mình thấy 1 thanh ghi lạ 

![s](https://user-images.githubusercontent.com/84331340/151706237-b84c9e8d-a08d-462b-b5b2-6bb3a437b90d.jpg)

Search mới biết đây là thanh ghi [chống debug](https://stackoverflow.com/questions/14496730/mov-eax-large-fs30h)

(chả biết gọi đây là thanh ghi có đúng không =.=)

Nói chúng là chạy khi debug thì nó set bit cho [edi+2] (còn edi đang trỏ tới cái gì thì không cần biết!)

![s](https://user-images.githubusercontent.com/84331340/151706310-2fa31ac0-958c-48dd-b7e2-7089b6a04f3f.jpg)

![Uploading s.jpg…]()



