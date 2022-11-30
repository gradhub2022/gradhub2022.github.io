# pip install qrcode[pil]

import qrcode
img = qrcode.make('https://www.duckduckgo.com/')
img.save("my_qr.png")