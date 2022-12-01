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

puzzle = [l.strip() for l in puzzle]

# %%

# Part 1: count unique length values in ouput of puzzle
def part1(puzzle):
    uniquelengths = set([2, 3, 4, 7])
    output = [l.split(" | ")[1].split() for l in puzzle]
    counts = [len([x for x in l if len(x) in uniquelengths]) for l in output]
    return sum(counts)

part1(puzzle)

# %%

# Part 2: guess mapping for digits

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

# %%

def map_input(input: List[str]) -> Dict[int, str]:
    """
    Given a list of possible values for all ten digits, guess which value
    corresponds to which digit by comparing common values in mappings.

    Parameters
    ----------
    input : List[str]
        the input digit values

    Returns
    -------
    Dict[int, str]
        the guessed mapping for each digit
    """
    mapping = {}
    i = 0
    while len(mapping) < 10:
        digit = input[i]
        if digit not in mapping.values():
            candidates = {
                k: digit
                for k, v in digits.items()
                if len(v) == len(digit) and k not in mapping
            }
            if len(candidates) == 1:
                mapping.update(candidates)
            else:
                valid_candidates = {
                    k: v
                    for k, v in candidates.items()
                    if all(
                        [
                            len(set(v) & set(y))
                            == len(set(digits[k]) & set(digits[x]))
                            for x, y in mapping.items()
                        ]
                    )
                }
                if len(valid_candidates) == 1:
                    mapping.update(valid_candidates)
        i = (i + 1) % 10
    return mapping

# %%
input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
input = input.split()
map_input(input)

# %%

def get_ouput(line: str) -> int:
    """
    Given an input line, guess the mapping from the input, then use it
    to find out the output value

    Parameters
    ----------
    line : str
        input puzzle line

    Returns
    -------
    int
        the output value
    """

    input, output = line.split(" | ")
    mapping = map_input(input.strip().split())

    value = ""
    for digit in output.strip().split():
        for k, v in mapping.items():
            if set(v) == set(digit):
                value += str(k)
    
    return int(value)

# %%

# output should be 5353
line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
get_ouput(line)

# %%

# solve puzzle
values = [get_ouput(line) for line in puzzle]
sum(values)
# %%
