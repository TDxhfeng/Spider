import os
import requests
import useragentutil


def read_hero_file():
    """从hero.csv中读取数据内容，获得英雄名称、头像图片地址"""
    #open file
    hero_file = open("./herofile/hero.csv","r",encoding="utf-8")
    lines = hero_file.readlines()
    #切片不要第一行表头
    content = lines[1:]
    #空列表 存放英雄信息 如：[{...},{...},{...}]
    lists = []

    for hero_before_element in content:
        hero_item = {}
        #通过切片去掉每一行的"\n"符号
        hero_element = hero_before_element[:-1]
        #分割字符串成子串，并以列表的形式返回  # split
        hero_list = hero_element.split(",")

        hero_item["hero_name"] = hero_list[0]
        hero_item["hero_url"] = hero_list[1]
        list.append(hero_item)
    return lists


def creat_hero_dir(hero_lists):
    """创建英雄名称相应目录"""
    dir_name = "./herofile"

    for hero_element in hero_lists:
        hero_name = hero_element["hero_name"]
        #拼接
        hero_path = dir_name + "/" + hero_name
        #判断
        if not os.path.exists(hero_path):
            os.makedirs(hero_path)
        print("所有目录创建成功")


def download_hero_image(hero_list):
    """下载头像图片"""
    dir_name = "./herofile"
    for hero_element in hero_list:
        hero_name = hero_element["hero_name"]
        hero_url = hero_element["image_url"]

        headers = useragentutil.get_headers()
        response = requests.get(hero_url,headers=headers)
        image_content = response.content

        hero_path = dir_name+"/"+hero_name+"/1"+hero_name+".jpg"
        #文件操作 写入
        with open(hero_path,"wb") as hero_file:
            hero_file.write(image_content)
        print("正在下载--(%S)--图片"%hero_name)
    print("所有图片头像已经下载成功")


def main():
    # 读取hero.csv内容
    hero_datas = read_hero_file()
    # 创建英雄名称相应目录
    creat_hero_dir(hero_datas)
    #下载英雄头像图片
    download_hero_image(hero_datas)



if __name__ == '__main__':
    main()