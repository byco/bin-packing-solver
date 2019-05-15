# Name: Becky Chao
# Class: CS325
# Assigmnent: HW8
# Date: 26 November 2018

# Description: This program uses three greedy approximation algorithms to solve a 
# bin packing problem: how to fit items into bins with an alloted weight? Reading
# a source file provided by the user, the program will output how many bins should
# be used to store the items listed using first-fit, first-fit-decreasing, and best
# fit algorithms.

from __future__ import print_function

class Bin:
	def __init__(s):
		s.list = []

	#add new item weight to bin list
	def addItem(s, item):
		s.list.append(item)

	#shows current weight of bin
	def binWeight(s):
		total = 0

		for i in s.list:
			total += i

		return total

def firstFit(weight, items, capacity):
	binSpace = []
	# start with at least 1 bin
	binSpace.append(Bin())

	#go through all items to insert into bins
	for i in range(items):
		binNeeded = True

		#check which bin is most appropriate for this item
		for j in binSpace:
			# if current item can be put into bin, then add
			if j.binWeight() + weight[i] <= capacity:
				j.addItem(weight[i])
				binNeeded = False
				break

		# if item can't be put into an existing bin, start new bin and add item
		if binNeeded == True:
			newBin = Bin()
			newBin.addItem(weight[i])
			binSpace.append(newBin)		

	# return the number of bins used
	return len(binSpace)

# sort used for first fit decreasing greedy approximation algorithm
def timSort(array):
	temp = sorted(array, reverse=True)
	
	# copy newly sorted descending array from temp to original
	for i in range(len(array)):
		array[i] = temp[i]

def bestFit(weight, items, capacity):
	binSpace = []
	newBin = Bin()
	binSpace.append(newBin)

	# find the bin with the smallest space and see if item fits
	# default smallest space is higher than the actual capacity - should be changed as program runs
	for i in range(items):
		itemAdded = False
		smallestSpace = capacity + 1
		smallestIndex = 0

		# consider each binspace and find the smallest space available for item being evaluated
		for j in binSpace:
			if capacity - j.binWeight() < smallestSpace and j.binWeight() + weight[i] <= capacity:
				smallestSpace = capacity - j.binWeight() - weight[i]
				smallestIndex = j

		# add item to smallest possible space from bin options
		for j in binSpace:
			if j == smallestIndex:
				j.addItem(weight[i])
				itemAdded = True

		# if item cannot be added to any current bins, create a new bin and add item
		if itemAdded == False:
			newBin = Bin()
			newBin.addItem(weight[i])
			binSpace.append(newBin)

	# PRINT OUT ARRAY FOR TESTING
	#for j in binSpace:
		#print j.binWeight()
	return len(binSpace)			

with open('bin.txt') as file:
	while True:
		ch1 = file.readline()

		if ch1 != '':
			try:	
				cases = int(ch1)
				#print cases

				for case in range(cases):
					print("Test Case",case + 1, end=' ')
					ch2 = file.readline()
					capacity = int(ch2)
					#print capacity

					ch3 = file.readline()
					items = int(ch3)
					#print items

					itemArray = []

					ch4 = file.readline()

					counted = 0

					for i in range(items):
						j = 0
						while counted < items and j < len(ch4):
							itemW = ''

							while j < len(ch4) and ch4[j].isdigit():
								itemW += ch4[j]
								j += 1


							if itemW != ' ' and itemW != '' and counted < items:
								itemNum = int(itemW)
								itemArray.append(itemNum)
								counted += 1
							
							j += 1		
					
					temp = []
					for y in range(len(itemArray)):
						temp.append(itemArray[y])

					print("First Fit:", firstFit(itemArray,items,capacity), end=', ')
					timSort(temp)
					print("First Fit Decreasing:", firstFit(temp,items,capacity), end=', ')
					print("Best Fit:", bestFit(itemArray,items,capacity))			

			except ValueError:
				break



#TESTING
#itemsWeight = [3,8,2,7]
#print(firstFit(itemsWeight, 4, 10))

#itemsWeight = [3,8,2,7]
#timSort(itemsWeight)
#print(firstFit(itemsWeight, 4, 10))

#itemsWeight = [5, 10, 2, 5, 4, 4]
#timSort(itemsWeight)
#print(firstFit(itemsWeight, 6, 10))

#itemsWeight = [3,8,2,7]
#print(bestFit(itemsWeight,4,10))