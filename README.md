演示分布式定时任务

在slow_task运行时，如果有其他地方调用slow_task， 则会失败、丢弃。


在演示代码中， 每隔10秒启动hello函数， hello函数调用slow_task函数。

但是由于slow_task的执行时间为30秒，

故而在30秒内，hello函数对slow_task函数的调用，只有一次成功，另外两次调用则失败、丢弃。

同时， 如果在浏览器中输入网址，调用slow_task函数， 都会失败、丢弃。

如此，实现在同一时间内，只有一个slow_task运行，不会多个同时运行。



#环境需求

ubuntu 18.04

python3.6


#安装项目依赖模块

pip3 install -r requirements.txt


#配置参数

配置项目中config.py文件


#开启web服务

/bin/bash run.sh

#开启celery的worker

/bin/bash run_worker.sh



#测试

1、在浏览器输入

http://localhost:9090/

2、在终端观察输出





