Bài này có vẻ khá dễ, nhiệm vụ của chúng ta là nhập vào 2 số mà tổng của chúng bằng 20 và tính của chúng bằng 100

![BATA](https://user-images.githubusercontent.com/84331340/147116616-73ed00f6-975f-4828-ada3-41f89f0da2fc.jpg)

=> chỉ có một cặp số là 10, 10 là thỏa mãn

![BATA](https://user-images.githubusercontent.com/84331340/147116908-235c126d-f9e1-4495-82af-b1531d1832f6.jpg)

![BATA](https://user-images.githubusercontent.com/84331340/147117005-cbcee133-d59b-4221-ba79-fab1bd9577c9.jpg)

(edx giữ tổng và eax giữ tích)

Nhưng nếu nhập 10 10 thì chúng ta vấp phải 1 hàm check

![BATA](https://user-images.githubusercontent.com/84331340/147117203-55069a66-4d8d-4198-812d-ba84040d2cd9.jpg)

Để ý trong chương trình có hàm GetArgs

Mình tạo 1 patch, thay đổi lệnh check trong hàm này để giúp mình nhập được 2 ký tự trở lên

Trước khi chuyển: 
![BATA](https://user-images.githubusercontent.com/84331340/147117744-d2416d83-1835-4a07-97b6-02c8bd73020e.jpg)


Sau khi chuyển:
![BATA](https://user-images.githubusercontent.com/84331340/147117898-087cbe65-2585-46ae-996a-c48de7f7c2ef.jpg)


Vá xong là ok:

![BATA](https://user-images.githubusercontent.com/84331340/147118021-138b6f49-0d21-4049-9849-885a8f52fec7.jpg)

Flag: CTFlearn{+123R10..de..JaneiR0}
