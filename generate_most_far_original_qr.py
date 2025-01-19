# pip install pyzbar pillow segno
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
mandatory = [(0, 9, False), (0, 10, False), (2, 10, True), (10, 0, True), (11, 0, True), (12, 1, False), (12, 2, True), (21, 9, False), (23, 9, False), (24, 9, False), (5, 11, True), (7, 9, True), (8, 9, False), (8, 12, False), (9, 10, False), (10, 11, True), (11, 11, True), (12, 11, True)]

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


    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # uncomment this for cool animation
    # img.save("qr_code.png")


    # Decode the QR from the image data
    img = Image.open(img_bytes)
    decoded_objects = decode(img)


    return decoded_objects[0].data.decode("utf-8") if decoded_objects else None


qr = qrcode.QRCode()
qr.add_data(link)
qr.make()

orig = deepcopy(qr.modules)

qr2 = qrcode.QRCode()
qr2.add_data(fake_link)
qr2.make()

target = qr2.modules

differences = []

for x, row in enumerate(target):
    for y, p in enumerate(row):
        for xx, yy, val in mandatory:
            if xx == x and yy == y:
                target[x][y] = val


print()
for row in orig:
    print("    " + "".join('██' if col else '  ' for col in row))
print()
print()
for row in target:
    print("    " + "".join('██' if col else '  ' for col in row))
print()


for x, row in enumerate(orig):
    for y, p in enumerate(row):
        if p != target[x][y]:
            differences += [(x, y, p)]

print(f"{len(differences)} differences left")
print(differences)

def mutantaz(number, arr2):

    for zzz in itertools.combinations(arr2, number):
        # zzz = arr1 + list(zzz)
        out = []
        for x, row in enumerate(target):
            line = []
            for y, f in enumerate(row):
                d = f
                for xx, yy, pp in zzz:
                    if xx == x and yy == y:
                        d = pp
                line += [d]
            out += [line]
        yield out, zzz

border = 4
ef = 1
try:
    ef = int(sys.argv[1])
except:
    pass

for error in range(ef, len(differences)):
    print(error)
    for matrix, mutation in mutantaz(error, differences):
        xxx = parse_as_image(matrix)
        if xxx:
            print(xxx)
            print(f"[{error}] Difference: {len(differences)  - error} (border {border})")
            print()
            print(mutation)
            for row in matrix:
                print("    " + "".join('██' if col else '  ' for col in row))
            if xxx == link:
                exit()
            break

print()
print()

