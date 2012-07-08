#!/usr/bin/python

from anecdotally import Anecdotally
import pprint as pp


def main():
    myapi = Anecdotally("4f947b4ebd8ad50e49000000")

    pp.pprint(myapi.programs.find_one())
    print "_"*80
    pp.pprint(myapi.anecdotes.find_one())
    print "_"*80


if __name__ == '__main__':
    main()