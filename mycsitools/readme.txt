---------------------------------------------------------------
作者：余迎港 
日期：2018-03-11
1、该软件建立在csitools已能使用命令行运行的情况下，机器上需安装csitools工具，并可以使用

2、需要安装python、python-numpy、python-pyqtgraph以及PYQT4

3、该软件仅辅助可视化以及简便化操作

4、经测试，发送器仅可以不超过500HZ频率发包的情况下收包器不会崩溃，否则收包底层服务将出现recv:no buffer space available错误，并崩溃

5、直接点击start_rcver.sh 或 start_tsmter.sh，弹框后选择在终端中运行，否则在命令行中将这两个文件设置为可运行文件（sudo chmod 777 xxx.sh）


---------------------------------------------------------------
代码结构：

1、发送端：CSItransmitter.py
接收图形化界面的发包参数，按下Start按钮后fork一个进程，运行CSiTools初始化命令，运行random_packet程序发包，并监控random_packet程序的输出，实时显示在命令行标准输出上。
按下stop按钮后，杀死子线程
按下close图标后，运行sudo ifconfig mon0 down 命令关闭网卡，之后杀死自身且由于自身死亡，子进程死亡（存疑，好像是这样，如果不是，可以于closeEvent()中加入杀死子进程代码）
***************************************************************
2、接收端：
A：通信层log_to_file2.c
主要功能：接收物理层收到的包并取出数据，将二进制原始数据存为文件，并使用Unix_socket与csireader.py进行本地进程TCP通信，CSiReader为服务器端，log_to_file2为客户端。
目前问题：不增加Unix_socket时可以以最大频率收包，增加后，仅能以不高于500Hz频率收包，若发包频率超过该值后，将发生recv:no baffer space available错误并自动崩溃。
使用说明：需要将conf目录中几个头文件以及log_to_file2.c拷贝至原log_to_file程序目录下（*/linux-80211n-csitool-supplementary/netlink）并编译为log_to_file2程序（gcc -o log_to_file2 log_to_file2.c）
问题解决方法：弃用Unix域socket方法，改用共享内存方式进行通信，后者为最快IPC方式。c-python样例代码已给出（不保证可以用），但需要增加信号量等方式互斥访问共享内存。

B:解析数据服务CSiReader.py
主要功能：作为Unix_socket tcp服务器，侦听log_to_file2发送来的数据并解析，解析后存为日志文件、csv格式csi数据文件，并将需要显示的数据通过multiprocessing.Queue进程通信传递给CSIdisplayer显示。
将处理、保存数据与数据显示模块分离，保证接收到的数据一定被保存（显示是不必须的）。
类初始化过程中创建unix_socket，运行一系列命令操作网卡，对CSiTools进行初始化工作；
process_bfee()函数，解析接收到的二进制csi数据
monitor()函数，循环监控Unix_socket通信，接收log_to_file2发送过来的数据，调用process_bfee解析数据后，将数据无阻塞压入Queue中，如果接收到结束进程event，结束进程

C：图形化显示程序CSIdisplayer2.py
基本思想：使用multiprocessing.Queue与csireader.py进行进程间通信，本程序updateData函数从Queue中取解析好的数据，放入一个data二维数组中，将data二维数组绘图展示；
当queue中堆积数据过多时，使用时间戳mod采样显示；
可选择仅显示某些天线的子载波数据，checkBoxChange函数中将对应天线的绘线隐藏，并与updateData函数中取出数据后不更新对应data二维数组中数据；
可选择仅显示某些子载波，checkBoxChange函数中，将对应子载波绘线隐藏，并与updateData函数中取出数据后不更新对应data二维数组中数据；
可选择显示幅值还是相位数据：切换后初始化data数组，并在取出数据后计算对应的值后放入data中；
主进程设置定时器，每0秒刷新运行updateData函数。


