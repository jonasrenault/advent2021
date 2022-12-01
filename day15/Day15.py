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

# Day 15

# %%

from typing import Dict, List
import pandas as pd
import numpy as np
from collections import Counter, defaultdict

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

puzzle = np.array([[int(c) for c in l.strip()] for l in puzzle])


# %%

# Part 1: find minimum risk path in cave

dirs = [(1, 0), (0, 1)]


def set_min_risk(x, y, cave, risks):
    opts = [
        risks[x + d[0], y + d[1]]
        for d in dirs
        if x + d[0] < cave.shape[0] and y + d[1] < cave.shape[1]
    ]
    if opts:
        risks[x, y] = cave[x, y] + min(opts)
    else:
        risks[x, y] = cave[x, y]


def build_risks(cave):
    endx, endy = cave.shape
    endx -= 1
    endy -= 1
    risks = np.zeros(cave.shape)
    risks[endx, endy] = cave[endx, endy]
    for i in range(0, len(cave)):
        for j in range(endx, endx - i, -1):
            set_min_risk(endx - i, j, cave, risks)
            set_min_risk(j, endy - i, cave, risks)
        set_min_risk(endx - i, endy - i, cave, risks)
    return risks


risks = build_risks(puzzle)
print(f"Min total risk = {risks[0, 0] - puzzle[0, 0]}")

# %%

# Part 2: build larger cave


def tile_cave(cave, tiles):
    total_cave = np.empty((cave.shape[0] * tiles, cave.shape[1] * tiles))
    row_cave = cave
    col_cave = cave
    for x in range(tiles):
        for y in range(tiles):
            total_cave[
                x * cave.shape[0] : (x + 1) * cave.shape[0],
                y * cave.shape[1] : (y + 1) * cave.shape[1],
            ] = col_cave
            col_cave = col_cave + 1
            col_cave[col_cave == 10] = 1
        row_cave = row_cave + 1
        row_cave[row_cave == 10] = 1
        col_cave = row_cave
    return total_cave

large_cave = tile_cave(puzzle, 5)
risks = build_risks(large_cave)
print(risks)
# print(f"Min total risk = {risks[0, 0] - puzzle[0, 0]}")

# %%
