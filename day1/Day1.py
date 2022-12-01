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

inputs = df.input.values
diff = inputs - np.append(inputs[:1], inputs[:-1])
print(f" There are {np.count_nonzero(diff > 0)} increasing depths")

# %%
diff2 = inputs[3:] - inputs[:-3]
print(f" There are {np.count_nonzero(diff2 > 0)} increasing sliding windows")
# %%
