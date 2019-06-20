#coding:utf-8

from PIL import Image

# PartI 定义参数
# 输入的图片文件路径
#IMG = 'D:\PythonWorkSpace\\PictureTransferPictureCharacter\\ascii_dora.png'
IMG = 'D:\PythonWorkSpace\PythonProject\Project1_PictureTransferPictureCharacter\\ascii_dora.png'

# 输出字符画的宽度
WIDTH = 60
# 输出字符画的高度
HEIGHT = 45

# 字符画所使用的字符集，一共有70个字符
# 一个字符能表现一种颜色，字符种类越多，可以表现的颜色也越多，图片也会更有层次感
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# PartII 实现RGB值转字符的函数

# 下面是RGB值转字符的函数，注意alpha值为0的时候表示图片中该位置为空白（透明度）
# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha = 256):
    # 判断alpha值
    if alpha == 0:
        return ' '

    # 获取字符集的长度， 这里为70
    length = len(ascii_char)
    # 将RGB值转为灰度值gray， 灰度值范围为0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 灰度值范围为0-255，而字符集只有70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1) / length

    # 返回灰度值对应的字符
    return ascii_char[int(gray / unit)]

# PartIII 处理图片

if __name__ == '__main__':

    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ""

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将(j, i)坐标的RGB像素转为字符后添加到txt字符串
            # im.getpixel((j, i))获取得到坐标(j, i)位置的RGB像素值，返回的结果是一个元祖
            # 例如(1, 2, 3)或者(1, 2, 3, 0)。我们使用*可以将元祖作为参数传递给get_char,
            # 同时元祖中的每个元素都对应到get_char函数的每个参数。
            txt += get_char(*im.getpixel((j, i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)

    # 字符画输出到文件
    with open("output.txt", 'w') as f:
        f.write(txt)

