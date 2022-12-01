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
from collections import Counter, defaultdict

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

template = puzzle[0].strip()
pairs = dict([l.strip().split(" -> ") for l in puzzle[2:]])

# %%

# Part 1: apply polymer pairs


def polymerize(pairs, template):
    polymer = "".join(
        [
            template[i] + pairs.get(template[i : i + 2], "")
            for i in range(len(template))
        ]
    )
    return polymer


def score(pairs, template, steps):
    for _ in range(steps):
        template = polymerize(pairs, template)
    c = Counter(template)
    print(f"Distribution after {steps} steps: {c}")
    return c.most_common()[0][1] - c.most_common()[-1][1]


score(pairs, template, 10)


# %%

# Part 2 : do 40 steps


def template_to_map(template):
    template_map = defaultdict(int)
    for i in range(len(template)):
        template_map[template[i]] += 1
        if len(template[i : i + 2]) == 2:
            template_map[template[i: i + 2]] += 1
    return template_map


def smart_polymerize(pairs, template_map):
    next_step_map = defaultdict(int)
    for k, v in template_map.items():
        if len(k) == 1:
            next_step_map[k] = v
    for key, value in template_map.items():
        if len(key) == 2:
            if key in pairs:
                next_step_map[key[0] + pairs[key]] += value
                next_step_map[pairs[key] + key[1]] += value
                next_step_map[pairs[key]] += value
            else:
                next_step_map[key] += value
    return next_step_map

def smart_score(pairs, template, steps):
    template_map = template_to_map(template)
    for _ in range(steps):
        template_map = smart_polymerize(pairs, template_map)
    c = Counter()
    for k, v in template_map.items():
        if len(k) == 1:
            c[k] = v
    print(f"Distribution after {steps} steps: {c}")
    return c.most_common()[0][1] - c.most_common()[-1][1]

smart_score(pairs, template, 40)

#%%


# %%
