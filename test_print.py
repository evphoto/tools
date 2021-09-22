#!/usr/bin/env python3
import qrcode

img = qrcode.make('09/20/2021')
img.save('testqrcode.png')
