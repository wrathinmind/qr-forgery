import itertools
import string
import qrcode
from typing import List
from copy import copy, deepcopy
import sys

data = "https://qr.spd.de/tp/1"
base = "https://qr-spd.de"

# Function to generate URI parts
def generate_uris():
    start = 1
    try:
        start = int(sys.argv[1])
    except:
        pass
    uri_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "/?&=_%#!-+!@$^*()"
    for length in range(start, 20):  # URI parts length can vary
        for combination in itertools.product(uri_characters, repeat=length):
            for start in ['/', '?']:
                yield start + "".join(combination)

def compare_matrices(matrix1, matrix2) -> int:
    differences = 0
    for x, row in enumerate(matrix1):
        for y, v in enumerate(row):
            if matrix2[x][y] != v:
                differences += 1

    return differences



qr0 = qrcode.QRCode()
qr0.add_data(data)
qr0.make()
orig = deepcopy(qr0.modules)

# Generate domains and combine with URI parts
_min = 255
for idx, domain in enumerate([base]):
    for uri in generate_uris():
        dmn = f"{domain}{uri}"
        qr1 = qrcode.QRCode()
        qr1.add_data(dmn)
        qr1.make()
        new_m = qr1.modules
        cmp = compare_matrices(orig, new_m)
        if cmp < _min:
            _min = cmp
            print(dmn, cmp, f"[{data}]")

        if _min <= 46:
            break

        if idx > 10:  # Limit link
            break
