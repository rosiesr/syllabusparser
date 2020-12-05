"""
syllabus parser file
author: rad 
.txt files only

don't ruin this file rosie please
"""

import json

f = open("CS 250 Syllabus.txt", "r")

def parse(file):
    out = {}
    for line in file:
        if "-" in str(line):
            linelist = line.split(" - ")
            work = linelist[0]
            date = linelist[1]
            out.update({work:date[:len(date) - 1]})
    return json.dumps(out)

if __name__ == "__main__":
    print(parse(f))

