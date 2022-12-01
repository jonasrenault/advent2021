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

# Day 8

# %%

from typing import Dict, List
import pandas as pd
import numpy as np

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

puzzle = np.array([[int(c) for c in l.strip()] for l in puzzle])

# %%

# Part 1: find low points
def lowpoints(puzzle):
    diff = puzzle[:, :-1] - puzzle[:, 1:]
    mask = np.hstack((diff < 0, np.ones((puzzle.shape[0], 1), dtype=bool)))
    diff = puzzle[:, 1:] - puzzle[:, :-1]
    mask &= np.hstack((np.ones((puzzle.shape[0], 1), dtype=bool), diff < 0))

    diff = puzzle[:-1, :] - puzzle[1:, :]
    mask &= np.vstack((diff < 0, np.ones((1, puzzle.shape[1]), dtype=bool)))
    diff = puzzle[1:, :] - puzzle[:-1, :]
    mask &= np.vstack((np.ones((1, puzzle.shape[1]), dtype=bool), diff < 0))

    return mask


# Risk is 1 + height of lowpoints
mask = lowpoints(puzzle)
sum((1 + puzzle)[mask])


# %%

# Part 2: count bazin size

from functools import reduce

dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))


def neighbors(point, puzzle):
    x, y = point
    return [
        (x + a, y + b)
        for a, b in dirs
        if 0 <= x + a < puzzle.shape[0] and 0 <= y + b < puzzle.shape[1]
    ]


def basin(point, puzzle):
    return reduce(
        set.union,
        (
            basin(neighbor, puzzle)
            for neighbor in neighbors(point, puzzle)
            if 9 > puzzle[neighbor] > puzzle[point]
        ),
        set((point,)),
    )


# %%
basins = np.nonzero(mask.astype(int))
basin_sizes = np.array([len(basin((x, y), puzzle)) for x, y in zip(*basins)])
total = np.argpartition(basin_sizes, -3)[-3:]
basin_sizes[total].prod()

# %%
