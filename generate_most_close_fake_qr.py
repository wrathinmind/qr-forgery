# pip install pyzbar pillow qrcode
import itertools
import string
import qrcode
import random
from typing import List
import sys
import itertools

from PIL import Image
from pyzbar.pyzbar import decode
from io import BytesIO
from copy import copy, deepcopy

link = "https://qr.spd.de/tp/1"
fake_link = "https://qr-spd.de/txi$"


def parse_as_image(matrix, scale=10):
    rows = len(matrix)
    cols = len(matrix[0])

    img = Image.new("1", (cols * scale, rows * scale), 1)  # "1" mode is for 1-bit pixels (B/W)

    pixels = img.load()

    for y in range(rows):
        for x in range(cols):
            color = 0 if matrix[y][x] else 1  # Black for 1, white for 0
            for i in range(scale):
                for j in range(scale):
                    pixels[x * scale + i, y * scale + j] = color

    # just if you want to see the process
    # img.save("qr_code.png")


    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Decode the QR from the image data
    img = Image.open(img_bytes)
    decoded_objects = decode(img)

    return decoded_objects[0].data.decode("utf-8") if decoded_objects else None

link = "https://qr.spd.de/tp/1"
qr = qrcode.QRCode()
qr.add_data(link)
qr.make()

orig = deepcopy(qr.modules)

qr2 = qrcode.QRCode()
qr2.add_data(fake_link)
qr2.make()

forged = qr2.modules
size = len(forged[0])
print()
for row in orig:
    print("    " + "".join('██' if col else '  ' for col in row))
print()
print()
for row in forged:
    print("    " + "".join('██' if col else '  ' for col in row))
print()


bifferences = []
differences = []
border = 6
try:
    border = int(sys.argv[1])
except:
    pass

bb = [i for i in range(0,border)] + [i for i in range(size-border,size)]

for x, row in enumerate(orig):
    for y, p in enumerate(row):
        if x not in bb and y not in bb:
            if p != forged[x][y]:
                differences += [(x, y, p)]

print(f"{len(differences)} differences in center")
for x, row in enumerate(orig):
    for y, p in enumerate(row):
        if x in bb or y in bb:
            if p != forged[x][y]:
                bifferences += [(x, y, p)]

print(f"{len(bifferences)} differences on borders")


def mutantaz(number, arr1, arr2):

    for zzz in itertools.combinations(arr2, number):
        xxx = arr1 + list(zzz)
        out = []
        for x, row in enumerate(forged):
            line = []
            for y, f in enumerate(row):
                d = f
                for xx, yy, pp in xxx:
                    if xx == x and yy == y:
                        d = pp
                line += [d]
            out += [line]
        yield out, xxx

ef = 1

for error in range(ef, len(differences)):
    print(error)
    for mat, fix in mutantaz(error, bifferences, differences):
        xxx = parse_as_image(mat)
        if xxx:
            print(xxx)
            print(f"[{error}] Difference: {len(differences)  - error} (border {border})")
            print()
            print()
            print(fix)
            for row in mat:
                print("    " + "".join('██' if col else '  ' for col in row))
            if xxx != fake_link:
                exit()
            break

print()
print()

