# wall.py - a multihead wallpaper creator

## Dependencies

Tested on Linux only.

- Python: ^3.7
- Pillow
- `xrandr`

```bash
pip install Pillow
```

```bash
# For xrandr on Arch
sudo pacman -S xorg-xrandr
# Debian
sudo apt install x11-xserver-utils
```

## Usage

```bash
$ python3 wall.py [IMAGE]
```

## Example

Given this image (taken from [this reddit post](https://www.reddit.com/r/WidescreenWallpaper/comments/bvqt41/dreams_3440x1440/)):

![](https://external-preview.redd.it/maCo_IQpxZHQiKhC3btIbR1uw6Y06aGOpibwtQYkA1E.png?width=1024&auto=webp&s=96105512137914fa271b532879075078d6c7980d)

And (for example) my monitor setup, something like this:

```
+------+ +--------------+
|      | |              |
|      | |              |
|      | +--------------+
|      |
+------+

1024x1280+0+0, 1920x1080+1024+0
```

The script will output these two images, with the correct aspect ratio of my two monitors:

<img src="eg_1.png" height=300px>
<img src="eg_2.png" height=300px>

And this image showing where the crops were made:

![](eg_regions.png)

## Limitations

This script should work with any number of monitors, although untested. Currently, it will always try to crop from the top right of the source image.
