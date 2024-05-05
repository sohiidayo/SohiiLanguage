import time
import threading
import random

sohii_Language_version_1 = "2"
sohii_Language_version_2 = "0"
sohii_Language_version_3 = "0"
sohii_Language_version = sohii_Language_version_3 + "." + sohii_Language_version_2 + "." + sohii_Language_version_1 

SOHII_FUNCTIONS = {}

#标准函数库
#是Sohii语言标准函数库
def s_add(x, y):  
    try:  
        return str(float(x) + float(y)) 
    except ValueError:  
        try:  
            return str(int(x) + int(y))
        except ValueError:  
            raise ValueError("Both x and y must be convertible to numbers")  
def s_sub(x, y):  
    try:  
        return str(float(x) - float(y))
    except ValueError:  
        try:  
            return str(int(x) - int(y))
        except ValueError:  
            raise ValueError("Both x and y must be convertible to numbers")  
def s_mul(x, y):  
    try:  
        return str(float(x) * float(y))
    except ValueError:  
        try:  
            return str(int(x) * int(y)) 
        except ValueError:  
            raise ValueError("Both x and y must be convertible to numbers")  
def s_div_float(x, y):  
    try:  
        return str(float(x) / float(y))
    except ValueError:  
        raise ValueError("Both x and y must be convertible to floats")  
