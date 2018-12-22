# set-log-analysis
定势日志分析

#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
import datetime

def analy_log(path):
    with open(path,'r') as file_log:
        file_log=file_log.readlines()
        error_list = []
        for line in file_log:
            line = line.strip("\n").strip("\r").split(",")
            if len(line) == 5:
                start_list = []
                end_list = []
                file_size,start_year,start_time,end_year,end_time = line           
                starttime_no_ms = start_year + "_" + start_time.split(".")[0]
                starttime_ms=start_time.split(".")[1]
                startArray = time.strptime(starttime_no_ms,"%Y/%m/%d_%H:%M:%S")
                startstamp = str(time.mktime(startArray))
                start_list.append(startstamp.split(".")[0])
                start_list.append(starttime_ms)
                starttime = "".join(start_list)
                #print start_list
            
                endtime_no_ms = end_year + "_" + end_time.split(".")[0]
                endtime_ms=end_time.split(".")[1]
                endArray = time.strptime(endtime_no_ms,"%Y/%m/%d_%H:%M:%S")
                endstamp = str(time.mktime(endArray))
                end_list.append(endstamp.split(".")[0])
                end_list.append(endtime_ms)
                endtime = ''.join(end_list)
                try:
                    down_speed = round(float(('{0}'.format(int(file_size)/(int(endtime)-int(starttime))*1000/1024))),3)
                    print '{0}KB/S'.format(down_speed)
                except Exception as e:
                    line=line + "计算下载速度的时候出错"
                    error_list.append(line)
            elif len(line) != 5 or line.isspace():
                error_list.append(line)
        if len(error_list) != 0:
            print "~~~~~~~~~~~~~~~~上面是下载速度,下面是异常的~~~~~~~~~~~~~~~"
            for err in error_list:
                print err
        else:
            pass
if __name__=='__main__':
    path='./test.log'
    analy_log(path)
