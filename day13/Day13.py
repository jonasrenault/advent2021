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

# Day 13

# %%

from typing import Dict, List
import pandas as pd
import numpy as np
from collections import defaultdict

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

dots = np.array(
    [
        [int(c) for c in l.strip().split(",")]
        for l in puzzle
        if l.strip() and not l.startswith("fold")
    ]
)
folds = [
    l.strip()[11:].split("=") for l in puzzle if l.startswith("fold along")
]

# %%

# Part 1: create paper


def paper(dots):
    y, x = dots.max(axis=0)
    p = np.zeros((x + 1, y + 1))
    p[dots[:, 1], dots[:, 0]] = 1
    return p


def fold(paper, coord):
    axis, idx = coord
    idx = int(idx)
    if axis == "y":
        top = paper[idx:, :]
        bottom = paper[:idx, :]
    else:
        top = paper[:, idx:]
        bottom = paper[:, :idx]
    x, y = np.nonzero(top)
    if axis == "y":
        bottom[idx - x, y] = 1
    else:
        bottom[x, idx - y] = 1
    return bottom


p = paper(dots)
fp = fold(p, folds[0])
np.count_nonzero(fp)

# %%

# Part 2 : complete all folds

p = paper(dots)
for f in folds:
    p = fold(p, f)

s = p.shape[1] // 8
for l in range(0, p.shape[1], s):
    l = p[:, l : l + s].astype(int).astype(str)
    l[l == "0"] = "."
    l[l == "1"] = "#"
    print(l)
    print("===========")
    print("===========")

