Bài này khá dễ

Tải về và giải nén thì nhận được 1 QR code

Scan bằng [4qrcode](https://4qrcode.com/scan-qr-code.php) thì được 1 đoạn mã:

![BATA](https://user-images.githubusercontent.com/84331340/147388756-44d37f20-35ca-4ca0-b40f-4c9fd7dc20f3.jpg)

lên decode [base 64](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=ZjBWTVJnRUJBUUFBQUFBQUFBQUFBQUlBQXdBQkFBQUFnSUFFQ0RRQUFBQ01BZ0FBQUFBQUFEUUFJQUFDQUNnQUJnQUZBQUVBQUFBQUFBQUFBSUFFQ0FDQUJBakZBQUFBeFFBQUFBVUFBQUFBRUFBQUFRQUFBTWdBQUFESWtBUUl5SkFFQ0ZjQUFBQlhBQUFBQmdBQUFBQVFBQUFBQUFBQUFBQUFBQUFBQUFDNkNnQUFBTGtVa1FRSXV3RUFBQUM0QkFBQUFNMkFNY0E4QjNRZGk1RGtrQVFJUU9rQUFBQUFWWW5sVUlEeUY0aFZBRmhkNmQvLy8vKzdBQUFBQUxnQkFBQUF6WUFBQUFBNXc2bmh1N1BEdkh0cWJqMDlmU0FnUEZ3NklDQmZYeUFnVURBQVJrVklZU1FuYWdCUnc3TkJPR1REdW5Bd2JUazVjc2U1TURRd1ZqQTFabVl4VEd4ck9Wd3diMDljUXk5Y01EQUFRMVJHYkdWaGNtNTdDZ0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFDQWdBUUlBQUFBQUFNQUFRQUFBQUFBeUpBRUNBQUFBQUFEQUFJQUFRQUFBQUFBQUFBQUFBQUFCQUR4L3dnQUFBRElrQVFJQUFBQUFBQUFBZ0FQQUFBQTVKQUVDQUFBQUFBQUFBSUFGUUFBQU95UUJBZ0FBQUFBQUFBQ0FCMEFBQUFVa1FRSUFBQUFBQUFBQWdBakFBQUFtSUFFQ0FBQUFBQUFBQUVBS0FBQUFLaUFCQWdBQUFBQUFBQUJBRFVBQUFDNWdBUUlBQUFBQUFBQUFRQS9BQUFBZ0lBRUNBQUFBQUFRQUFFQU9nQUFBQitSQkFnQUFBQUFFQUFDQUVZQUFBQWZrUVFJQUFBQUFCQUFBZ0JOQUFBQUlKRUVDQUFBQUFBUUFBSUFBSEZ5TG1GemJRQnlZVzVrYjIwQVpXWnNZV2NBY21GdVpHOXRNZ0J6Wm14aFp3QnNiMjl3QUdKcGRHVmZiMlpmWm14aFp3QmtiMjVsQUY5ZlluTnpYM04wWVhKMEFGOWxaR0YwWVFCZlpXNWtBQUF1YzNsdGRHRmlBQzV6ZEhKMFlXSUFMbk5vYzNSeWRHRmlBQzUwWlhoMEFDNWtZWFJoQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFiQUFBQUFRQUFBQVlBQUFDQWdBUUlnQUFBQUVVQUFBQUFBQUFBQUFBQUFCQUFBQUFBQUFBQUlRQUFBQUVBQUFBREFBQUF5SkFFQ01nQUFBQlhBQUFBQUFBQUFBQUFBQUFFQUFBQUFBQUFBQUVBQUFBQ0FBQUFBQUFBQUFBQUFBQWdBUUFBOEFBQUFBUUFBQUFMQUFBQUJBQUFBQkFBQUFBSkFBQUFBd0FBQUFBQUFBQUFBQUFBRUFJQUFGSUFBQUFBQUFBQUFBQUFBQUVBQUFBQUFBQUFFUUFBQUFNQUFBQUFBQUFBQUFBQUFHSUNBQUFuQUFBQUFBQUFBQUFBQUFBQkFBQUFBQUFBQUE9PQ), nhận được 1 đoạn code binary:

![BATA](https://user-images.githubusercontent.com/84331340/147388802-5e765fdd-595d-4950-a82e-07064eaf5e91.jpg)

Vì là code binary, nên khi chép vào file cũng phải giữ nguyên định dạng

code tạo file: 

```python

import base64

s = "f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAgIAECDQAAACMAgAAAAAAADQAIAACACgABgAFAAEAAAAAAAAAAIAECACABAjFAAAAxQAAAAUAAAAAEAAAAQAAAMgAAADIkAQIyJAE>

ori = base64.b64decode(s)

p = open("File", "wb")
p.write(ori)

```

Chạy xong chúng ta có được 1 file File

Mở file lên: 

![BATA](https://user-images.githubusercontent.com/84331340/147388905-2b72389e-2dc9-476e-a583-9691092fae80.jpg)

Mở bằng GDB, đặt breakpoint ở 1 địa chỉ bất kì thuộc hàm <bite_of_flag>

cứ ```ni``` là ra flag

flag: CTFlearn{QR_v30}
