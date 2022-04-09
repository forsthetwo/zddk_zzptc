# zddk_zzptc
基于python开发的打卡程序

## 使用说明

本程序仅供学习参考

使用时默认接受使用后产生的不良后果

下面是使用教程

### 一、配置

本程序所运行共需要两个文件

第一个：程序本体

![image-20220409011318571](https://github.com/forsthetwo/zddk_zzptc/raw/main/tp/image-20220409011318571.png)



第二个：配置文件（只需要写一次）

在程序本体同一文件夹下创建一个名为`data.txt`的文件

![image-20220409011901316](https://github.com/forsthetwo/zddk_zzptc/raw/main/tp/image-20220409011901316.png)

在`data.txt`里第一行写上学号

第二行写上身份证后六位

第三行写上1~5之间的一位数，含义如下

```
1.未接种2.已接种未完成3.已接种已完成4.已接种加强针5.未接种加强针
```

写完之后保存`data.txt`就好了

配置就完成了



### 二、运行



之后点击程序就可以打卡了

 双击右键运行出现运行成功的提示就好了

![image-20220409013019251](https://github.com/forsthetwo/zddk_zzptc/raw/main/tp/image-20220409013019251.png)





其实还可以使用windows定时任务实现定时自动打卡（没有服务器的情况下）

 windows定时启动程序请参考

[windows 10添加定时任务 - 小虎利思 - 博客园 (cnblogs.com)](https://www.cnblogs.com/wensiyang0916/p/5773828.html)

