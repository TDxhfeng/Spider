import json
import os
from matplotlib import pyplot as plt


def read_hero_skin_by_json():
    """读取hero_tail文件获取英雄名称列表和皮肤个数列表"""
    hero_skin_file = open("./herofile/hero_detail.json","r",encoding="utf-8")
    content = hero_skin_file.read()

    hero_lists = json.loads(content)
    hero_skin_file.close()

    #名称列表
    hero_name_lists = []
    #皮肤个数列表
    skin_num_lists =[]
    for element in hero_lists:
        hero_name = element["hero_name"]
        hero_name_lists.append(hero_name)

        hero_skins = element["hero_skins_list"]
        skin_num = len(hero_skins) #计算列表长度统计皮肤个数
        skin_num_lists.append(skin_num)
    return hero_name_lists,skin_num_lists


def draw_hero_image(x1,y):
    """绘制柱形图"""
    # 正常显示中文编码
    plt.rcParams["font.sans_serif"] = ["SimHei"]
    # 生成相对应英雄个数列表
    x = [i for i in range(1,len(x1)+1)]
    # 画布大小
    plt.figure(figsize=(24,10),dpi=80)
    #绘制网格
    plt.grid(alpha = 0.4)
    #添加标题
    plt.title("王者荣耀皮肤个数数据柱形图")
    #横纵坐标标题
    plt.xlabel("英雄名称")
    plt.ylabel("皮肤个数（单位:个）")
    #绘制
    plt.bar(x,y,width=0.8)
    #调整显示位置并且添加标签
    plt.xticks(x,x1,rotation =75)
    #调整横纵坐标范围
    plt.xlim(0,len(x1)+1)

    #创建并保存图片
    dir_name = "./iamge"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    plt.savefig(dir_name+"/hero.png")
    #显示图形
    plt.show()

def main():
    """统计每个英雄所拥有的皮肤数量"""
    #读取文件
    hero_names_lists,skin_nums_lists = read_hero_skin_by_json()

    #绘制并保存图形
    draw_hero_image(hero_names_lists,skin_nums_lists)


if __name__ == '__main__':
    main()