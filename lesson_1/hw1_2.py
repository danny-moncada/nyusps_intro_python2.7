#!/usr/bin/env python

"""
	hw1_2.py -- tip calculator: write a restaurant bill calculator
	author: Danny Moncada
"""
bill_amt = raw_input('Please enter the total bill amount:  ')

party = raw_input('Please enter the number in your party:  ')

tip = raw_input('Please enter the desired tip percentage (for example, "20" for 20%):  ')

bill_int = int(bill_amt)
party_int = int(party)
tip_flt = float(tip)

tip_applied = bill_int * (tip_flt / 100)
total_bill = bill_int + tip_applied

split_check = round((total_bill / party_int), 2)

print "A " + str(tip_flt) + "% tip" + "($" + str(tip_applied) + ") was added to the bill, for a total of $" + str(total_bill)
print "With " + party + " in your party, each person must pay $" + str(split_check)
