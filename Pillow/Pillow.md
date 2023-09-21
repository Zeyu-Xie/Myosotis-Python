# Pillow

## Tutorial

### Using the Image Class

##### Import

```
from PIL import Image
im = Image.open("favicon.jpeg")
```

### Rading and Writng Images

##### Image Info

```
print(im.format)
print(im.size)
print(im.mode)
```

##### Convert Format

```
# Method 1
with Image.open("favicon.jpeg") as im:
    im.save("favicon.png")

# Method 2
im = Image.open("favicon.jpeg")
im.save("favicon", "PNG")
```

##### Seperate Extension

```
f, e = os.path.splitext("favicon.png")
print(f, e)
```

##### Thumbnail

```
size = (32, 32)
im.thumbnail(size)
im.save("favicon", "BMP")
```

##### Use Arguments

```
print(sys.argv[1])
```

##### Identify Image Files

```
for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass
```

### Cutting, Pasting and Merging Images

##### Create a (rectangular) Box Area

```
box = (100, 100, 400, 400)
```

##### Sub Rectangle from the Image

```
region = im.crop(box)
```

##### Transpose the Region

```
region = region.transpose(Image.Transpose.ROTATE_180)
```

##### Paste the Region

```
# When pasting regions back, the size of the region must match the given region exactly.
im.paste(region, box)
```

##### Rolling an Image

```
def roll(im, delta):
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im
```

##### Merging Images

```
def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im
```

##### Splitting and Merging Bands

```
r, g, b = im.split()
im4 = Image.merge("RGB", (b, g, r))
```

### Geometrical Transforms

##### Simple Geometrical Transforms

```
out = im.resize((128, 128))
out = im.rotate(45)
```

##### Transposing an Image

```
out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
out = im.transpose(Image.Transpose.ROTATE_90)
out = im.transpose(Image.Transpose.ROTATE_180)
out = im.transpose(Image.Transpose.ROTATE_270)
```

### Color Transforms

##### Converting Between Codes

```
with Image.open("hopper.ppm") as im:
    im = im.convert("L")
```

### Image Enhancement

##### Filters

```
out = im.filter(ImageFilter.GaussianBlur)
```

| 滤镜名称          | 描述                                                 |
| ----------------- | ---------------------------------------------------- |
| BLUR              | 使图像变得模糊，可以减少图像中的噪点和细节。         |
| CONTOUR           | 突出图像中的轮廓，使图像看起来更加清晰。             |
| DETAIL            | 增强图像的细节，使图像更加锐利。                     |
| EDGE_ENHANCE      | 增强图像中的边缘，使其更加清晰和饱满。               |
| EMBOSS            | 创建浮雕效果，使图像看起来像是凸起的或凹陷的。       |
| SHARPEN           | 增强图像的清晰度，使边缘更加明显。                   |
| SMOOTH            | 平滑图像，减少图像中的噪点和细节。                   |
| GAUSSIAN_BLUR     | 高斯模糊滤镜，通过应用高斯函数对图像进行模糊处理。   |
| CONTOUR_ENHANCE   | 增强图像中的轮廓和边缘，使其更加鲜明。               |
| EMBOSS_MORE       | 创建更强烈的浮雕效果，增加图像中凸起和凹陷的对比度。 |
| EDGE_ENHANCE_MORE | 提供更强的边缘增强效果，使图像的边缘更加明显。       |
| SHARPEN_MORE      | 提供更强烈的锐化效果，使图像的边缘和细节更加清晰。   |
| UNFILTER          | 取消图像上应用的滤镜效果，恢复原始图像。             |

##### Point Operations

Applying Point Transforms

```
# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)
```

Processing Individual Brands

```
# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)
```

##### Enhancement

Enhancing Images

```
from PIL import ImageEnhance

enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
```

### Image Sequences

##### Reading Sequences

```
from PIL import Image

with Image.open("animation.gif") as im:
    im.seek(1)  # skip to the second frame

    try:
        while 1:
            im.seek(im.tell() + 1)
            # do something to im
    except EOFError:
        pass  # end of sequence
```

##### Using the ImageSequence Iterator Class

```
from PIL import ImageSequence
for frame in ImageSequence.Iterator(im):
    # ...do something to frame...
```

### Post Script Painting

##### Drawing Post Script

```
from PIL import Image
from PIL import PSDraw

with Image.open("hopper.ppm") as im:
    title = "hopper"
    box = (1 * 72, 2 * 72, 7 * 72, 10 * 72)  # in points

    ps = PSDraw.PSDraw()  # default is sys.stdout or sys.stdout.buffer
    ps.begin_document(title)

    # draw the image (75 dpi)
    ps.image(box, im, 75)
    ps.rectangle(box)

    # draw title
    ps.setfont("HelveticaNarrow-Bold", 36)
    ps.text((3 * 72, 4 * 72), title)

    ps.end_document()
```

### More on Reading Images

##### Reading from an Open File

```
from PIL import Image

with open("hopper.ppm", "rb") as fp:
    im = Image.open(fp)
```

##### Reading from Binary Data

```
from PIL import Image
import io

im = Image.open(io.BytesIO(buffer))
```

##### Reading from URL

```
from PIL import Image
from urllib.request import urlopen
url = "https://python-pillow.org/images/pillow-logo.png"
img = Image.open(urlopen(url))
```

##### Reading from a .tar Archive

```
from PIL import Image, TarIO

fp = TarIO.TarIO("Tests/images/hopper.tar", "hopper.jpg")
im = Image.open(fp)
```

##### Batch Processing

```
import glob
from PIL import Image


def compress_image(source_path, dest_path):
    with Image.open(source_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(dest_path, "JPEG", optimize=True, quality=80)


paths = glob.glob("*.png")
for path in paths:
    compress_image(path, path[:-4] + ".jpg")
```

You can also use the pathlib module instead of the glob module

```
from pathlib import Path

paths = Path(".").glob("*.png")
for path in paths:
    compress_image(path, path.stem + ".jpg")
```

### Controlling the Decoder

##### Reading in Draft Mode

```
from PIL import Image

with Image.open(file) as im:
    print("original =", im.mode, im.size)

    im.draft("L", (100, 100))
    print("draft =", im.mode, im.size)
```

The output may be like this

```
original = RGB (512, 512)
draft = L (128, 128)
```

