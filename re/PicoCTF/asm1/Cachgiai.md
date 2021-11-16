![alt_text](https://i.imgur.com/ot0WnBe.png)


Input là nhập 0x6fa, đây được coi luôn là ```esp```

Trước tiên là <+3>```cmp``` input của chúng ta trong stack với 0x3a2, thì đương nhiên 0x6fa phải lớn hơn 0x3a2, vậy nên chúng ta sẽ nhảy đến <+37>

ở <+37> sẽ cmp input với 0x6fa, 2 cái bằng nhau nên không thực hiên bước nhảy <+44>, do đó đi tiếp

<+46> chuyển input trong stack vào ```eax```, rồi trừ eax cho 0x12 (vì là pointer nên cũng có nghĩa trừ luôn input trong stack, nên giờ input trong stack chứa 0x6fa - 0x12 = 0x6e8)

rồi nhảy đến <+60> rồi pop, do đó esp cuối cùng sẽ chứa giá trị 0x6e8

flag: 0x6e8