def s_div_int(x, y):  
    try:  
        return str(int(x) // int(y))
    except ValueError:  
        raise ValueError("Both x and y must be convertible to integers")  
def s_bitwise_and(x, y):  
    try:  
        return str(int(x) & int(y))
    except ValueError:  
        raise ValueError("Both x and y must be convertible to integers")  
def s_bitwise_or(x, y):  
    try:  
        return str(int(x) | int(y))
    except ValueError:  
        raise ValueError("Both x and y must be convertible to integers")  
def s_bitwise_not(x):  
    try:  
        return str(~int(x))
    except ValueError:  
        raise ValueError("x must be convertible to an integer")  
def s_bitwise_nand(x, y):  
    return str(~(int(x) & int(y))) 
def s_bitwise_nor(x, y):  
    return str(~(int(x) | int(y))) 
def s_bitwise_and_or_not(x, y, z):  
    return str(~((int(x) & int(y)) | int(z)))  
def s_bitwise_xor(x, y):  
    try:  
        return str(int(x) ^ int(y))  # 异或  
    except ValueError:  
        raise ValueError("Both x and y must be convertible to integers")  
def s_bitwise_xnor(x, y):  
    return str(~(int(x) ^ int(y))) 
def s_modulo(x, y):  
    try:  
        return str(float(x) % float(y))
    except ValueError:  
        try:  
            return str(int(x) % int(y))
        except ValueError:  
            raise ValueError("Both x and y must be convertible to numbers")
def s_power(x, y):  
    try:  
        return str(float(x) ** float(y))
    except ValueError:  
        try:  
            return str(int(x) ** int(y))
        except ValueError:  
            raise ValueError("Both x and y must be convertible to numbers")
def s_random_integer(min_value, max_value):  
    return str(random.randint(int(min_value), int(max_value)))  
def s_delay(x):
    time.sleep(float(x))

def run(TaskList,split_signal=" "):
    TaskList=TaskList.split(split_signal)
    TaskList = [s for s in TaskList if s]
    if TaskList and TaskList[-1] != "stop": 
        TaskList.append("stop") 
    NoStop = 1
    LogStep = 0
    Logging = 0
    count = len(TaskList)
    TaskIndex = 0
    functionDic=None
    threads = []
    gotoDic = {}
    objectDic = {}
    for n, task in enumerate(TaskList):  
        if task == 'point':  
            if n + 1 < len(TaskList) and n + 2 < len(TaskList):  
                gotoDic[TaskList[n + 1]] = n + 2
    while(NoStop):
        TaskKey=TaskList[TaskIndex]
        if TaskKey == "stop" or TaskKey == "" :
            if(LogStep or Logging):
                print("log:" + TaskKey)
            NoStop = 0
            break
        elif TaskKey == "log":
            LogStep = 1
            TaskIndex += 1
        elif TaskKey == "logging":
            Logging = 1
            TaskIndex += 1

        elif TaskKey == "stoplog":
            Logging = 0
            TaskIndex += 1
        elif TaskKey == "delay":
            if(LogStep or Logging):
                print("log:" + "执行延时->"+" "+TaskList[TaskIndex+1])
                LogStep = 0
            time.sleep(float(TaskList[TaskIndex+1]))
            TaskIndex += 2
        elif TaskKey == "print":
            if(LogStep or Logging):
                print("log:" + TaskKey+" "+TaskList[TaskIndex+1])
                LogStep = 0
            print(TaskList[TaskIndex+1])
            TaskIndex += 2
        elif TaskKey == "copy":

            varCount = TaskIndex + 1
            objectFromList = []
            
            logg = []

            while(1):
                if TaskList[varCount]=="to":
                    break
                else:
                    if(LogStep or Logging):
                        logg.append([TaskList[varCount],objectDic[TaskList[varCount]]])
                    objectFromList.append(TaskList[varCount])
                varCount += 1
            a = 0
            for i in objectFromList:
                if(LogStep or Logging):
                    logg[a].append(TaskList[varCount + a + 1])
                    logg[a].append(objectDic[TaskList[varCount + a +1]])
                objectDic[TaskList[varCount + a +1]] = objectDic[objectFromList[a]]

                a += 1 
            TaskIndex += a + a + 2

            if(LogStep or Logging):
                count = 0
                s = ""
                for i in logg:
                    s += f" copy {i[0]} : {i[1]} to {i[2]} : {i[3]} "
                print("log:使用对象赋值" + s)
                LogStep = 0
        elif TaskKey == "do":
            if(functionDic==None):
                functionDic = globals()
            if(TaskList[TaskIndex+2] == "("):
                varCount = TaskIndex+2
                varList = []
                while(1):
                    if TaskList[varCount+1]==")":
                        break
                    varList.append(TaskList[varCount+1])
                    varCount += 1
                func = functionDic.get(TaskList[TaskIndex+1])
                if(LogStep or Logging):
                    print("log:" +"执行函数->"+TaskList[TaskIndex+1] + str(varList))
                    LogStep = 0
                if callable(func):  
                    func(*varList)
                else:
                    print("error:函数不可用->" + TaskList[TaskIndex+1] )
                TaskIndex += len(varList) + 4
            elif(TaskList[TaskIndex+2] == "unzip"):
                varList =  TaskList[TaskIndex+3].split(",")
                func = functionDic.get(TaskList[TaskIndex+1])
                if(LogStep or Logging):
                    print("log:" +"执行函数->"+TaskList[TaskIndex+1] + str(varList))
                    LogStep = 0
                if callable(func):  
                    func(*varList)
                else:
                    print("error:函数不可用->" + TaskList[TaskIndex+1] )
                TaskIndex += 4
            elif(TaskList[TaskIndex+2] != "(" and TaskList[TaskIndex+1] != "unzip"):
                # 不带参数的情况下
                    if(LogStep or Logging):
                        print("log:" +"执行函数->"+TaskList[TaskIndex+1])
                        LogStep = 0
                    func = functionDic.get(TaskList[TaskIndex+1])
                    if callable(func):  
                        func()
                    else:
                        print("error:函数不可用->" + TaskList[TaskIndex+1] )
                    TaskIndex += 2
        elif TaskKey == "thread":
            if(functionDic==None):
                functionDic = globals()
            if(TaskList[TaskIndex+2] == "("):
                varCount = TaskIndex+2
                varList = []
                while(1):
                    if TaskList[varCount+1]==")":
                        break
                    varList.append(TaskList[varCount+1])
                    varCount += 1
                func = functionDic.get(TaskList[TaskIndex+1])
                if(LogStep or Logging):
                    print("log:" +"多线程执行函数注册->"+TaskList[TaskIndex+1] + str(varList))
                    LogStep = 0
                if callable(func):  
                    thread = threading.Thread(target=func,args= varList)
                    threads.append(thread)
                else:
                    print("error:函数不可用->" + TaskList[TaskIndex+1] )
                TaskIndex += len(varList) + 4
            elif(TaskList[TaskIndex+2] == "unzip"):
                varList =  TaskList[TaskIndex+3].split(",")
                func = functionDic.get(TaskList[TaskIndex+1])
                if(LogStep or Logging):
                    print("log:" +"多线程执行函数注册->"+TaskList[TaskIndex+1] + str(varList))
                    LogStep = 0
                if callable(func):  
                    thread = threading.Thread(target=func,args = varList)
                    threads.append(thread)
                else:
                    print("error:函数不可用->" + TaskList[TaskIndex+1] )
                TaskIndex += 4
            elif(TaskList[TaskIndex+2] != "(" and TaskList[TaskIndex+1] != "unzip"):
                # 不带参数的情况下
                    if(LogStep or Logging):
                        print("log:" +"多线程执行函数注册->"+TaskList[TaskIndex+1])
                        LogStep = 0
                    func = functionDic.get(TaskList[TaskIndex+1])
                    if callable(func):  
                        thread = threading.Thread(target=func)
                        threads.append(thread)
                    else:
                        print("error:函数不可用->" + TaskList[TaskIndex+1] )
                    TaskIndex += 2
        elif TaskKey == "start":
            for thread in threads:
                thread.start()
            TaskIndex += 1
        elif TaskKey == "wait":
            for thread in threads:
                thread.join()
            TaskIndex += 1
        elif TaskKey == "run":
            split_signal = TaskList[TaskIndex+1]
            command = TaskList[TaskIndex+2]
            if(LogStep or Logging):
                print("log:" + "执行指令->"+" "+command.replace(split_signal," ")) # Log秒数
                LogStep = 0
            run(command,split_signal)
            TaskIndex += 3
        elif TaskKey == "point":
            if(LogStep or Logging):
                print("log:" + "注册传送点->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            gotoDic[TaskList[TaskIndex+1]] = TaskIndex
            TaskIndex += 2
        elif TaskKey == "index_add":
            if(LogStep or Logging):
                print("log:" + "当前字词索引 + ->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            TaskIndex += int(TaskList[TaskIndex+1])
        elif TaskKey == "index_add_obj":
            if(LogStep or Logging):
                print("log:" + "当前字词索引 + ->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            TaskIndex += int(objectDic[TaskList[TaskIndex+1]])
        elif TaskKey == "goto":
            if(LogStep or Logging):
                print("log:" + "跳到循环->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            #TaskIndex += 2
            index=gotoDic[TaskList[TaskIndex+1]]
            TaskIndex = index
        elif TaskKey == "index":
            if(LogStep or Logging):
                print("log:" + "显示当前索引->"+" "+str(TaskIndex)) 
                LogStep = 0
            print("索引->"+" "+str(TaskIndex)) 
            TaskIndex += 1
        elif TaskKey == "sohii":
            if(LogStep or Logging):
                print("log:" + "Sohii Language"+" " + sohii_Language_version) 
                LogStep = 0
            print(" sohii_Language_version: "+ sohii_Language_version) 
            TaskIndex += 1
        elif TaskKey == "jump":
            if(LogStep or Logging):
                print("log:" + "跳转到索引->"+" "+str(TaskList[TaskIndex+1])) 
                LogStep = 0
            TaskIndex = int(TaskList[TaskIndex+1])
        elif TaskKey == "object":
            if(LogStep or Logging):
                print("log:" + "注册对象->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            objectDic[TaskList[TaskIndex+1]] = TaskIndex
            TaskIndex += 2
        elif TaskKey == "int" or TaskKey == "str" or TaskKey == "obj" or TaskKey == "float": 
            if(LogStep or Logging):
                print("log:" + "定义变量->"+" "+TaskList[TaskIndex+1] + " 并赋值" + TaskList[TaskIndex+2]) 
                LogStep = 0
            objectDic[TaskList[TaskIndex+1]] = TaskList[TaskIndex+2]
            TaskIndex += 3
        elif TaskKey == "obj_print":
            if(LogStep or Logging):
                print("log:" + "打印对象->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            print(objectDic[TaskList[TaskIndex+1]])            
            TaskIndex += 2
        elif TaskKey == "obj_print":
            if(LogStep or Logging):
                print("log:" + "打印对象->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            print(objectDic[TaskList[TaskIndex+1]])            
            TaskIndex += 2
        elif TaskKey == "input":
            if(LogStep or Logging):
                print("log:" + "等待接收数据->"+" "+TaskList[TaskIndex+1]) 
                LogStep = 0
            objectDic[TaskList[TaskIndex+1]] = input()            
            TaskIndex += 2
        elif TaskKey == "modify":
            if(LogStep or Logging):
                print(f"log:修改指令数据->索引{TaskList[TaskIndex+1]} : {TaskList[int(TaskList[TaskIndex+1])]} to {TaskList[TaskIndex+2]}")
                LogStep = 0
            TaskList[int(TaskList[TaskIndex+1])] = TaskList[TaskIndex+2]
            TaskIndex += 3
        elif TaskKey == "run_do":
            if(functionDic==None):
                functionDic = globals()
            if(TaskList[TaskIndex+2] == "("):
                varCount = TaskIndex+2
                varList = []
                while(1):
                    if TaskList[varCount+1]==")":
                        break
                    varList.append(objectDic[TaskList[varCount+1]])
                    varCount += 1
                func = functionDic.get(TaskList[TaskIndex+1])
                if callable(func):  
                    a = func(*varList)
                    if(LogStep or Logging):
                        print("log:" +"执行函数->"+TaskList[TaskIndex+1] + str(varList) + " 获得返回值:" + str(a) +" to " + TaskList[TaskIndex + len(varList) + 4])
                        LogStep = 0
                    objectDic[TaskList[TaskIndex + len(varList) + 4]] = a
                else:
                    print("error:函数不可用->" + TaskList[TaskIndex+1] )
                TaskIndex += len(varList) + 5
        elif TaskKey == "run_run":
            split_signal = TaskList[TaskIndex+1]
            command = TaskList[TaskIndex+2]
            objectDic[TaskList[TaskIndex+3]] = run(command,split_signal)
            if(LogStep or Logging):
                print("log:" + "执行指令->"+" "+command.replace(split_signal," ") + " 得到结果 " + objectDic[TaskList[TaskIndex+3]] + " to " + TaskList[TaskIndex+3])
                LogStep = 0
            TaskIndex += 4
        elif TaskKey == "obj_set" or TaskKey == "set":
            if(LogStep or Logging):
                print("log:" +"设定立即字符串->"+TaskList[TaskIndex+1] +"为"+ TaskList[TaskIndex+2])
                LogStep = 0
            objectDic[TaskList[TaskIndex+1]] = TaskList[TaskIndex+2]
            TaskIndex += 3
        elif TaskKey == "sohii_v":
            if(LogStep or Logging):
                print("log:" +"设定立即字符串->"+TaskList[TaskIndex+1] +"为"+ sohii_Language_version_1 + f"，{TaskList[TaskIndex+2]} 为 {sohii_Language_version_2}" + f"，{TaskList[TaskIndex+3]} 为 {sohii_Language_version_3}")
                LogStep = 0
            objectDic[TaskList[TaskIndex+1]] = sohii_Language_version_1
            objectDic[TaskList[TaskIndex+2]] = sohii_Language_version_2
            objectDic[TaskList[TaskIndex+3]] = sohii_Language_version_3
            TaskIndex += 4
        elif TaskKey == "return":
            if(LogStep or Logging):
                print("log:" +"返回对象->"+TaskList[TaskIndex+1] +"为"+ objectDic[TaskList[TaskIndex+1]])
                LogStep = 0
            return objectDic[TaskList[TaskIndex+1]]
        elif TaskKey == "run_with":
            if(TaskList[TaskIndex+2] == "("):
                varCount = TaskIndex+2
                varList = []
                while(1):
                    if TaskList[varCount+1]==")":
                        break
                    varList.append(TaskList[varCount+1])
                    varCount += 1
            split_signal = TaskList[TaskIndex+1]
            command = TaskList[len(varList)+7]
            replace_dict = {}  
            for i in range(0, len(varList), 2):  
                replace_dict[varList[i]] = varList[i+1] 
            for key, value in replace_dict.items():  
                command = command.replace(key, value)
            objectDic[TaskList[len(varList)+8]] = run(command,split_signal)
            if(LogStep or Logging):
                print("log:" + "执行指令->"+" "+command.replace(split_signal," ") + " 得到结果 " + objectDic[TaskList[TaskIndex+9]] + " to " + TaskList[TaskIndex+9])
                LogStep = 0
            TaskIndex += len(varList)+8
        elif TaskKey == "if": 
            a = 0 
            b = 0
            try: 
                try:  
                    a =  int(TaskList[TaskIndex+1])
                except ValueError:   
                    a= int(float(objectDic[TaskList[TaskIndex+1]]))
                try:  
                    b =  int(TaskList[TaskIndex+2])  
                except ValueError:   
                    b = int(float(objectDic[TaskList[TaskIndex+2]]))
                if a>b :
                    if(LogStep or Logging):
                        print(f"log:因为{TaskList[TaskIndex+1]}>{TaskList[TaskIndex+2]}跳转到{TaskList[TaskIndex+3]}")
                        LogStep = 0
                    TaskIndex = gotoDic[TaskList[TaskIndex+3]]
                elif b>a :
                    if(LogStep or Logging):
                        print(f"log:因为{TaskList[TaskIndex+1]}<{TaskList[TaskIndex+2]}跳转到{TaskList[TaskIndex+4]}")
                        LogStep = 0
                    TaskIndex = gotoDic[TaskList[TaskIndex+4]]
                elif a==b:
                    if(LogStep or Logging):
                        print(f"log:因为{TaskList[TaskIndex+1]}=={TaskList[TaskIndex+2]}跳转到{TaskList[TaskIndex+5]}")
                        LogStep = 0
                    TaskIndex = gotoDic[TaskList[TaskIndex+5]]
            except:
                if(LogStep or Logging):
                    print(f"log:因为{TaskList[TaskIndex+1]}和{TaskList[TaskIndex+2]}不能进行整数比较，不进行跳转")
                    LogStep = 0
                TaskIndex += 6
        else:
            print("error:不明的指令" + "->"+ TaskKey)
            TaskIndex += 1

#######################

def sohii_cmd():
    print("Sohii Language " + sohii_Language_version)
    while(1):
        try:
            command=input("-->")
            run(command)
        except:
            pass

#######################

if __name__=='__main__':
    sohii_cmd()

#0.0.2

#if 支持立即数判定。
#只支持整形

#sohii_v
#object int1 object int2 object int3 object int1 sohii_v int1 int2 int3 obj_print int1 obj_print int2 obj_print int3
#index_add index_add_obj
#jump的相对位置版本
#index_add 4 print A print B
#object int obj_set int 4 index_add_obj int print A print B
#sohii
#int str obj float关键字
#等同于 int/str/obj A T -> object A obj_set A T
#set 完全等同于obj_set
#copy to 关键字
#用于复制对象 # 支持立即数
#copy A B C ... to a b c ...
#int A 1 int B 2 int C 3 copy A A A  to A B C obj_print A obj_print B obj_print C
#int A 1 int AA 1 int AAA 1 int B 2 int C 3 copy A AA AAA  to A B C obj_print A obj_print B obj_print C
#input 关键字
#获取输入至对象
#str str1 0 input str1 obj_print str1

#0.0.3 环境更新

#新概念，环境交互。

#解释器目前可以对变量和sohii函数进行注册（可覆盖），从而实现上下文之间的联系。
#将变量A以name的名称注册到环境中
#reg name A
#以name的名称从环境中获取变量赋值给B
#get name B

#sohii函数 关键字func 支持重载关键字 函数内是新指令，属于局部变量。
#支持 无参数 无输入 无输出 重载关键字 注册关键字 模式

#标准格式
#func name A B ... ( return A ) to D
#调用方式
#name A B ...  D

#无输入模式
#func name (int a 1 return a) to D
#调用方式
#name D

#无输出模式
#func name A B ... ( obj_print A  obj_print B )
#调用方式
#name A B ... 

#无输出无输入格式
#func name (print 1111)
#调用方式
#name

#定义一次性可以打印两个对象的关键字
#func print_2_obj A B (print A print B)
#int a 1 int b 2 print_2_obj a b 

#重载关键字以屏蔽原有关键字功能，从而限制嵌入python程序的sohii控制台控制的权限。
#例子
#在这之前实现了函数 !help !buy
#关闭调试功能
#func log ( )
#此后log将无法正确运行
#func stoplog ( )
#此后logging将无法停止
#func func( )
#关闭定义函数功能

#sohii文件源代码
#支持换行模式(仅sohii文件)
#注释模式

#导入sohii文件功能,支持重复导入功能。
#inc math.sohii
#重载了add让add指令失效
#func add ( )
#重新导入sohii库文件
#inc math.sohii
#int a 1 int b 1 int c 0 add( a b ) c obj_print c


