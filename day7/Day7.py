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

inputs = np.array([int(x) for x in inputs[0].strip().split(",")])
inputs

# %%

crabs = np.array([16,1,2,0,4,2,7,1,2,14])
costs = []
for p in crabs:
    costs.append(abs(crabs - p).sum())
costs

# %%

costs = []
for p in range(crabs.max()):
    d = abs(crabs - p)
    d * (d + 1) / 2
    costs.append((d * (d + 1) / 2).sum())
costs

# %%
costs = []
for p in inputs:
    costs.append(abs(inputs - p).sum())
min(costs)

# %%

costs = []
for p in range(max(inputs)):
    d = abs(inputs - p)
    d * (d + 1) / 2
    costs.append((d * (d + 1) / 2).sum())
min(costs)

# %%
