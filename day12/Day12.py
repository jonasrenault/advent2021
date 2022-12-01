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

# Day 12

# %%

from typing import Dict, List
import pandas as pd
import numpy as np
from collections import defaultdict

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

paths = defaultdict(set)
for l in puzzle:
    s, e = l.strip().split("-")
    paths[s].add(e)
    paths[e].add(s)

# %%

# Part 1: find paths from start to end


def paths_from(point, visited):
    if point == "end":
        return ["end"]

    if point.islower() and point in visited:
        return []

    results = []
    for exit in paths[point]:
        results.extend(
            [point + ", " + x for x in paths_from(exit, visited | {point})]
        )
    return results


possible_paths = paths_from("start", set())
print(possible_paths)
print(len(possible_paths))


# %%

# Part 2: visit one small cave twice


def paths_from_2(point, visited, small_cave):
    if point == "end":
        return ["end"]

    if point.islower() and point in visited:
        return []

    results = []
    for exit in paths[point]:
        results.extend(
            [
                point + ", " + x
                for x in paths_from_2(exit, visited | {point}, small_cave)
            ]
        )
        if point.islower() and len(small_cave) == 0 and point != "start":
            results.extend(
                [
                    point + ", " + x
                    for x in paths_from_2(exit, visited, {point})
                ]
            )
    return list(set(results))


possible_paths = paths_from_2("start", set(), set())
print(len(possible_paths))

# %%
# %%


# %%
