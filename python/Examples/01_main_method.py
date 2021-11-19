#!/usr/bin/env python3
# Demo of main method

import platform

def main():
    message()

def message():
    print("Py version {}".format(platform.python_version()))

if __name__ == '__main__' : main()
