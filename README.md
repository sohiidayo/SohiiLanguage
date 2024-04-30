# Sohii Language 
基于解释器模式和汇编原理设计的解释器语法   
用于python桌面程序的控制台   
用于python程序的动态运行逻辑   
~~好玩~~   
....
```

Sohii Language 0.0.1
-->print hello,world
hello,world
-->

```

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
运行关键字语法时，程序运行位置始终是关键字的位置，运行结束后，跳转到下一个指令的开头。下文的" +"均为空格      
### log

单字词指令。     
在控制台输出下一个指令的运行详细步骤，如果是无需返回信息的指令延续到下一指令。      

### logging and stoplog

均为单字词指令      
使用logging后接下来运行的步骤均会在控制台输出详细步骤，直到运行到stoplog关键字。      

### stop 

单字词指令。      
解释器执行stop指令时立刻结束，并且不会返回任何值。      
在输入指令末尾不为stop时，解释器自动在后位添加stop。       

### delay
```python
a = "delay 0.5"   
run(a)
```
双字词指令 
用于阻塞进程的延时 
### print
```python
a = "print hello,world"   
run(a)
```
双字词指令      
用于打印字符串      

### do
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

### thread start wait
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

### index 
index     
控制台输出当前指令运行位置，无论有没有log的影响都会输出运行的位置。      

#### point goto jump
```python
#goto无限循环语句
a = "point A print 1 print 2 print 3 goto A"
run(a)
```
```python
# print 10 指令不会被运行
a = "goto A print 10 point A print 20"
run(a)
```
```python
#jump无限循环 print 123 只会运行一次
a = "print 123 print 234 print 456 jump 2"
run(a)
```
1 point 为双字词指令。将下一关键字的字词索引设计为标记点： point 标记符号          
**注意：point指令在解释器运行前就已经开始起到作用了，可看上面的第二个示例代码。如果中途动态修改过指令，则需要再次使用point指令才能正确的进行工作**      
2 goto 为无条件跳转双字词指令。配合point注册的标识符使用，无条件跳转到标识符所代表的指令位置。      
3 jump 为无条件跳转双字词指令。能立即修改程序运行的字词位置。      
**注意：jump跳转很不稳定，尤其在动态修改指令和 index log 等调试用指令的影响下位置常常发生偏移**      

### modify
```python
#执行一遍print 1后执行的是print 2
a = "point A print 1 modify 3 2 goto A"
run(a)
```
```python
#修改goto A 为go to B 来跳过循环
a = "point A print 1 modify 8 B goto A point B print 2"
run(a)
```
modify 为三字词指令，用于运行时修改运行的指令 modify + 需要修改字词索引 + 修改的字符串      

### object obj_set obj_print
```python
#定义对象A后，给A赋值字符串9999，最后输出A
a = "logging object A obj_set A 9999 obj_print A"
run(a)
```
这里的对象是**任意类型**的数据。      
在指令中定义python的对象，设定对象的值，打印对象。            
1 object 双字词指令，使用用户标识符来新建一个对象。默认值为object关键字的字词索引(**整形**)。      
2 obj_set 三字词指令，使用**字符串**赋予用户标识符标识所指对象的值 obj_set A OIiaioooooiai。      
3 obj_print 双字词指令，如同在python中print一样输出这个对象。      

### run run_run run_with
```python
#使用空格替换子句中的$字符，得到一条新的句子。并且运行这条句子。
#pythoy_thread是在全局定义的函数名。
a = "run $ thread$pythoy_thread$thread$pythoy_thread$thread$pythoy_thread$start$wait$"
run(a)
```
```python
#使用run_run 获取子句return回来的对象。
a = "object B run_run $ object$A$obj_set$A$9999$return$A B obj_print B"
run(a)
```

```python
#使用"1"替换子句中的*，使用"return"替换子句的&，使用空格替换子句中的$。
a = "logging object obj run_with $ ( * 1 & return ) logging$object$obj$obj_set$obj$*$&$obj obj print obj"
run(a)
```

run 为三字词指令。作用是运行一条新的句子。      
子句只占用一个字词，却包含多个指令。父句执行run指令时，将子句中分隔符(一般是$)替换为空格，生成一条新的句子，用新的句子进行运算。使用分隔符的原因是增加句子的层次结构。            
run + 空格分割符 + 子句      

run_run 为四字词指令。和run不一样的是，可以接收返回的对象。    
run_run + 空格分割符 + 子句 + 接收对象的指示符   

run_with为run_run的升级版本。不定字词指令。
括号内包含替换规则，作用是在子句解压前执行一系列的替换规则。括号内参数个数均为偶数。索引为偶数的为替换标识符，下一位为替换后的字符串。
run_with + 分割符号 + ( 替代符号1 替代用文字1 替代符号2 替代用文字1 ... ...) + 子句 + 接收对象的指示符

### run_do
运行python全局定义函数的指令。      
```python
#random_integer是在全局定义的函数名,作用是接受整形or浮点型or字符串型的数值，生成两者之间的整数字符串。      
#生成0-10之间的数字并且打印出来。
a = " object obj0 object obj1 object obj2 "
b = " obj_set obj0 0 obj_set obj1 10 "
c = " run_do random_integer ( obj0 obj1 ) obj2 obj_print obj2"
run(a+b+c)
```       
run_do是多字词指令，能将object定义的对象和python中定义的函数交互。      
run_do + 全局定义函数名称 + ( + 参数对象1 + 参数对象2 + ... + ) + 用于接收结果的对象      

