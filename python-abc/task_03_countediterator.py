#!/usr/bin/env python3
"""
Module for CountedIterator class.
"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.counter

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Return the iterator object itself."""
        return self
