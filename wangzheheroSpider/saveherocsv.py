import requests
import useragentutil
import lxml.html
import os
from selenium import webdriver


def get_html_datas(url_datas):
    """爬取英雄界面network代码"""
    headers = useragentutil.get_headers()
    #获取页面内容
    driver = webdriver.PhantomJS("./phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver.get(url_datas)
    html_content = driver.page_source
    driver.quit()
    return html_content

#空列表 存放整体信息
hero_list = []

def get_hero_datas(url):
    """获取所有英雄的信息内容"""
    metree = lxml.html.etree
    parser = metree.HTML(url)
    #li英雄列表信息
    li_list = parser.xpath("//div[@class='herolist-content']/ul[@class='herolist clearfix']/li")
    #遍历
    for li_element in li_list:
        #   定义空列表存放信息
        hero_item = []
        #获得英雄名称
        hero_name = li_element.xpath("./a/text()")[0]
        hero_item.append((hero_name))
        #获得头像图片地址
        hero_image_url = "https"+ li_element.xpath("./a/img/@src")[0]
        hero_item.append(hero_image_url)

        #获取英雄信息界面地址
        hero_url = li_element.xpath("./a/@href")[0]
        hero_item.append(hero_url)
        hero_list.append(hero_item)
    return hero_list


def download_hero_csv(hero_lists):
    """以csv格式保存数据内容"""
    dir_name = "./herofile"
    if not os.path.exists(dir_name):
        os.makedirs((dir_name))
        print("目录%s创建成功"%dir_name)
    #存放文件
    hero_file = open(dir_name+"hero.csv","w",encoding="utf-8")
    #表头
    hero_file.write("英雄地址,图片地址,详情地址\n")
    #写入
    for element in hero_list:
        hero = ",".join(element)
        hero_file.write(hero+"\n")
    hero_file.close()
    print("所有英雄数据已保存成功")


def main():
    """程序入口"""
    wangzherul = "https://pvp.qq.com/web201605/herolist.shtml"
    # 爬取王者网页数据
    html_datas = get_html_datas(wangzherul)

    #提取英雄数据信息
    hero_datas = get_hero_datas(html_datas)

    #保存为csv格式
    download_hero_csv(hero_datas)


if __name__ == '__main__':
    main()
