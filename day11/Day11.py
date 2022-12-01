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

# Day 11

# %%

from typing import Dict, List
import pandas as pd
import numpy as np

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

puzzle = np.array([[int(c) for c in l.strip()] for l in puzzle])

# %%

from itertools import product

# Part 1: Simulate flashes

def flash(puzzle, point):
    """
    Flash a point and its neighbors
    """
    x, y = point
    counts = 1
    for a, b in product((-1, 0, 1), (-1, 0, 1)):
        x0, y0 = x + a, y + b
        if 0 <= x0 < puzzle.shape[0] and 0 <= y0 < puzzle.shape[1]:
            puzzle[x0, y0] += 1
            if puzzle[x0, y0] == 10:
                counts += flash(puzzle, (x0, y0))
    return counts


def step(puzzle):
    puzzle = puzzle + 1
    tens = np.argwhere(puzzle == 10)
    counts = 0
    for x, y in tens:
        counts += flash(puzzle, (x, y))
    puzzle[puzzle > 9] = 0
    return puzzle, counts

# %%

flashes = 0
runs = 100
for x in range(runs):
    puzzle, c = step(puzzle)
    flashes += c
print("Total ", flashes , " for ", runs, " runs")


# %%

# Part 2: find complete flashes

flashes = 0
count = 0
while flashes != 100:
    puzzle, flashes = step(puzzle)
    count += 1

print("They all flashed on step ", count)
# %%
