### 王者荣耀爬虫--头像与皮肤图片信息获取与保存

项目主要是爬取王者荣耀官网所有英雄皮肤的头像和皮肤图片，并且画出英雄与皮肤数量对应条形图

#### 主要文件有：

- useragentutil.py ：随机请求头
- saveherocsv.py ：获取官网数据并保存csv格式
- downloadimages.py：下载英雄头像图片
- heroskinsspider.py：获取英雄皮肤数据
- downloadheroskins.py：下载皮肤图片
- drawheroimage.py：绘制英雄皮肤数量柱形图

#### 运行环境：

- python 3.7

#### 需要安装的包：

- requests
- json
- os
- matplotlib.pyplot
- lxml.html
- selenium

#### 思维导图：![王者荣耀Spider](.\王者荣耀Spider.png)