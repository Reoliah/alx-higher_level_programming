#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if sentence == "":
            sentence[0] = "None"
        return (len(sentence), sentence[0])
