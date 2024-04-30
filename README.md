# Sohii Language 
基于解释器模式和汇编原理设计的解释器语法   
用于python桌面程序的控制台   
用于python程序的动态运行逻辑     
....

## 语法概念
Sohii语言以句子为程序单位。句子由单个或多个指令构成，指令由单个或多个字词和空格构成。

1. 字词 关键字、自定义的标识符、字符数据  
2. 字词索引 字词在句子中的位置，从0开始
3. 子句 以单字词形式存在的一条句子，使用标识符代替空格进行连接
4. 对象 等同于python中的对象，在句子运行结束后销毁。
5. 全局函数 指的是在python中定义在全局变量中的函数
   
## 关键字
关键字是用来决定Sohii解释器将对解释器周围的字词进行何种操作的关键字。和汇编语言一样，解释器不会理会标识符、数据和关键字之间的区别。指令均以关键字为开头。

关键字
1. log
2. logging
3. stoplog
4. print
5. delay
6. do
7. thread
8. start
9. wait
10. point
11. goto
12. jump
13. index
14. modify
15. object
16. obj_print
17. obj_set
18. run
19. run_run
20. run_do
21. return
22. if
23. unzip
24. (
25. )


    
## 语法   
运行关键字语法时，程序运行位置始终是关键字的位置，运行结束后，跳转到下一个指令的开头。下文的" "均表为空格
#### log

单字词指令。     
在控制台输出下一个指令的运行详细步骤，如果是无需返回信息的指令延续到下一指令。

#### logging and stoplog

均为单字词指令
使用logging后接下来运行的步骤均会在控制台输出详细步骤，直到运行到stoplog关键字。

#### stop 

单字词指令。
解释器执行stop指令时立刻结束，并且不会返回任何值。
在输入指令末尾不为stop时，解释器自动在后位添加stop。

#### delay
```python
a = "delay 0.5"   
run(a)
```
双字词指令 
用于阻塞进程的延时 
#### print
```python
a = "print OIiaioooooiai"   
run(a)
```
双字词指令
用于打印字符串

#### do
```python
a = " do print123"
b = " do python_add ( 1 2 3 )"
c = " do python_add unzip 1,2,3"   
run(a+b+c)
```

三种用法，均不返回结果,输入全局函数的参数均为字符串。

1为双字词指令：do + 全局函数名称，不带参数调用。   
2为不定字词指令：do + 全局函数名称 + ( + 参数0 + 参数1 + ... + ) 。    
3为三字词模式，参数实际为一个字词，使用 "," 连接：do + 全局函数名称 + unzip + 参数1,参数2,,...    

#### thread start wait
```python
a = " thread print123"
b = " thread python_add ( 1 2 3 )"
c = " thread python_add unzip 1,2,3"
d = " start wait "
run(a+b+c+d)
```
thread的三种用法，均不返回结果,输入全局函数的参数均为字符串。    
并且运行thread指令并不会执行函数。而是在执行start后非阻塞运行之前注册过的所有thread函数。
wait是等待所有的thread函数执行完毕后才进行下一指令。

1为双字词指令：thread + 全局函数名称，不带参数调用。   
2为不定字词指令：thread + 全局函数名称 + ( + 参数0 + 参数1 + ... + ) 。    
3为三字词模式，参数实际为一个字词，使用 "," 连接：do + 全局函数名称 + unzip + 参数1,参数2,,... 
4start和wait均为单字词指令。