### return 
用于句子的返回值，使用ruturn 后立刻终止运行。如果没有父句子，则在python中运行的run函数返回对象。如果是子句，则将覆盖掉run_run和run_with接收对象位指示的对象。      
return + 返回的对象     

### if
```python    
a = " object obj0 object obj1 obj_set obj0 0 obj_set obj1 1  "
b = " if obj0 obj1 A B C print 4 goto D "
c = " point A print 1 goto D "
d = " point B print 2 goto D "
e = " point C print 3 goto D
f = " point D return obj0
run(a+b+c+d+e+f)
```     
分支语句      
对比时obj1和obj2均会被转化为整形      
不支持直接输入数字进行比较      
支持object obj object obj1 if obj obj1 A B C。不支持object obj if obj 0 A B       
如果obj1大于obj2 则跳转到A      
如果obj2大于obj1 则跳转到B      
如果相等 跳转至C      
不可比 or 转化失败 直接执行下一语句      
if + 比较对象1 + 比较对象2 对象1大时跳转点 对象2大时跳转点 对象相对跳转点      

## 样例

### 随机生成0-10之间的数字，直到生成10，累计生成的数。重复100次，求平均值。    
```python
a = " logging"
# obj0 随机最小数 obj1 随机最大数 obj2 计算值 obj3 次数 obj4 累计 
b = " object _ object obj0 object obj1 object obj2 object obj3 object obj4"
c = " obj_set obj0 0 obj_set obj1 10 obj_set obj2 0 obj_set obj3 0 obj_set obj4 0"
d = " point Main run_do s_random_integer ( obj0 obj1 ) obj2 run_do s_add ( obj4 obj2 ) obj4 if obj2 obj1 A B C"
e = " point A point B goto Main"
f = " point C return obj4"
com = (b+c+d+e+f).replace(" ","$")
# obj0 当前计算次数 obj1 最多计算次数 obj2 累积计算值 obj3 当前计算值 obj4 1 obj5 计算平均值
b = " object _ object obj0 object obj1 object obj2 object obj3 object obj4 object obj5"
c = " obj_set obj0 0 obj_set obj1 100 obj_set obj2 0 obj_set obj3 0 obj_set obj4 1 obj_set obj5 0"
d = f" point Main run_run $ {com} obj3 run_do s_add ( obj4 obj0 ) obj0 run_do s_add ( obj2 obj3 ) obj2 if obj0 obj1 A B C"
e = " point A point B goto Main"
f = " point C obj_print obj3 obj_print obj0 run_do s_div_float ( obj3 obj1  ) obj5 return obj5"
f = " point C run_do s_div_float ( obj3 obj1  ) obj5 return obj5"
a = a+b+c+d+e+f
run(a)
```
#### Sohii
```
logging object _ object obj0 object obj1 object obj2 object obj3 object obj4 object obj5 obj_set obj0 0 obj_set obj1 100 obj_set obj2 0 obj_set obj3 0 obj_set obj4 1 obj_set obj5 0 point Main run_run $ $object$_$object$obj0$object$obj1$object$obj2$object$obj3$object$obj4$obj_set$obj0$0$obj_set$obj1$10$obj_set$obj2$0$obj_set$obj3$0$obj_set$obj4$0$point$Main$run_do$s_random_integer$($obj0$obj1$)$obj2$run_do$s_add$($obj4$obj2$)$obj4$if$obj2$obj1$A$B$C$point$A$point$B$goto$Main$point$C$return$obj4 obj3 run_do s_add ( obj4 obj0 ) obj0 run_do s_add ( obj2 obj3 ) obj2 if obj0 obj1 A B C point A point B goto Main point C run_do s_div_float ( obj3 obj1  ) obj5 return obj5
```

### 随机延时
随机生成0-10之间的数，如果数字是10，则退出程序，如果是其他数，则延时这么多秒的时间，循环整个过程。       
```python
a = " logging"
b = " object _ object obj0 object obj1 object obj2 object obj3 object obj4 obj_set obj0 0 obj_set obj1 10 obj_set obj3 0 obj_set obj4 1"
c = " point A print ------- run_do s_random_integer ( obj0 obj1 ) obj2 print 随机数生成器[0-10]生成了 obj_print obj2 run_do s_add ( obj3 obj4 ) obj3"
d = " if obj1 obj2 B B C"
f = " point B print 生成数字不等于10 print 延时这么多秒哦喵 run_do s_delay ( obj2 ) _ goto A"
g = " point C if obj3 obj4 D D F point D print 生成数字等于10,你重试了 obj_print obj3 print 次 print ------- goto G" 
h = " point F print 幸运的你只用了一次！！！ goto H"
i = " point G print 希望你下次次数更少哦 point H return obj3"
a = b+c+d+f+g+h+i
run(a)
```
#### Sohii
```
object _ object obj0 object obj1 object obj2 object obj3 object obj4 obj_set obj0 0 obj_set obj1 10 obj_set obj3 0 obj_set obj4 1 point A print ------- run_do s_random_integer ( obj0 obj1 ) obj2 print 随机数生成器[0-10]生成了 obj_print obj2 run_do s_add ( obj3 obj4 ) obj3 if obj1 obj2 B B C point B print 生成数字不等于10 print 延时这么多秒哦
喵 run_do s_delay ( obj2 ) _ goto A point C if obj3 obj4 D D F point D print 生成数字等于10,你重试了 obj_print obj3 print 次 print ------- goto G point F print 幸运的你只用了一次！！！ goto H point G print 希望你下次次数更少哦 point H return obj3
```

