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

# Day 17

# %%

from typing import Dict, List
import pandas as pd
import numpy as np
import re
from collections import Counter, defaultdict

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

puzzle[0].strip()

m = re.search(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', puzzle[0].strip())
target = [int(c) for c in m.groups()]

# %%

# Part 1

from itertools import product

def probe_positions(position, velocity, target):
    x, y = position
    vx, vy = velocity
    x0, x1, y0, y1 = target
    positions = [position]
    while x < max(x0, x1) and y > min(y0, y1):
        x += vx
        y += vy
        positions.append((x, y))
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
    return positions

def hits_target(positions, target):
    x0, x1, y0, y1 = target
    for x, y in positions:
        if min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1)  :
            return True
    return False

def maximum_height(position, target):
    x0, x1, y0, y1 = target
    max_height = 0
    for vx, vy in product(range(max(x0, x1)), range(max(abs(y0), abs(y1)))):
        positions = probe_positions(position, (vx, vy), target)
        if hits_target(positions, target):
            max_y = max(positions, key=lambda x: x[1])[1]
            if max_y > max_height:
                max_height = max_y
                mvx, mvy = vx, vy
    
    return max_height, (mvx, mvy)


# %%


# hits_target(probe_positions((0, 0), (6, 9), target), target)
maximum_height((0, 0), target)


# %%

def all_velocities(position, target):
    x0, x1, y0, y1 = target
    velocities = []
    print("y=", min(y0, y1), max(abs(y0), abs(y1)))
    for vx, vy in product(range(max(x0, x1) + 1), range(min(y0, y1), max(abs(y0), abs(y1)))):
        positions = probe_positions(position, (vx, vy), target)
        if hits_target(positions, target):
            velocities.append((vx, vy))
    
    return velocities

# %%

len(all_velocities((0, 0), target))
# %%
