这是网上搜集的unittest + ddt 的demo

HTMLTestRunner修改Python3的版本
http://blog.51cto.com/hzqldjb/1590802

ddt
http://ddt.readthedocs.io/en/latest/example.html

ddt json yml
https://www.cnblogs.com/hellowcf/p/6962935.html

Python接口自动化实战10-2 DDT结合excel使用
https://v.qq.com/x/page/f054243eprq.html

unittest介绍
https://www.cnblogs.com/hhudaqiang/p/6596043.html

logging
https://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
https://www.cnblogs.com/weiok/p/5592448.html
文件配置方式，log输出时使用stdout切换模块之后不换行，换成stderr之后就可以正常换行。。。估计是个bug，文件里面一直是能换行的
使用common.log_configer时直接运行testcase.TestJson.py没有问题，但是通过run_test.py运行就报错，现改用写死日志配置的方式（log_configer2.py）避免该报错

环境：
python3.6.3
ddt==1.1.1
PyYAML==3.12
xlrd==1.1.0
执行run_test.py即可

使用Anaconda时需使用
%windir%\System32\cmd.exe "/K" C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3
中pip安装所需要的包

excel部分后续再加