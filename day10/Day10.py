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

# Day 10

# %%

from typing import Dict, List
import pandas as pd
import numpy as np

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

puzzle = [l.strip() for l in puzzle]

# %%

mapping = {"[": "]", "(": ")", "{": "}", "<": ">"}

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

# Part 1: find corrupted lines
def corrupted(puzzle):
    corrupt = []
    for line in puzzle:
        chunks = []
        for c in line:
            if c in mapping.keys():
                chunks.append(c)
            else:
                expected = mapping[chunks.pop()]
                if c != expected:
                    print("Expected ", expected, " got ", c)
                    corrupt.append((c, line))
                    break

    return corrupt


sum([points[c] for c, _ in corrupted(puzzle)])


# %%

# Part 2: complete strings

from functools import reduce
import statistics

values = {")": 1, "]": 2, "}": 3, ">": 4}


def autocomplete(puzzle):
    completed = []
    for line in puzzle:
        chunks = []
        for c in line:
            if c in mapping.keys():
                chunks.append(c)
            else:
                expected = mapping[chunks.pop()]
                if c != expected:
                    break
        else:
            autocomplete = [mapping[c] for c in chunks[::-1]]
            completed.append(autocomplete)

    return completed


scores = [
    reduce(lambda tot, c: tot * 5 + values[c], ac, 0)
    for ac in autocomplete(puzzle)
]
statistics.median(scores)


# %%
