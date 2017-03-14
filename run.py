# -*- coding: utf-8 -*-


import load_jiang
import network
import time
import os



for k in range(3,7):
    training_data, validation_data, test_data = load_jiang.jiang2("/Users/gaominghui/git/jiang/history.xls",k)
    now_date = time.strftime("%Y-%m-%d", time.localtime())
    if  not os.path.exists("/Users/gaominghui/git/jiang_log/"+now_date):
        os.mkdir("/Users/gaominghui/git/jiang_log/"+now_date)
    f = open("/Users/gaominghui/git/jiang_log/"+now_date+"/log.txt",'w')
    f.close()
    
    for i in range(40,34*k/2,10):
        net = network.Network([34 * k, i, 34],now_date)
        for  p in range(5,15,5):
            net.SGD(training_data, 300, p, 1.2, test_data=test_data)
