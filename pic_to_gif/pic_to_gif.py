from PIL import Image,ImageSequence

gif = []
pictures = ['3.png', '5.png', '6.png', '7.png', '5.png']
for pic in pictures:
    img = Image.open(pic)  # 開啟圖片
    gif.append(img)                    # 加入串列
# 儲存為 gif
gif[0].save("my_work.gif", save_all=True, append_images=gif[1:], duration=250, loop=0, disposal=0)