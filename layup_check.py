# -*- coding: utf-8 -*-

import os
import json
import matplotlib.pyplot as plt
import numpy as np
import math
import database_connect_test
#from utils.anomaly import ghost

new_video_path, new_video_id, new_video_date= database_connect_test.new_video_id()
video_path= '/home/data/uploads/'+ new_video_path
video_date= new_video_date
video_id= new_video_id
openpose_output_path='/home/json_out/json'+ str(video_id)
path = openpose_output_path
files= os.listdir(path)
files.sort()


count = 0
count_1 = 0
count_2 = 0
sum = []
original = []
x=[]
y=[]

body= list()
for i in range (0, 25):
    body.append(dict())
    body[i]["x"]= []
    body[i]["y"]= []

main_role_x = 960
frame_height = 1080
j = 0


# 取主角所有節點x的平均，避免只取一點資料而那點資料有問題
def average_x(jf):
    average = 0
    x_sum = 0
    count_x = 0
    for i in range(0, 25):
        if jf[3 * i] != 0:
            x_sum += jf[3 * i]
            count_x += 1
    # print(count_x)
    average /= count_x
    return average

# 補遺失點

def fill_lose(original):
    pre = 0
    follow = 0
    adjust = original
    tmp = 0
    d = 0
    for i in range(len(original)):
        if (adjust[i] == 0):
            pre = original[i - 1]
            for j in range(i + 1, count):
                if (original[j] != 0):
                    follow = original[j]
                    tmp = j
                    break
            d = (follow - pre) / (j - i + 1)
            ct = 1
            for k in range(i, tmp):
                adjust[k] = pre + (ct) * d
                ct += 1

    return adjust


# 找靠近主要腳色的骨架
def alg1(jf):
    temp = 0
    near = 0

    for i in range(0):

        # near= 該骨架與main_role_x的距離
        # 點1的數據不可以出問題
        near = abs(average_x(jf['people'][0]['pose_keypoints_2d']) - main_role_x)
        if abs(average_x(jf['people'][i]['pose_keypoints_2d']) - main_role_x) < near:
            near = abs(average_x(jf['people'][i]['pose_keypoints_2d']) - main_role_x)
            temp = i
    # print(jf['people'][temp]['pose_keypoints_2d'][1*6])
    # print(near)

    return jf['people'][temp]['pose_keypoints_2d']

# 起腳為左腳在前
def check_first_step_1(jf):
    checker = None
    for i in range(1, count):  # First Step
        if body[14]['x'][i - 1] > body[11]['x'][i - 1] and body[14]['x'][i] > body[11]['x'][i] and body[14]['x'][i + 1] < body[11]['x'][
            i + 1] and body[14]['x'][i + 2] < body[11]['x'][i + 2] and j == 0:  # judge first step (Right)
            #print(sum[i], ':', 'First Step is right')
            comment_1 = 1 # 1 : 第一步正確
            checker = True
            i += 1
            break

        elif body[14]['x'][i - 1] < body[11]['x'][i - 1] and body[14]['x'][i] < body[11]['x'][i] and body[14]['x'][i + 1] > body[11]['x'][
            i + 1] and body[14]['x'][i + 2] > body[11]['x'][i + 2] and j == 0:
            #print(sum[i], ':', "Incorrect First Step")
            comment_1 = 0 # 0 : 第一步錯誤

    for count_1 in range(count):
        if body[11]['x'][count_1] < body[14]['x'][count_1]:
            count_1 += 1
        else:
            break
    total = 0
    for i in range(0, 10):
        sum[i] = abs(body[14]['x'][i] - body[14]['x'][0])
        total = total + sum[i]

    avg = total / 10
    if abs(body[14]['x'][count_1] - body[14]['x'][0]) > avg + 50:
        checker = False

    if not bool(checker):
        #print("Incorrect First Step")
        comment_1 = 0

    return comment_1 , i


# 起腳為右腳在前
def check_first_step_2(jf):

    for count_2 in range(count):
        if body[11]['x'][count_2] > body[14]['x'][count_2]:
            count_2 += 1
        else:
            break

    total = 0
    for i in range(0, 10):
        sum[i] = abs(body[11]['x'][i] - body[11]['x'][0])
        total = total + sum[i]

    avg = total / 10

    if abs(body[11]['x'][count_2] - body[11]['x'][0]) > avg+50:
        comment_1 = 1 # 1 : 第一步正確

    else:
        comment_1 = 0 # 0 : 第一步錯誤


    return comment_1 , count_2


def check_second_step(jf,i):

    for k in range(i+1,count):
        if body[14]['x'][k - 1] < body[11]['x'][k - 1] and body[14]['x'][k] < body[11]['x'][k] and body[14]['x'][k+ 1] > body[11]['x'][
            k + 1] and body[14]['x'][k + 2] > body[11]['x'][k + 2]:  # judge second step (Left)
            comment_2 = 1 # 1 : 第二步正確
            break


    return comment_2 , k

