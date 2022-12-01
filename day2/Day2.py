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

df = pd.read_table("input.txt", header=None)
df.columns = ('input',)

# %%

input = df.input

forward = df.input[df.input.str.startswith('forward')].str.split(" ", expand=True).iloc[:, 1].astype(int).sum()
up = df.input[df.input.str.startswith('up')].str.split(" ", expand=True).iloc[:, 1].astype(int).sum()
down = df.input[df.input.str.startswith('down')].str.split(" ", expand=True).iloc[:, 1].astype(int).sum()
print(forward, down, up)
total = forward * (down - up)
print(total)

# %%

def get_depth(inputs):
    aim, depth = 0, 0
    for i in inputs:
        if i.startswith("down"):
            aim += int(i[len("down") + 1:])
        elif i.startswith("up"):
            aim -= int(i[3:])
        else:
            depth += int(i[len("forward") + 1:]) * aim
    return depth

get_depth(input.values)
# %%

forward * get_depth(input.values)
# %%
