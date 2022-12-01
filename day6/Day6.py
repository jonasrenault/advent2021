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

inputs = [np.array([int(x) for x in l.strip().split(",")]) for l in inputs]
inputs

# %%

def solve(days, fishes):
    for d in range(days):
        prev = fishes[d]
        zeros = prev == 0
        new = prev.copy()
        new[zeros] = 6
        new[~zeros] -= 1
        fishes.append(np.concatenate(
            (new, np.full(np.count_nonzero(zeros.astype(int)), 8)), axis=None
        ))


# %%
solve(80, inputs)
len(inputs[-1])


# %%
f = np.array([3,4,3,1,2])
f + 2
f7 = np.concatenate((f, f +2), axis=None)
f14 = np.concatenate((f7, f7 +2), axis=None)
f14.sum()


# %%
from collections import Counter

counts = Counter(inputs[0])
counts
counts.get(1, 0)

# %%

def solve(days, counts):
    for d in range(days):
        old_8 = counts.get(8, 0)
        old_7 = counts.get(7, 0)
        counts[8] = counts.get(0, 0)
        counts[7] = old_8
        for i in range(6):
            counts[i] = counts[i + 1]
        counts[6] = old_7 + counts[8]


counts = Counter([3,4,3,1,2])
solve(256, counts)
print(counts)
sum(counts.values())

# %%
inputs
counts = Counter(inputs[0])
solve(256, counts)
print(counts)
sum(counts.values())

# %%
