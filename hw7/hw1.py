"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections import defaultdict
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


counter = defaultdict(int)


def find_occurrences(tree: dict, element: Any) -> int:

    if isinstance(tree, (list, tuple, set)):
        for val in tree:
            if val == element:
                counter[element] += 1

            find_occurrences(val, element)

    elif isinstance(tree, dict):
        for key, val in tree.items():
            if element == val:
                counter[element] += val.count(element)
            find_occurrences(val, element)

    return counter[element]


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
