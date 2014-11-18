from PIL import Image


mask1 = Image.open('shadow-mask.png')
temp1 = Image.new('L', (1080, 1080))
temp1.paste(mask1)
temp1.save('shadow-mask2.png')

mask2 = Image.open('transparency-mask.png')
temp2 = Image.new('L', (1080, 1080))
temp2.paste(mask2)
temp2.save('transparency-mask2.png')
