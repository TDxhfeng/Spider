import json
import requests
import useragentutil


def read_hero_skin_by_json():
    """读取hero_detail.json文件"""
    with open("./herofile/hero_detail.json","r",encoding="utf-8") as hero_skin_file:
        content = hero_skin_file.read()
        #还原python格式
        py_content_lists = json.loads(content)
    return py_content_lists


def main():
    """下载皮肤图片"""
    #读取json文件
    hero_lists = read_hero_skin_by_json()
    #遍历
    for hero_element in hero_lists:
        hero_name = hero_element["hero_name"]
        hero_skins = hero_element["hero_skin_list"]

        # [{'skin_name': '流云之翼', 'skin_url ': 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/506/506-bigskin-1.jpg'},

        headers = useragentutil.get_headers()
        for skins_element in hero_skins:
            #皮肤名称
            skin_name = skins_element["skin_name"]
            #皮肤url
            skin_url = skins_element["skin_url"]
            #下载图片
            response = requests.get(skin_url,headers=headers)
            image_content = response.content

            #文件操作保存图片
            with open("./herofile/"+hero_name+"/"+skin_name+".jpg","wb") as image_file:
                image_file.write(image_content)
            print("正在下载——>%s-->皮肤%s图片.."%(hero_name,skin_name))
        print("----%s的所有皮肤图片下载成功"%hero_name)
    print("所有英雄图片下载成功")

if __name__ == '__main__':
    main()