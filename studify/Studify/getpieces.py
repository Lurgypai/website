#!/bin/python3

import json

def getpieces():
    with open('Studify/pieces.json', 'r') as pieces_file:
        ret = json.loads(pieces_file.read())
        pieces_file.close()
        return ret
