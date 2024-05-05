class sohii():
    __sohii_language_version_1__ = "3"
    __sohii_language_version_2__ = "0"
    __sohii_language_version_3__ = "0"
    __sohii_language_version__ = __sohii_language_version_3__ + "." + __sohii_language_version_2__ + "." + __sohii_language_version_1__ 
    #环境内的函数
    __SOHII_FUNCTIONS__ = {}
    #环境内的变量
    __SOHII_OBJECT__ = {}
    #sohii关键字
    __KEYWORD__ = {}
    def run(string , split_signal=" "):
        #指令预处理
        #处理换行
        string=string.replace("\n", " ")
        #生成字词列表
        TaskList=string.split(split_signal)
        #去除空字符串
        TaskList = [s for s in word_list if s]
        #末尾添加stop
        if TaskList and TaskList[-1] != "stop": 
            TaskList.append("stop") 
        NoStop = 1
        #定点字典
        gotoDic = {}
        #日志记录
        LogStep = 0
        Logging = 0
        #将无条件传送点进行注册
        for n, task in enumerate(TaskList):  
            if task == 'point':  
                if n + 1 < len(TaskList) and n + 2 < len(TaskList):  
                    gotoDic[TaskList[n + 1]] = n + 2
        #进入主循环
        while(NoStop):
            TaskKey=TaskList[TaskIndex]
            key = None
            word_num = 0
            try:
                key , word_num = __SOHII_FUNCTIONS__[TaskKey]
            except:
                try:
                    key , word_num = __KEYWORD__[TaskKey]
                except:
                    print("寻找不到关键字！"+ TaskKey)
                    return 
            for i in range(TaskIndex+1,mword_num+1):
                i.append

for i in range(0+1,0+1):
    print(i)