from selenium import webdriver
import lxml.html
import json


def read_hero_csv():
    """通过读取csv文件数据，获取英雄名称，详情地址"""
    dir_name = "./herofile"
    hero_file = open(dir_name+"hero.csv","r",encoding="utf-8")

    lines = hero_file.readlines()[1:]
    #空列表存放
    lists = []
    for element in lines:
        item = {}
        hero = element[:-1]
        hero_list = hero.split(",")
        #名字
        hero_name = hero_list[0]
        item["hero_name"] = hero_name
        #详情信息
        hero_url = hero_list[2]
        item["hero_url"] = hero_url
        lists.append(item)
    return lists


def parse_hero_skins_url(http_url):
    """获取皮肤页面数据源代码"""
    #获得对象
    driver = webdriver.PhantomJS("./phantomjs-2.1.1-windows/bin/phantomjs.exe")
    #请求网址
    try:
        driver.get(http_url)
        #超时限制
        driver.set_script_timeout(2)
        #内容
        html_content = driver.page_source
    except Exception as e:
        print(str(e))
    #关闭浏览器
    driver.quit()
    return  html_content


def get_hero_skin_datas(html_content):
    """提取英雄皮肤数据"""
    metree = lxml.html.etree
    parser = metree.HTML(html_content)

    #放回列表
    lists = []
    li_list = parser.xpath("//div[@class='pic-pf']/ul[@class='pic-pf-list pic-pf-list3']/li")
    for li_element in li_list:
        skin_item = {}
        #皮肤名称
        skin_name = li_element.xpath("./p/text(")[0]
        skin_item["skin_name"] = skin_name
        #皮肤地址
        skin_url = "https:" + li_element.xpath("./i/img/@data-imgname")[0]
        skin_item["skin_url"] = skin_url
        lists.append(skin_url)
    return lists


def save_hero_skin_data_by_json(hero_list):
    """以json文件保存数据内容"""
    json_strs = json.dumps(hero_list,ensure_ascii=False,indent=2) #相当于格式化
    #文件操作
    with open("./herpfile/hero_detail.json","w",encoding="utf-8") as hero_file:
        hero_file.write(json_strs)


def main():
    """进入英雄详情地址获取信息"""
    #读取csv文件
    hero_datas = read_hero_csv()
    # 提取英雄名称、皮肤数据[皮肤名称，皮肤地址]
    # 样式[{hero_name:鲁班,hero_skins_lists[{一个以上皮肤信息和网址},{},{}]},{英雄},{英雄}]
    #外部大列表
    all_hero_skin_lists = []
    for element in hero_datas:
        # 大列表中的字典
        item ={}
        #名称
        hero_name = element["hero_name"]
        item["hero_name"] = hero_name

        #详情地址
        hero_url = element["hero_url"]
        #获取皮肤页面数据源代码
        html_datas = parse_hero_skins_url(hero_url)
        #提取皮肤数据
        get_hero_skin_datas(html_datas)
        #添加皮肤到item中
        item["hero_skins_list"] = get_hero_skin_datas(html_datas)
        #效果
        print("英雄--(%s)--皮肤数据正在下载！！" %hero_name)
        #添加到大列表中
        all_hero_skin_lists.append(item)
        #保存数据到json文件中
        save_hero_skin_data_by_json(all_hero_skin_lists)
    print("所有英雄皮肤数据保存成功")

if __name__ == '__main__':
    main()