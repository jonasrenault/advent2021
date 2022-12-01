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

lines = [ l.strip().replace(' -> ', ',').split(',') for l in inputs]
lines = [[int(x) for x in l] for l in lines]
lines = np.array(lines)


# %%
grid = np.zeros((1000, 1000))

vertical = lines[lines[:, 0] == lines[:, 2]]
horizontal = lines[lines[:, 1] == lines[:, 3]]
print(f"{len(vertical)} vertical and {len(horizontal)} horizontal")

# %%
for row in horizontal:
    grid[row[1], min(row[0], row[2]): max(row[0], row[2]) + 1] += 1

for col in vertical:
    grid[min(col[1], col[3]): max(col[1], col[3]) + 1, col[0]] += 1

np.count_nonzero(grid[grid > 1].astype(int))

# %%
grid = np.zeros((1000, 1000))

for row in lines:
    if row[0] == row[2]:
        # vertical
        grid[min(row[1], row[3]): max(row[1], row[3]) + 1, row[0]] += 1
    elif row[1] == row[3]:
        # horizontal
        grid[row[1], min(row[0], row[2]): max(row[0], row[2]) + 1] += 1
    else:
        stepx = -1 if row[0] > row[2] else 1
        stepy = -1 if row[1] > row[3] else 1
        for i in range(0, abs(row[2] - row[0]) + 1):
            grid[row[1] + i*stepy, row[0] + i * stepx] += 1
        # grid[row[1]:row[3] + stepy:stepy, row[0]:row[2] + stepx:stepx] +=1

np.count_nonzero(grid[grid > 1].astype(int))


# %%
x = np.zeros((10, 10))
s = [[9, 7, 7, 9]]
for row in s:
    if row[0] == row[2]:
        # vertical
        x[min(row[1], row[3]): max(row[1], row[3]) + 1, row[0]] += 1
    elif row[1] == row[3]:
        # horizontal
        x[row[1], min(row[0], row[2]): max(row[0], row[2]) + 1] += 1
    else:
        stepx = -1 if row[0] > row[2] else 1
        stepy = -1 if row[1] > row[3] else 1
        for i in range(0, abs(row[2] - row[0]) + 1):
            x[row[1] + i*stepy, row[0] + i * stepx] += 1
x
# %%

# %%
