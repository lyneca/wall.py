import re
import sys
import subprocess
import colorsys
from dataclasses import dataclass
from random import random
import math

from PIL import Image, ImageDraw

@dataclass
class Display:
    width: int
    height: int
    x_off: int
    y_off: int

    def scale(self, factor):
        return Display(
            int(self.width * factor),
            int(self.height * factor),
            int(self.x_off * factor),
            int(self.y_off * factor)
        )

    def to_tuple(self):
        return (
            self.x_off,
            self.y_off,
            self.x_off + self.width,
            self.y_off + self.height
        )

output = subprocess.run('xrandr', stdout=subprocess.PIPE)
displays = [
    Display(*(int(y) for y in re.split(r'[x+]', x)))
    for x in re.findall(r'\d+x\d+\+\d+\+\d+', output.stdout.decode())
]

image = Image.open(sys.argv[1]).convert('RGBA')
size = image.size

full_width = max([display.x_off + display.width for display in displays])
full_height = max([display.y_off + display.height for display in displays])

if full_width / size[0] >= full_height / size[1]:
    scale_factor = size[0] / full_width
else:
    scale_factor = size[1] / full_height

scaled = [
    x.scale(scale_factor) for x in displays
]

sections = [
    image.crop(x.to_tuple())
    for x in scaled
]

tmp = Image.new('RGBA', image.size, (0, 0, 0, 0))

draw = ImageDraw.Draw(tmp)

for i, display in enumerate(scaled):
    color = colorsys.hsv_to_rgb(i / len(scaled), 1, 1)
    color = tuple([int(x * 255) for x in color] + [127])
    draw.rectangle(display.to_tuple(), fill=color)

image = Image.alpha_composite(image, tmp)

for i, section in enumerate(sections):
    size = (
        math.ceil(section.size[0] / scale_factor),
        math.ceil(section.size[1] / scale_factor)
    )
    section.save(f'out_{i}_{size[0]}x{size[1]}.png')

image.save('regions.png')
