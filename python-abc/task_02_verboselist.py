#!/usr/bin/env python3
"""
Module for VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Add an item and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extend the list and print notification."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove an item and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
