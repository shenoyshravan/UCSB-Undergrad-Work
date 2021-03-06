# Student(s): Ning Qi, Shravan Shenoy
# Make sure to read the comments for each function. 

def createWordList(filename):
  '''
  Reads in the filename and creates a list L which contains all the words. 
  You must remove the newline character ('\n') at the end of each word.  

  :param filename: the string which represents the filename you are reading from.
  :return: A list of strings  
  '''
  file=open(filename,'r')
  line=file.readlines()
  a=[]
  for i in line:
      b=i.strip('\n')
      a.append(b)
  file.close()
  return a


def canWeMakeIt(myWord, myLetters):
  '''
  Takes in a word and a string of letters and checks whether the word can be made with those letters.  

  :param myWord: the string we are checking.
  :param myLetters: a string of letters we can use to build a string. 
  :return: A bool whether the string can be made or not.  
  '''
  a=[]
  for i in myLetters:
    a.append(i)
  for b in myWord:
    if b in a:
      a.remove(b)
    else:
      return False
  return True

def getWordPoints(myWord, letterPoints):
  '''
  Returns the total points of a given word. 

  :param myWord: the string you want to calculate points for
  :param LetterPoints: a dictionary of (letter, value) pairs which gives the point value of each letter
  :return: The total point value of the word.   
  '''
  ttlpoints=0
  for i in myWord:
    if type(i)==str:
      if i in letterPoints:
        a=letterPoints[i]
        ttlpoints+=a
      else:
        next
    else:
      return 0
  return ttlpoints


def outputWordPointPairs(pointWordList, filename, toFile):
    '''
    Outputs the contents of pointWordList in a specified format to a file (see lab instructions).
    
    :param pointWordList: a list of tuples to print or output to a file, each tuple 
    contains a (pointValue, word) pair
    :param filename: a string that you will name the file with if toFile is True
    Your function should add the .txt extension to the filename before creating it.
    :param toFile: a boolean to decide whether I want to print to file or not. If True then output to file else output to terminal.
    :return: None
    '''
    file=str(filename)+".txt"
    outfile=open(file,'w')
    for a in pointWordList:
        if toFile==False:
            print('{1:{x}}{0:}'.format(a[0],a[1],x=len(a)+4))
        else:
            outfile.write('{1:{x}}{0:}'.format(a[0],a[1],x=len(a)+4)+'\n')
                
    outfile.close()


def scrabbleWords(myLetters):
  '''
  A function which takes in a string of letters and shows what words can be constructed from it.
  It should use the helper functions defined above to do so. 

  :param myLetters: a string of letters we are using. 
  :return: None
  '''
  wordlist=createWordList('wordlist.txt')
  myWords=[]
  for word in wordlist:
    if canWeMakeIt(word,myLetters)==True:
      myWords.append(word)
  letterPoints={'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5, 'l':1, 'm':3,
                'n':1, 'o':1, 'p':3, 'q':10,'r':1, 's':1,'t':1, 'u':1, 'v':4, 'w':4, 'x':8,'y':4, 'z':10}
  pointWordList=[]
  for points in myWords:
    total=getWordPoints(points,letterPoints)
    pointWordList.append((total,points))
  pointWordList.sort()
  pointWordList.reverse()
  outputWordPointPairs(pointWordList, myLetters, False)
  outputWordPointPairs(pointWordList, myLetters, True)

if __name__=="__main__":
  print("Manual test cases can be done here and/or in IDLE's command line")
  # Manual test cases...

