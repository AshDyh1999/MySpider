# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os

#单张图片下载
def download_single_img(url_info, pic_dir, name):
    try:
        if not os.path.exists(pic_dir):
            print('创建文件夹 %s'%(pic_dir))
            os.mkdir(pic_dir)
            # os.chdir(pic_dir)
        else:
            # print('%s 目录已经存在'%(pic_dir))
            pass

        # print("正在下载图片 %s"%(url_info))
        if name not in os.listdir(pic_dir):
            response = requests.get(url_info)
            # 获取的文本实际上是图片的二进制文本
            img = response.content
            # 拷贝到本地文件 w 写 b 二进制 wb代表写入二进制文本
            path= pic_dir + '/' + name
            with open(path, 'wb') as f:
                f.write(img)
        else:
            print('%s 文件已经存在'%(name))
    except:
        print('保存失败')
        pass

#获取目录
def get_memu(target):
    #发送请求，返回html文档
    req = requests.get(url=target)
    html = req.content.decode('utf-8')
    #使用BeautifulSoup解析文档
    bf = BeautifulSoup(html, "html.parser")
    #ul标签
    ul_bf = BeautifulSoup(html, "html.parser")
    ul = ul_bf.find_all('ul', class_ = 'chapter')
    a_bf = BeautifulSoup(str(ul[1]), "html.parser")
    #a标签
    a = a_bf.find_all('a')
    names = []
    urls = []
    for each in a:

        names.append(str(each.text).replace('\ufeff',''). strip())
        urls.append(server + each.get('href'))
        # print(str(each.text).replace(' ','_'), server + each.get('href'))
    
    return names, urls

#下载所有pic
def get_picture(names, urls):
    for i, each in enumerate(urls):
        # print(i,each,names[i])
        if(i>-1):
            name = names[i]
            print(name)
            flag = 1
            while(flag == 1):
                req = requests.get(each)
                html = req.content.decode('utf-8')
                #解析页面
                bf = BeautifulSoup(html, "html.parser")
                #找到下一页标签
                a_bf = bf.findAll('a', id = 'pb_next')
                next_page_html = str(a_bf[0].get('href'))
                next_page = next_page_html.split('.')[0]
                if('_' not in next_page):
                    page = str(eval(page + '+1'))
                    jpg_url = server2 + chapter + '/' + page + '.jpg'
                    print(next_page ,'第%s章,第%s页'%(chapter, page), jpg_url)
                    download_single_img(jpg_url, name.replace(' ', '_'), page+'.jpg')
                    break
                else:
                    chapter = next_page.split('_')[0].rjust(4,'0')
                    page = next_page.split('_')[1]
                    jpg_url = server2 + chapter + '/' + page + '.jpg'
                    print('第%s章,第%s页'%(chapter, page), jpg_url)
                    download_single_img(jpg_url, name.replace(' ', '_'), page+'.jpg')
                    each = server + next_page_html

if __name__ == '__main__':
    #目录
    target = 'http://m.tangsanshu.com/manhua/01/index.html'

    #单话
    target2 = 'http://m.tangsanshu.com/manhua/01/1_1.html'  #内容 
    target3 = 'http://m.tangsanshu.com/manhua/01/1.html'    #封面
    img_url = 'http://img.tangsanshu.com/comic/0001/1.jpg'  #图片地址

    #server
    server = 'http://m.tangsanshu.com/manhua/01/'
    server2 = 'http://img.tangsanshu.com/comic/'
    names , urls = get_memu(target)
    
    get_picture(names, urls)
   