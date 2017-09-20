"""
    hw9.1.py -- filelib.py module with three functions
    author: Danny Moncada
"""

def getlines(filename, newlines=False):
    mylist = []
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        if newlines == True:
            line = line
        else:
            line = line.rstrip()
        mylist.append(line)
    file.close()
    return mylist

def gettext(filename):
    file = open(filename)
    text = file.read()
    file.close()
    return text

def getfields(filename, delimiter=None):
    mylist = []
    file = open(filename)
    fields = file.readlines()
    for line in fields:
        line = line.rstrip()
        if delimiter == None:
            line = line.split()
        elif delimiter not in line:
            raise ValueError('that delimiter was not found in the file!')
        else:
            line = line.split(delimiter)
        mylist.append(line)
    file.close()
    return mylist
