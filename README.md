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
   
## 关键字
关键字是用来决定Sohii解释器将对解释器周围的字词进行何种操作的关键字。和汇编语言一样，解释器不会理会标识符、数据和关键字之间的区别。

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
