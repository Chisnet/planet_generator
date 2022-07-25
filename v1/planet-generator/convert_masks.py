from pathlib import Path

from PIL import Image

script_dir = Path(__file__).absolute().parent

mask1 = Image.open(f'{script_dir}/shadow-mask.png')
temp1 = Image.new('L', (1080, 1080))
temp1.paste(mask1)
temp1.save(f'{script_dir}/shadow-mask.png')

mask2 = Image.open(f'{script_dir}/transparency-mask.png')
temp2 = Image.new('L', (1080, 1080))
temp2.paste(mask2)
temp2.save(f'{script_dir}/transparency-mask.png')

mask3 = Image.open(f'{script_dir}/atmosphere.png')
temp3 = Image.new('RGBA', (1080, 1080))
temp3.paste(mask3)
temp3.save(f'{script_dir}/atmosphere.png')
