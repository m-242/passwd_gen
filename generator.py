#!/usr/bin/python
# -*- coding: utf-8 -*-

# A simple password generator, outputs X words from a given dic, in camelCase.

import argparse
import random
import sys
import os


def args_parsing_and_checking():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--nb_words",
        help="The number of words you desire in your password",
        default=3,
        type=int,
    )
    parser.add_argument(
        "--dictionnary", help="The text file containing your dict, one word per line"
    )

    args = parser.parse_args()

    # check
    if not (args.dictionnary):
        sys.exit("[!] You must provide a dictionnary")

    if not (os.path.isfile(args.dictionnary)):
        sys.exit("[!] Invalid dictionnary provided")

    return args


def generate_and_print_passwd(x, d):
    with open(d, "r") as file:
        dictionnary = file.readlines()

        psswd = ""

        for i in range(x):
            psswd += random.choice(dictionnary).title()

            psswd = psswd.rstrip()  # remove any trailing line

        print(psswd)



if __name__ == "__main__":

    args = args_parsing_and_checking()

    generate_and_print_passwd(args.nb_words, args.dictionnary)

    sys.exit()
