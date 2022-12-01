# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     notebook_metadata_filter: voila
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   voila:
#     template: neurolang
# ---

# %% [markdown]

# Day 1

# %%

import pandas as pd
import numpy as np

with open("input.txt", "r") as f:
    inputs = f.readlines()

lines = [l.strip() for l in inputs]

# %%
from collections import OrderedDict

dirs = OrderedDict(
    [
        ("ne", (1, 1)),
        ("nw", (-1, 1)),
        ("se", (1, -1)),
        ("sw", (-1, -1)),
        ("e", (2, 0)),
        ("w", (-2, 0)),
    ]
)

def coords_for_line(line):
    x, y = (0, 0)
    i = 0
    while i < len(line):
        for k, (x0, y0) in dirs.items():
            if line[i:].startswith(k):
                i += len(k)
                x += x0
                y += y0
    
    return x, y

# %%

line = "nwsweene"
coords_for_line(line)

# %%

line = "sesenwnenenewseeswwswswwnenewsewsw"
coords_for_line(line)

def black_tiles(lines):
    blacks = set()
    for line in lines:
        x, y = coords_for_line(line)
        if (x, y) in blacks:
            blacks.remove((x, y))
        else:
            blacks.add((x, y))

    return blacks

res = black_tiles(lines)
len(res)

# %%

def black_neighbors(coords, blacks):
    count = 0
    x, y = coords
    for (x0, y0) in dirs.values():
        if (x + x0, y + y0) in blacks:
            count += 1
    return count

def flip_tiles(blacks):
    flips = set()
    for (x, y) in blacks:
        count = 0
        for (x0, y0) in dirs.values():
            neighbor = (x + x0, y + y0)
            if neighbor in blacks:
                count += 1
            elif black_neighbors(neighbor, blacks) == 2:
                flips.add(neighbor)

        if count == 0 or count > 2:
            flips.add((x, y))
    for key in flips:
        if key in blacks:
            blacks.remove(key)
        else:
            blacks.add(key)

# %%

def repeat_until(pattern, days):
    tiles = black_tiles(pattern)
    for x in range(days):
        flip_tiles(tiles)
    return len(tiles)

repeat_until(lines, 100)


# %%
