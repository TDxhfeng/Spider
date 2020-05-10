import saveherocsv
import downloadimages
import heroskinsspider
import downloadheroskins
import drawheroimage


def main():
    #爬取王者荣耀官网数据并保存CSv格式
    saveherocsv.main()
    #下载英雄头像图片
    downloadimages.main()
    #获取英雄皮肤数据
    heroskinsspider.main()
    #下载皮肤图片
    downloadheroskins.main()
    #绘制英雄皮肤数量柱形图
    drawheroimage.main()

if __name__ == '__main__':
    main()