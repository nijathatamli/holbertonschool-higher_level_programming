#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new = sorted(self)
        print(new)
