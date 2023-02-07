#随机试验概率测试代码
import random
import time

def run(box_list,number):
    index = number
    for i in range(50):
        if box_list[index] == number :
            return i+1
        else:
            index = box_list[index]
    return 0

if __name__ == '__main__':
    start = time.time()
    box_list = [] #创建一个空的list
    success_time = 0 #成功的次数
    failure_time = 0 #失败的次数
    test_time = 10000 #测试次数
    for i in range (0,100) : #创建一个1-100的list
        box_list.append(i)
    for m in range (0,test_time):#100次试验
        random.shuffle(box_list) #打乱原来的列表
        failed_flag = False #失败标识符
        for number in range(0,100) : #单次试验开始
            ires = run(box_list,number)
            if ires == 0:
                failed_flag = True #如果有一次循环失败 则整体失败 退出循环 失败标识符置true
                break
        if failed_flag == True:
            failure_time += 1
        else:
            success_time += 1
    life_rate = success_time/test_time
    print("指针成功概率为%f%%" % (life_rate*100))
    end = time.time()
    print("程序运行时间%f秒" % (end-start))
else:
    print("其他模块执行的")