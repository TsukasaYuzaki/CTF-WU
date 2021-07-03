# RAmada

This is a beginners Reversing Challenge. It is build with the optimization level set to 0 so that the assembler is more readable. If you are new to reversing, please remember that to solve Reversing challenges you probably need to know some C/C++, Assembler and also some experience with gdb (the gnu debugger). And maybe Ghidra. So this challenge is a great place to start Reversing, but unfortunately it's only 10 points because it's easier than other reversing challenges. It probably requires more skills than solving a 10 point Forensics problem like RubberDuck. If you solve the challenge you can use the flag to decrypt the sources and see how the challenge is created.

Bất đầu từ bài này mình sẽ dùng kết hợp cả IDA và Ghidra (công dụng của 2 cái mình thầy như nhau, nhưng code assembly của IDA viết dễ đọc hơn, còn Ghidra lại có thể đào sâu hơn vào chương trình)

Trước tiên là IDA:

Mở chương trình bằng IDA 64 bit, chạy vào hàm main và decompile, thu được code:

```C++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // er13
  unsigned int v4; // er12
  const char *v5; // rbp
  bool v6; // zf
  int v7; // er12
  size_t v8; // rax
  __int64 v9; // rcx
  char *v10; // rdi
  char v12[104]; // [rsp+0h] [rbp-68h] BYREF

  puts("Welcome to the CTFLearn Ramada Reversing Challenge!");
  v3 = getpid();
  v4 = getppid();
  __printf_chk(1LL, "\tpid : %10d 0x%08x\n", v3, v3);
  __printf_chk(1LL, "\tppid: %10d 0x%08x\n", v4, v4);
  if ( argc == 1 )
  {
    v7 = 1;
    puts("Usage: Ramada CTFlearn{kernel}");
  }
  else
  {
    v5 = argv[1];
    v6 = memcmp("CTFlearn{", v5, 9uLL) == 0;
    v7 = !v6;
    if ( v6 )
    {
      v8 = strlen(v5);
      if ( v5[v8 - 1] == 125 )
      {
        if ( v8 == 31 )
        {
          InitData();
          v9 = 16LL;
          v10 = v12;
          while ( v9 )
          {
            *(_DWORD *)v10 = v7;
            v10 += 4;
            --v9;
          }
          strncpy(v12, v5 + 9, 0x15uLL);
          __printf_chk(1LL, "Your Flag Kernel: %s\n", v12);
          if ( !(unsigned int)CheckFlag(v12) )
            __printf_chk(1LL, "Woot Woot! You found the flag! %s\n", v5);
          puts("All Done Ramada!");
        }
        else
        {
          v7 = 4;
          puts("Your flag is the wrong length dude!");
        }
      }
      else
      {
        v7 = 3;
        puts("Error: Your flag must end with '}'");
      }
    }
    else
    {
      v7 = 2;
      puts("Error: Your flag must start with CTFlearn{");
    }
  }
  return v7;
}
```

Ở đây chương trình yêu cầu chúng ta nhập trực tiếp flag vào để kiểm tra, flag có dạng: CTFlearn{chuỗi cần tìm}

Để ý lệnh code:

```assembly
 v8 = strlen(v5);
      if ( v5[v8 - 1] == 125 )
      {
        if ( v8 == 31 )
        {
```



