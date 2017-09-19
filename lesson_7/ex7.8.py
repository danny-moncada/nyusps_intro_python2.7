#!/usr/bin/env python

words = [ 'Hello', 'my', 'dear', 'the', 'heart', 'is', 'a', 'child.' ]

three_letter = [ i.upper().rstrip('.') for i in words if len(i) > 3]

print three_letter