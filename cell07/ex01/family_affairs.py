#!/usr/bin/env python3

def find_the_redheads(family):
    temp = dict(filter(lambda item: item[1] == "red", family.items()))
    redhead = []
    for name in temp:
        redhead.append(name)
    return redhead

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
