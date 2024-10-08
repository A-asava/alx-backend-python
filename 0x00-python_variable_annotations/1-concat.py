#!/usr/bin/env python3
"""Concatenate strings"""


def concat(str1: str, str2: str) -> str:
    """type-annotated function concat that
        take a string str1 and a string str2 as
        arguments and returns a concatenated string
    """

    return str("{}{}".format(str1, str2))
