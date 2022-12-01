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

draws = [int(i) for i in inputs[0].strip().split(",")]
board = []
boards = []
for line in inputs[2:]:
    if line.strip() != "":
        board.append([int(i) for i in line.strip().split()])
    else:
        boards.append(np.array(board))
        board = []
boards.append(np.array(board))

print(draws)
print(boards)


# %%


def solve(draws, boards):
    masks = [b < 0 for b in boards]
    for d in draws:
        masks = [m | (b == d) for m, b in zip(masks, boards)]

        winner = None
        for i, m in enumerate(masks):
            if (m.astype(int).sum(axis=0) == 5).any() or (
                m.astype(int).sum(axis=1) == 5
            ).any():
                winner = i
                break

        if winner is not None:
            return boards[winner], masks[winner], d


b, m, d = solve(draws, boards)

total = d * b[~m].sum()
print("Total ", total)


# %%


def winner(m):
    return (m.astype(int).sum(axis=0) == 5).any() or (
        m.astype(int).sum(axis=1) == 5
    ).any()


def last_winner(draws, boards):
    masks = [b < 0 for b in boards]
    winner_draws = []
    winners = []
    print(f"Starting with {len(masks)}")
    for d in draws:
        print("Drawing", d)
        masks = [m | (b == d) for m, b in zip(masks, boards)]

        new_winners = [(m, b) for m, b in zip(masks, boards) if winner(m)]
        boards = [b for m, b in zip(masks, boards) if not winner(m)]
        masks = [m for m in masks if not winner(m)]
        if len(new_winners) > 0:
            print(f"Adding {new_winners} for {d}")
            winners.extend(new_winners)
            winner_draws.append(d)
            print(f"Now have {len(masks)} left")

    return winners, winner_draws

winners, winner_draws = last_winner(draws, boards)
d = winner_draws[-1]
m, b = winners[-1]

print(b, m, d)

total = d * b[~m].sum()
print("Total ", total)
# %%

# %%

x = [1, 2, 3]

x.extend([6, 7, 8])
x.append("a")
x

# %%
