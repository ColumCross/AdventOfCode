#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


input_file = "test.txt" if sys.argv[1] == 1 else "input.txt"

with open(input_file, "r") as f:
    input_values = [n for n in f.read().splitlines()]

# ------------------ #
