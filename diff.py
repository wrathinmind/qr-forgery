# pip install pyzbar pillow segno
import itertools
import string
import segno
import random
from typing import List
import sys
import itertools

from PIL import Image
from pyzbar.pyzbar import decode
from io import BytesIO


# link = "https://qr.spd.de/tp/1"
# forged = segno.make_qr(link)
# size = len(forged.matrix[0])
# print()
# for row in forged.matrix:
#     print("    " + "".join('██' if col else '  ' for col in row))
# print()

def read_qr(name):
    out = []
    for line in open(name).read().strip().split('\n'):
        buf = [0 if line[i] == ' ' else 1 for i in range(0, len(line), 2)]
        if len(buf) < 25:
            buf += [0 for i in range(0, 25-len(buf))]
        out += [buf]
    return out

def diff(a, b):
    count = 0
    ddd = []
    for x, row in enumerate(a):
        for y, c in enumerate(row):
            if c != b[x][y]:
                count += 1
                ddd += [(x,y,b[x][y])]
    return count, ddd


orig = read_qr(sys.argv[1])
# print(orig)
forg = read_qr(sys.argv[2])

print(diff(orig, forg))


# def parse_as_image(matrix, scale=10):
#     # Dimensions of the QR code
#     rows = len(matrix)
#     cols = len(matrix[0])

#     # Create a new image with white background
#     img = Image.new("1", (cols * scale, rows * scale), 1)  # "1" mode is for 1-bit pixels (B/W)

#     # Get the pixel access object
#     pixels = img.load()

#     # Draw the QR code
#     for y in range(rows):
#         for x in range(cols):
#             color = 0 if matrix[y][x] else 1  # Black for 1, white for 0
#             for i in range(scale):
#                 for j in range(scale):
#                     pixels[x * scale + i, y * scale + j] = color

#     # Convert the image to a BytesIO object to simulate file-like behavior
#     img_bytes = BytesIO()
#     img.save(img_bytes, format="PNG")
#     img_bytes.seek(0)

#     # Decode the QR from the image data
#     img = Image.open(img_bytes)
#     decoded_objects = decode(img)

#     return decoded_objects[0].data.decode("utf-8") if decoded_objects else None

# link = "https://qr.spd.de/tp/1"
# # link = "https://qr.spd.de/spd-sticker"
# # link = "https://qr.spd.de/wk/35"
# orig = segno.make_qr(link)

# # link = "https://qrnspd.de/wf(1 44"
# # link = "https://qr-spd.de?asm6%"
# link = "https://qr-spd.de/px+P"
# forged = segno.make_qr(link)
# size = len(forged.matrix[0])
# print()
# for row in orig.matrix:
#     print("     " + "".join('██' if col else '  ' for col in row))
# print()


# bifferences = []
# differences = []
# border = 6
# bb = [i for i in range(0,border)] + [i for i in range(size-border,size)]

# for x, row in enumerate(orig.matrix):
#     for y, p in enumerate(row):
#         if x not in bb and y not in bb:
#             if p != forged.matrix[x][y]:
#                 differences += [(x, y, p)]

# print(f"{len(differences)} differences in common")
# for x, row in enumerate(orig.matrix):
#     for y, p in enumerate(row):
#         if x in bb or y in bb:
#             if p != forged.matrix[x][y]:
#                 bifferences += [(x, y, p)]

# print(f"{len(bifferences)} differences on borders")


# def mutantaz(number, arr1, arr2):
#     for zzz in itertools.combinations(arr2, number):
#         xxx = arr1 + list(zzz)
#         out = []
#         for x, row in enumerate(forged.matrix):
#             line = []
#             for y, f in enumerate(row):
#                 d = f
#                 for xx, yy, pp in xxx:
#                     if xx == x and yy == y:
#                         d = pp
#                 line += [d]
#                 # line += ['██' if d else '  ']
#             # print("     " + "".join(line))
#             out += [line]
#         yield out

#     # print(len(xxx))
#     # mutable_matrix = list(forged.matrix)
#     # for x,y,p in xxx:
#     #     # print(x, y, mutable_matrix[x])
#     #     mutable_matrix[x][y] = 0x00 if p else 0x01
#     #     # print(x, y, mutable_matrix[x])
    
#     # forged.matrix = tuple(mutable_matrix)
        
#     # print(len(arr) - number)
#     # for row in mutable_matrix:
#     #     print("".join('##' if col else '  ' for col in row))


# try:
#     ef = int(sys.argv[1])
# except:
#     ef = 1

# for error in range(ef, len(differences)):
#     print(error)
#     for mat in mutantaz(error, bifferences, differences):
#         xxx = parse_as_image(mat)
#         if xxx:
#             print(xxx)
#             print(f"[{error}] Difference: {len(differences)  - error}")
#             print()
#             print()
#             for row in mat:
#                 print("     " + "".join('██' if col else '  ' for col in row))
#             break

# print()
# print()

# # print(forged.show())
# # forged.show()
# # # Generate domains and combine with URI parts
# # _min = 255
# # for idx, domain in enumerate(['https://qr-spd.de']): #enumerate(generate_domains(base_url, tlds)):
# #     for uri in generate_uris():
# #         dmn = f"{domain}{uri}"
# #         new_m = segno.make(dmn).matrix
# #         cmp = compare_matrices(orig, new_m)
# #         if cmp < _min:
# #             _min = cmp
# #             print(dmn, cmp)

# #         if idx > 10:  # Limit output for demonstration purposes
# #             break


