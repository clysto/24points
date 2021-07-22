#!/usr/bin/env python3


from sys import argv
from typing import List
from copy import deepcopy


class Node:
    def __init__(self, value, left, right, operation) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.operation = operation

    def __add__(self, other):
        node = Node(self.value + other.value, left=self, right=other, operation="+")
        return node

    def __sub__(self, other):
        node = Node(self.value - other.value, left=self, right=other, operation="-")
        return node

    def __mul__(self, other):
        node = Node(self.value * other.value, left=self, right=other, operation="*")
        return node

    def __floordiv__(self, other):
        node = Node(self.value // other.value, left=self, right=other, operation="/")
        return node

    def to_rpn(self):
        ret = []
        if self.left:
            ret += self.left.to_rpn()
        if self.right:
            ret += self.right.to_rpn()
        if self.operation is None:
            ret += [self.value]
        else:
            ret += [self.operation]
        return ret


def solve(arr: List):
    arr_len = len(arr)

    if arr_len == 1:
        if arr[0].value == 24:
            node = arr[0]
            print(node.to_rpn())
        return

    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            new_arr = []
            for x in range(len(arr)):
                if x != i and x != j:
                    new_arr.append(deepcopy(arr[x]))

            solve(new_arr + [arr[i] + arr[j]])
            solve(new_arr + [arr[i] - arr[j]])
            solve(new_arr + [arr[j] - arr[i]])
            solve(new_arr + [arr[i] * arr[j]])

            if arr[j].value != 0:
                solve(new_arr + [arr[i] // arr[j]])

            if arr[i].value != 0:
                solve(new_arr + [arr[j] // arr[i]])


if __name__ == "__main__":
    solve(
        [
            Node(int(argv[1]), None, None, None),
            Node(int(argv[2]), None, None, None),
            Node(int(argv[3]), None, None, None),
            Node(int(argv[4]), None, None, None),
        ]
    )
