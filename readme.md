# 目录说明：
DoubanMovieTop250文件夹是使用Scrapy+Xpath实现的爬取豆瓣top250电影目录的项目；  
runoob文件夹是使用Scarpy实现的爬取runoob+Xpath教程链接的项目；  
WebSpiderbeginer文件夹是使用requests加beautifulsoup实现的对某漫画网站某热门漫画的爬取项目；

## DoubanMovieTop250和runoob
两个项目类似，以runoob为例进行说明。  
Scrapy项目目录如下：
```
.
│  link.csv
│  scrapy.cfg
│
└─runoob
    │  items.py
    │  middlewares.py
    │  pipelines.py
    │  settings.py
    │  __init__.py
    │
    ├─spiders
    │  │  cslink.py
    │  │  __init__.py
    │  │
    │  └─__pycache__
    │          cslink.cpython-37.pyc
    │          __init__.cpython-37.pyc
    │
    └─__pycache__
            items.cpython-37.pyc
            settings.cpython-37.pyc
            __init__.cpython-37.pyc
```
使用命令`Scrapy startproject projectname` 建立一个工程，会自动生成类似目录结构。  
使用命令`cd projcetname`切换到项目目录。  
使用命令`Scrapy genspider domain domain.com`建立一个爬虫文件, 会自动在spider文件夹中生成对应py文件。  
配置Items.py,这个是装数据的容器, 定义要爬取数据内容。  
编写spider.py,包含爬虫的主要逻辑和方法。  
配置pipelines.py文件, 定义对爬取项（Scraped Item）的处理类。  
可以修改setting.py, 里面有很多修改爬虫选项的设置。  
使用命令`scrapy crawl cslink -o link.csv`, 开始爬虫并且将数据存入link.csv文件中

## WebSpiderbeginner
这个项目是使用requests+beautiful soup实现的图片爬取爬虫，实现的比较完整，包括将爬取的图片按章节合并成pdf，并且将所有章节pdf合并成一个带书签目录的全书pdf

### image_spider.py
实现漫画爬取，包括漫画目录链接爬取，单张图片爬取，所有图片爬取。

### jpg2pdf.py
实现将爬取到的图片按文件夹合并成若干pdf文件，对应一个章节一个pdf。  
其中图片顺序的确定比较麻烦，通过图片命名的方式来按需求顺序排列图片。

### mergePDF.py
实现将所有pdf按照名称顺序合并成一个大pdf，并且以单个pdf名称作为书签和目录。
