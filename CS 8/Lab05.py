# lab05.py

# Student(s): Shravan Sharath Shenoy , Ning Qi

# This file contains several incomplete function definitions with stub
# values. lab05_tests.py have tests to check if the functions are correct.
# Your assignment is to complete each function according to the
# functions' descriptions.
#
# Once you complete a function, you can run pytest on the tests defined
# in lab05_tests.py to see if your functions are working correctly.
#
# If you use techniques that
#    we did not learn in class, you will not get credit.

def totalCharacters(listOfStr):
        a=0
        if type(listOfStr) != list:
                return -1
        for n in range(len(listOfStr)):
                if type(listOfStr[n]) != str:
                       return -1
        for n in range(len(listOfStr)):
                listOfStr[n]
                for i in range(len(listOfStr[n])):
                       a+=1
        return a


def factorial(n):
    if type(n) != type(1):
        return -1
    if n == 0:
        return 1
    for i in range(n):
        if n in range(1,100) and type(n)== int:
            p=n-1
            return n*(p)*(p-1)*(p-2)
    else:
        return -1
    
    
    '''
    (10 points)
    Function that takes an integer and returns the value of n factorial
    (n!).
    - If n is negative or not an int type, return the sentinal value
    of -1
    - Your solution should use a for loop and not use functions from
    python's math module.
    - If you do NOT use a for loop (or if you use techniques, like recursion, that
    we did not learn in class), you will not get credit for this part.
    - Hint: note that 0! = 1. You may have to adjust your range in your
    for loop to account for this.
    '''


def maxNum(listOfNums):
    MaxValue = listOfNums[0]
    if listOfNums == []:
        return None
    if type(listOfNums) != list:
        return None
    for z in range(len(listOfNums)):
        if type(listOfNums[z]) == int or type(listOfNums[z]) == float:
            continue
        elif type(listOfNums[z]) == str:
            return None
    for n in range(len(listOfNums)):
    	if listOfNums[n] > MaxValue:
    		MaxValue = listOfNums[n]
    return MaxValue

    '''
    (20 points)
    Function that takes in a list of numbers (listOfNums) and returns
    the maximum value in the list.
    - Returns the None type if listOfNums is not a list, listOfNums
    does not have elements in the list, or an element in listOfNums is
    not a numerical type (int or float).
        Note: This is an example of using python's None type as a
        sentinal value.
    - Your solution should use a for loop and not use the max() function.
    - If you do NOT use a for loop (or if you use techniques that
    we did not learn in class), you will not get credit for this part.
    - Hint: You can assign a default maxValue variable as the 1st element
    of listOfNums if valid. You can then iterate through listOfNums and
    compare the current maxValue with each element in the list, updating
    maxValue if necessary.
    '''


def indexOf(value, listOfValues):
    if type(listOfValues) != list:
        return None
    if value not in listOfValues:
        return None
    n=0
    for i in range(len(listOfValues)):
        if listOfValues[i] == value:
            return i
    '''
    (20 points)
    Function that takes in a value (of any type) and a list of values
    containing any type (listOfValues). Returns the index in the list of
    the first match between value and an element in listOfValues.
    - Returns None if listOfValues is not a list type or if value is
    not present in the list
    '''

# Item namedtuple definition used for the next two functions
# Name is the name of an item, price is the price of an item in dollars, and
# purchased is the number of items sold.
from collections import namedtuple
Item = namedtuple("Item", "name price purchased")

i1 = Item('Eggs', 2.00, 2)
i2 = Item('Milk', 4.00, 0)
i3 = Item('Honey', 3.00, 3)
i4 = Item('Orange', 1.00, 0)

def unpopularItems(listOfItems):
    if type(listOfItems) == list:
        NewList = []
        for n in range(len(listOfItems)):
            if listOfItems[n].purchased == 0:
                NewList.append(listOfItems[n])
                n += 1
        return NewList
    else:
        return None
    
    '''
    (20 points)
    Function that takes in a list of Items. Returns a new list of items
    containing the items that had 0 purchases.
    - Note: We've seen something similar to this in the last lab. Think
    of using .append to add items to your resulting list when the amount
    purchased is 0.
    '''

def updatePrice(pricePercent, listOfItems):
    if type(listOfItems) == list:
        n = 0
        for n in range(len(listOfItems)):
            listOfItems[n] = listOfItems[n].name,((1.00+(pricePercent/100))*listOfItems[n].price),listOfItems[n].purchased
            n+=1
        return listOfItems
    else:
        return None
    
    '''
    (20 points)
    Function that takes a pricePercent value and a list of Items.
    Returns a list with updated Items in listOfItems with the original
    price changed by pricePercent.
        - For example, if the price of an item is $2.00 and pricePercent is 50, then
        the updated price is $3.00. If an item is $2.00 and pricePercent
        is -50, then the resulting price is $1.00.
    - Hint: Recall that namedtuples are IMMUTABLE types and we cannot
    simply change a namedtuple attribute. See the pdf slides for lecture 9 and 10 on how we can
    update namedtuple attributes using the ._replace method or
    constructing a new namedtuple object.
    '''

