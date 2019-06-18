---
title: Linux中java -version改不了的问题
date: 2018-02-25 18:35:32

---
首先查看/etc/profile中的路径等等有没有问题。

因为一些历史原因，我的linux系统中jdk版本被我改得乱七八糟。

用java -version查看版本号

![](https://img-
blog.csdn.net/20180225182816180?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWXphcnJL/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

这是修改过后的，原来的jdk版本为1.6。

用which java 和which javac查看jdk所在

![](https://img-
blog.csdn.net/20180225182927813?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWXphcnJL/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

不用在意文件夹名字，进入文件夹（我这里是/usr/java/jdk1.6.0_45/bin）

![](https://img-
blog.csdn.net/20180225183114835?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWXphcnJL/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

如果软连接链接的地方不是所需jdk的目录，那就rm -rf java 和rm -rf javac

然后重新链接

ln -s $JAVA_HOME/bin/javac /usr/bin/javac

ln -s $JAVA_HOME/bin/java /usr/bin/java

然后进入/etc/alternatives

![](https://img-
blog.csdn.net/20180225183434540?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWXphcnJL/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

ll java把软连接改成所需目录



完成 ![](https://img-
blog.csdn.net/20180225183511687?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvWXphcnJL/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

