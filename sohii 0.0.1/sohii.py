import time
import threading
import random
sohii_Language_version ="0.0.1"

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
    def logging():
        pass
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
        elif TaskKey == "obj_set":
            if(LogStep or Logging):
                print("log:" +"设定立即对象->"+TaskList[TaskIndex+1] +"为"+ TaskList[TaskIndex+2])
                LogStep = 0
            objectDic[TaskList[TaskIndex+1]] = TaskList[TaskIndex+2]
            TaskIndex += 3
            pass
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
            try:
                a = int (float(objectDic[TaskList[TaskIndex+1]]))
                b = int (float(objectDic[TaskList[TaskIndex+2]]))
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