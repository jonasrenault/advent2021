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

with open('input.txt', 'r') as f:
    inputs = f.readlines()

inputs = [[int(c) for c in line.strip()] for line in inputs]
inputs = np.array(inputs)
avg = np.mean(inputs, axis=0)
gamma = np.array(avg > 0.5, dtype=int)
epsilon = np.array(avg < 0.5, dtype=int)


# %%

def tobits(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

decg = tobits(gamma)
dece = tobits(epsilon)
print("Gamma: ", decg)
print("Epsilon: ", dece)
print("Total", decg * dece)


# %%

import operator

def rating(inputs, op):
    col = 0
    while len(inputs) > 1:
        if op(np.mean(inputs[:, col]), .5):
            inputs = inputs[inputs[:, col] == 1, :]
        else:
            inputs = inputs[inputs[:, col] == 0, :]
        col += 1
    return inputs

oxygen = rating(inputs, operator.ge)
co2 = rating(inputs, operator.lt)

# %%
print("Support rating = ", tobits(oxygen[0]) * tobits(co2[0]))