def check_traveling(jf, k):
    for l in range(k + 1, count):
        if body[14]['x'][l - 1] > body[11]['x'][l - 1] and body[14]['x'][l] > body[11]['x'][l] and body[14]['x'][l + 1] < body[11]['x'][l + 1] and body[14]['x'][l + 2] < body[11]['x'][l + 2]:  # judge third step (Right)
            l += 1
            # print(body_14_y[l])
            break
        else:
            pass

    for m in range(l, count):
        if body[11]['y'][l] > body[11]['y'][l + 1] and body[11]['y'][l] > body[11]['y'][l + 2] and body[11]['y'][l] > body[11]['y'][l + 3]:
            comment_3 = 0 # Traveling


        else:
            comment_3 = 1 # No Traveling
            break

    return comment_3


def check_arm(jf, index):

    v32_x= body[2]['x'][index]- body[3]['x'][index]
    v32_y= body[2]['y'][index]- body[3]['y'][index]
    v34_x= body[4]['x'][index]- body[2]['x'][index]
    v34_y= body[4]['y'][index]- body[3]['y'][index]

    Lx= np.sqrt(v32_x*v32_x+ v32_y*v32_y)
    Ly= np.sqrt(v34_x*v34_x+ v34_y*v34_y)

    cos_angle=(v32_x* v34_x+ v32_y*v34_y)/(Lx*Ly)

    angle=np.arccos(cos_angle)
    judge_angle_2=angle*360/2/np.pi
    #print(judge_angle_2)
    if 160 <= judge_angle_2 <= 180:
        comment_4 = 2 # Perfect Finish

    elif 140 <= judge_angle_2 < 160:
        comment_4 = 1 # Good Finish

    elif 120 <= judge_angle_2 < 140:
        comment_4 = 0 # OK Finish

    else:
        comment_4 = 11 # Bad Finish

    return comment_4


for file in files:
    with open(path+"/"+file , 'r') as reader:
        data = reader.read()
        jf_1 = json.loads(data)
        #print(jf_1['people'][0]['pose_keypoints_2d'])

        #print(jf)
        json_size = len(jf_1['people'])
        count += 1

        if json_size != 0:
            jf= alg1(jf_1)
            body[2]['x'].append(jf[3 * 2])
            body[3]['x'].append(jf[3 * 3])
            body[4]['x'].append(jf[3 * 4])
            body[8]['x'].append(jf[3 * 8])
            body[11]['x'].append(jf[3 * 11])
            body[14]['x'].append(jf[3 * 14])
            body[19]['x'].append(jf[3 * 19])
            body[20]['x'].append(jf[3 * 20])
            body[21]['x'].append(jf[3 * 21])
            body[22]['x'].append(jf[3 * 22])
            body[23]['x'].append(jf[3 * 23])
            body[24]['x'].append(jf[3 * 24])


            body[2]['y'].append(frame_height - jf[1 + 3 * 2])
            body[3]['y'].append(frame_height - jf[1 + 3 * 3])
            body[4]['y'].append(frame_height - jf[1 + 3 * 4])
            body[7]['y'].append(frame_height - jf[1 + 3 * 7])
            body[8]['y'].append(frame_height - jf[1 + 3 * 8])
            body[10]['y'].append(frame_height - jf[1 + 3 * 10])
            body[11]['y'].append(frame_height - jf[1 + 3 * 11])
            body[14]['y'].append(frame_height - jf[1 + 3 * 14])
            body[19]['y'].append(frame_height - jf[1 + 3 * 19])
            body[20]['y'].append(frame_height - jf[1 + 3 * 20])
            body[21]['y'].append(frame_height - jf[1 + 3 * 21])
            body[22]['y'].append(frame_height - jf[1 + 3 * 22])
            body[23]['y'].append(frame_height - jf[1 + 3 * 23])
            body[24]['y'].append(frame_height - jf[1 + 3 * 24])

            sum.append(count)

        if json_size == 0:
            count-=1

body= fill_lose(body) # 補點

index = body[8]['y'].index(max(body[8]['y']))
if abs(body[10]['y'][index] - body[10]['y'][index-1]) > 200: # delete the outlier
    body[10]['y'][index] = 0
    max = max(body[10]['y'])
    index = body[10]['y'].index(max)+3


if body[11]['x'][0] < body[14]['x'][0]:
    print('左腳在前')
    comment_1, i = check_first_step_1(jf)
    print(comment_1)
    if comment_1 == 0:
        database_connect_test.layup(video_id, comment_1, 11, 11)
        exit()

    comment_2, k = check_second_step(jf, i)
    print(comment_2)

    comment_3 = check_traveling(jf, k)
    print(comment_3)
    if comment_3 == 0:
        database_connect_test.layup(video_id, comment_1, comment_3, 11)
        exit()

    comment_4 = check_arm(jf, index)
    database_connect_test.layup(video_id, comment_1, comment_3, comment_4)


else:
    print('右腳在前')
    comment_1, i = check_first_step_2(jf)
    print(comment_1)
    if comment_1 == 0:
        database_connect_test.layup(video_id, comment_1, 11, 11)  # 11 : 代表前面錯誤就不判斷後面的動作
        exit()

    comment_2, k = check_second_step(jf, 0)
    print(comment_2)

    comment_3 = check_traveling(jf, k)
    print(comment_3)
    if comment_3 == 0:
        database_connect_test.layup(video_id, comment_1, comment_3, 11)
        exit()

    comment_4 = check_arm(jf, index)
    database_connect_test.layup(video_id, comment_1, comment_3, comment_4)