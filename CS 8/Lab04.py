# Student(s): (Ning Qi & Shravan Shenoy)


def notStringContainingR(word):
    '''
    - Return True when word is a string that contains no letter 'r' (or 'R')
    - It should work both for lower and upper case.
    - When word isn't a string or is an empty string (""), return True
    (because it is not a string contaning an R).
    - You can check if the word value is a string with type(word) == str 
    '''
    if type(word)!=str:
        return True
    elif len(word)==0:
        return True
    else:
        if "r" in word:
            return False
        elif"R" in word:
            return False
        else:
            return True


def hasVowel(word):
    '''
    - Return True when word is a string that contains a vowel
    (a,e,i,o,u,A,E,I,O,U).
    - It should work for both lower and upper case vowels.
    - When word doesn't have a vowel, return False. Return True otherwise.
    - If word isn't a string, return False (because it is not a string
    containing a vowel).
    - Hint: recall the boolean operator "in" and use that when
    checking if a character is a vowel.
    '''
    if type(word)!=str:
        return False
    else:
        if len(word)==0:
            return False
        else:
            for c in word:
                if c in "aeiouAEIOU":
                    return True
            return False


def isNumber(item):
    '''
    - Return True if item is of type int or type float, otherwise return
    False.
    - You can check if item is an int with type(item) == int, and a float
    with type(item) == float
    '''
    if type(item)==float:
        return True
    elif type(item)==int:
        return True
    else:
        return False


def onlyContainsStrings(theList):
    '''
    - Returns True if theList is a list containing only strings.
    - The parameter theList can be anything.
    - An empty list should return False since it doesn't contain a string.
    - If theList is not a list type, return False since theList is not a list
    containing only strings.
    - Note: you can check if theList is a list with type(theList) == list
    '''
    if type(theList)==list:
        if len(theList)==0:
            return False
        else:
            for i in theList:
                if type(i)!=str:
                    return False
            return True
    else:
        return False

def contains(x, theList):
    '''
    - Returns True if the value of x is in theList.
    - The parameters x and theList can be anything.
    - An emptyList should return False since it doesn't contain any values
    (including x).
    - If theList is not a list type, return False since x is not in a list.
    '''
    if type(theList)!=list:
        return False
    else:
        if len(theList)==0:
            return False
        else:
            for a in theList:
                if x==a:
                    return True
            return False


def abbreviate(word):
    '''
    - Returns a string with (up to) the first three characters of
    the string word.
    - The value of word can be anything.
    - If word is not a string, return an empty string ("").
    '''
    if type(word)!=str:
        return ""
    else:
        return word[0:3]


def hasMultiplesOf(x, listOfNums):
    '''
    - Returns True if ALL items in listOfNums are multiples of x.
    - theList can have elements of any type.
    - If listOfNums is not a list type, return False.
    - If listOfNums is empty, return False since no items are a multiple
    of x
    - If listOfNums contains an element that is not a number (int or
    float), return False.
    '''
    if type(x)==int or type(x)==float:
        if type(listOfNums)!=list:
            return False
        else:
            if len(listOfNums)==0:
                return False
            else:
                for i in listOfNums:
                    if i%x!=0:
                        return False
                return True
    else:
        return False
    

def countEvens(listOfInts):
    '''
    - Returns an integer value representing the number of even numbers that
    exist in listOfInts.
    - Return 0 if listOfInts is not a list type or if no even number exists
    in listOfInts.
    - Note: elements in listOfInts can contain any data type.
    '''
    if type(listOfInts)!=list:
        return 0
    else:
        count=0
        for i in listOfInts:
            if type(i)==int:
                if i%2==0:
                    count+=1
        return count


def computeGrade(percentage):
    '''
    - Return the corresponding letter grade string based on the value of
    percentage using the following scale:
    [100 - 90]: 'A'
    (90 - 80] : 'B'
    (80 - 70] : 'C'
    (70 - 60] : 'D'
    (60 - 0]  : 'F'
    - If percentage is not a number type (int or float) OR if percentage is
    outside the range of [100 - 0], return an empty string ("").
    '''
    if type(percentage)==int or type(percentage)==float:
        if percentage<0 or percentage>100:
            return ""
        else:
            if percentage>=90 and percentage<=100:
                return "A"
            elif percentage>=80 and percentage<90:
                return "B"
            elif percentage>=70 and percentage<80:
                return "C"
            elif percentage>=60 and percentage<70:
                return "D"
            else:
                return "F"
    else:
        return ""


# Definition of a Book namedtuple object used for the
# following function below.
from collections import namedtuple
Book = namedtuple("Book", "title author price")
def expensiveBooks(price, listOfBooks):
    '''
    - Returns a list of book titles of Books that are greater or equal to
    the value price.
    - If price is not a number type, then return an empty list ([]).
    - If listOfBooks is not a list type, then return an empty list ([]).
    - Elements in listOfBooks may contain multiple types (not necessarily
    Books). You can check if an element is a Book object with
    type(value) == Book. You can "skip" an element that's not a Book and
    continue checking other elements in listOfBooks.
    - You can assume Book objects are constructed correctly (i.e. title
    and author are strings, and book prices are either an int or float).
    - Note: You must obtain values of a book object using the name of
    the object's attributes (.title, .author, .price) instead of indexing
    them for full credit (as discussed in lecture). 
    - Hint: Think of appending book titles to a list (recall .append) when
    the cost of the book is greater than or equal to the value price, and 
    returning the list of accumulated book titles.
    '''
    if type(price)==int or type(price)==float:
        if type(listOfBooks)!=list:
            return []
        else:
            mylist=[]
            i=0
            for i in range(len(listOfBooks)):
                if listOfBooks[i].price>=price:
                    mylist.append(listOfBooks[i].title)
                    i=i+1                  
            return mylist
    else:
        return []
    



