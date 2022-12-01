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

# Day 16

# %%

from typing import Dict, List
import pandas as pd
import numpy as np
from collections import Counter, defaultdict

# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

puzzle = puzzle[0].strip()


# %%

# Part 1


def hex_to_bits(hex_input):
    num_of_bits = 4 * len(hex_input)
    return bin(int(hex_input, 16))[2:].zfill(num_of_bits)


def parse_packet(bits_input):
    version = int(bits_input[:3], 2)
    type_ = int(bits_input[3:6], 2)
    if type_ == 4:
        value, to_parse = parse_literal_value(bits_input[6:])
        return version, type_, value, to_parse
    else:
        versions, value, to_parse = parse_operator(bits_input[6:], parse_packet)
        return [version] + versions, type_, value, to_parse


def parse_literal_value(bits_input):
    i = 0
    value = ""
    while bits_input[i] == "1":
        value += bits_input[i + 1 : i + 1 + 4]
        i += 5
    value += bits_input[i + 1 : i + 1 + 4]
    return int(value, 2), bits_input[i + 1 + 4 :]


def parse_operator(bits_input, parse_packet_func):
    type_id = bits_input[0]
    if type_id == "0":
        return parse_operator_type_0(bits_input[1:], parse_packet_func)
    else:
        return parse_operator_type_1(bits_input[1:], parse_packet_func)


def parse_operator_type_0(bits_input, parse_packet_func):
    total_length = int(bits_input[:15], 2)
    to_parse = bits_input[15:]
    current_length = len(to_parse)
    values = []
    versions = []
    while current_length - len(to_parse) < total_length:
        version, type_, value, to_parse = parse_packet_func(to_parse)
        if isinstance(value, list):
            values.extend(value)
        else:
            values.append(value)
        if isinstance(version, list):
            versions.extend(version)
        else:
            versions.append(version)
    return versions, values, to_parse

def parse_operator_type_1(bits_input, parse_packet_func):
    num_of_subpackets = int(bits_input[:11], 2)
    to_parse = bits_input[11:]
    values = []
    versions = []
    for i in range(num_of_subpackets):
        version, type_, value, to_parse = parse_packet_func(to_parse)
        if isinstance(value, list):
            values.extend(value)
        else:
            values.append(value)
        if isinstance(version, list):
            versions.extend(version)
        else:
            versions.append(version)
    return versions, values, to_parse



# %%

bits_input = hex_to_bits(puzzle)
output = parse_packet(bits_input)
print(output, sum(output[0]))

# %%
bits_input = hex_to_bits("38006F45291200")
print(bits_input)
parse_packet(bits_input)

# %%
bits_input = hex_to_bits("A0016C880162017C3686B18A3D4780")
output = parse_packet(bits_input)
print(output, sum(output[0]))


# %%

# Part 2: compute value based on type

def parse_packet_2(bits_input):
    version = int(bits_input[:3], 2)
    type_ = int(bits_input[3:6], 2)
    if type_ == 4:
        value, to_parse = parse_literal_value(bits_input[6:])
        return version, type_, value, to_parse
    else:
        versions, values, to_parse = parse_operator(bits_input[6:], parse_packet_2)
        if type_ == 0:
            value = sum(values)
        elif type_ == 1:
            value = np.prod(values)
        elif type_ == 2:
            value = min(values)
        elif type_ == 3:
            value = max(values)
        elif type_ == 5:
            value = int(values[0] > values[1])
        elif type_ == 6:
            value = int(values[0] < values[1])
        elif type_ == 7:
            value = int(values[0] == values[1])
        return [version] + versions, type_, value, to_parse
        


# %%

bits_input = hex_to_bits(puzzle)
output = parse_packet_2(bits_input)
print(output)
# %%
