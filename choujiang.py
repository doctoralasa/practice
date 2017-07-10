#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
#创建一个员工列表
emplist=[]
#用with 自动关闭文件
with open('c://emps.csv') as f:
    empf=csv.reader(f)
    for emp in empf:
        emplist.append(emp)
print('进行一等奖抽奖，共有一名')
import random
#利用random模块的chice函数来从列表中随机选取一个元素
e1=random.choice(emplist)
#将中奖的员工从列表中提出
emplist.remove(e1)
print('一等奖的得主号码是%s'%e1)
print('进行3个二等奖的号码抽奖')
e2_1=random.choice(emplist)
emplist.remove(e2_1)
e2_2=random.choice(emplist)
emplist.remove(e2_2)
e2_3=random.choice(emplist)
emplist.remove(e2_3)
print('获得3个二等奖的号码是%s%s%S',(e2_1，e2_2,e2_3))
#进行三等奖之类的抽奖