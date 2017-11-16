# From the book :
# How to Think Like a Computer Scientist - Learning with Python
# Green Tea Press
# Wellesley, Massachusetts
# 2nd edition, August 2008
# by Allen Downey, Jeffrey Elkner and Chris Meyers


import math, string, random, operator

def newLine():
    print()

def threeLines():
    newLine()
    newLine()
    newLine()

def printTwice(bruce):
    print (bruce, bruce)

def catTwice(part1, part2):
    cat = part1 + part2
    printTwice(cat)

def printParity(x):
    if x%2 == 0:
        print (x, "is even")
    else:
        print (x, "is odd")

def printLogarithm(x):
    if x <= 0:
        print ("Positive numbers only, please.")
        return
    result = math.log(x)
    print ("The log of x is", result)

# See below iteration instead of recursion solution
#def countdown(n):
#    if n == 0:
#        print ("Blastoff!")
#    else:
#        print (n)
#        countdown(n-1)

# See below iteration instead of recursion solution
#def nLines(n):
#    if n > 0:
#        print()
#        nLines(n-1)

def cycleArea(radius):
    return math.pi * radius**2

def absoluteValue(x):
    if x < 0:
        return -x
    else:
        return x

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    return math.sqrt(dsquared)

def hypotenuse(a,b):
    return math.sqrt(a**2+b**2)

def cycleArea2(xc, yc, xp, yp):
    return cycleArea(distance(xc, yc, xp, yp))

def slope(x1, y1, x2, y2):
    pass

def intercept(x1, y1, x2, y2):
    pass

def isDivisible(x, y):
    return x % y == 0

def isBetween(x, y, z):
    return y<=x<=z

def factorial (n):
    if not isinstance(n, int):
        print ("Factorial is only defined for integers.")
        return -1
    elif n < 0:
        print ("Factorial is only defined for positive integers.")
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def countdown(n):
    while n > 0:
        print (n)
        n = n-1
    print ("Blastoff!")

def nLines(n):
    while n>0:
        print()
        n-=1

def printMultiples(n, high):
    i = 1
    while i <= high:
        print (n*i, '\t', sep=' ', end='')
        i = i + 1
    print()

def printMultTable(high):
    i = 1
    while i <= high:
        printMultiples(i, i)
        i = i + 1

# Exercise 7.3.1
def reverseString(s):
	n=len(s)-1
	while n>=0:
		print(s[n])
		n-=1

# Exercise 7.3.2
def Make_Way_for_Ducklings():
    prefixes = "JKLMNOPQ"
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            suffix = 'uack'
        else:
            suffix = "ack"
        print (letter + suffix)

def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1

# Exercise 7.7
def find_modified(str, ch, start):
# solution with 'while'
#    index = start
#    while index < len(str):
#        if str[index] == ch:
#            return index
#        index = index + 1
#    return -1
# solution with 'for'
    index = start
    for letter in str[start:]:
        if letter == ch:
            return index
        index += 1
    return -1


# Exercise 7.8.1
def countLetters(word,letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    print (count)


# Exercise 7.8.2
def countLetters_modified(word,letter):
    count=0
    a = find_modified(word,letter,0)
    while a > -1:
        count+=1
        a = find_modified(word,letter,a+1)
    print(count)

def isLower_v1(ch):
    return string.find(string.lowercase, ch) != -1

def isLower_v2(ch):
    return ch in string.lowercase

def isLower_v3(ch):
    return 'a' <= ch <= 'z'

# Exercise 8.3
def lengthOfElements():
    mylist=['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
    i=0
    while i < len(mylist):
        if isinstance(mylist[i], int):
            print('Member', mylist[i], 'is integer and has no length')
        else:
            print('Member', mylist[i], 'has length', len(mylist[i]))
        i += 1

# Exercise 9.4.1
def rand_lo_hi(lo,hi):
    pass

# Exercise 9.4.2
def rand_lo_hi_int(lo,hi):
    pass

def randomList(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s

def inBucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count += 1
    return count

def allBuckets(alist, numBuckets):
    buckets = [0] * numBuckets
    bucketWidth = 1.0 / numBuckets
    for i in range(numBuckets):
        low = i * bucketWidth
        high = low + bucketWidth
        buckets[i] = inBucket(alist, low, high)
    print (buckets)
    # Exercise 9.7 --> calculate standard deviation in all population, with lists
    m=1.0/numBuckets*sum(buckets)
    s=math.sqrt(sum(list(map(operator.pow, list(map(operator.sub, buckets, [m]*numBuckets)), [2]*numBuckets)))/numBuckets)
    print ("s=",s)

def allBuckets_v2(alist, numBuckets):
    buckets = [0] * numBuckets
    for i in alist:
        index = int(i * numBuckets)
        buckets[index] = buckets[index] + 1
    print (buckets)
    m=1.0/numBuckets*sum(buckets)
    s=math.sqrt(sum(list(map(operator.pow, list(map(operator.sub, buckets, [m]*numBuckets)), [2]*numBuckets)))/numBuckets)
    print ("s=",s)

# Exercise 9.8
def histogram(list, numBuckets):
    pass

def fibonacci_v2(n):
    previous = {0:1, 1:1}
    def fibonacci(n):
        if previous.has_key(n):
            return previous[n]
        else:
            newValue = fibonacci(n-1) + fibonacci(n-2)
            previous[n] = newValue
            return newValue

# Erases file comments if they start from the beginning
def filterFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.readline()
        if text == "":
            break
        if text[0] == '#':
            continue
        f2.write(text)
    f1.close()
    f2.close()
    return

def exists(filename):
    try:
        f = open(filename)
        f.close()
        return True
    except IOError:
        return False

# Exercise 11.5
def inputNumber () :
    x = input ('Pick a number: ')
    try:
        if x == 17 :
            raise ValueError
        return x
    except ValueError:
        print('17 is a bad number')

# Exercise 12.2
class Point:
    pass

def check_point():
    p1=Point()
    print(p1) # <__main__.Point object at 0x7f53088f42e8>
    id(p1)    # 139994602619624 same as above

def printPoint(p):
	print ('(' + str(p.x) + ', ' + str(p.y) + ')')

# Exercise 12.3
def distance_v2(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# compare deep equality (instead of shallow equality which is compares only references of objects
def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

def compare_equality(p1, p2):
    if p1 is p2:
        print('Points have shallow equality (they have the same reference)')
    if samePoint(p1, p2):
        print('Points have deep equality (their contents are the same)')

class Rectangle:
    pass

def newRectangle(width,height,x,y):
    box = Rectangle()
    box.width = width
    box.height = height
    box.corner = Point()
    box.corner.x = x
    box.corner.y = y

def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y - box.height/2.0
    return p

def growRect(box, dwidth, dheight) :
    box.width = box.width + dwidth
    box.height = box.height + dheight

# Exercise 12.7
def moveRect(box,dx,dy):
    box.corner.x += dx
    box.corner.y += dy

def growRect_v2(box, dwidth, dheight) :
    import copy
    newBox = copy.deepcopy(box)
    newBox.width = newBox.width + dwidth
    newBox.height
    return newBox

# Exercise 12.8
def moveRect_v2(box,dx,dy):
    import copy
    newBox = copy.deepcopy(box)
    newBox.corner.x += dx
    newBox.corner.y += dy
    return newBox

class Time:
    pass

def newTime(hours,minutes,seconds):
    time=Time()
    time.hours=hours
    time.minutes=minutes
    time.seconds=seconds
    return time

# Exercise 13.1
def printTime(timeObj):
    print('Time is ',str(timeObj.hours),':',str(timeObj.minutes),':',str(timeObj.seconds), sep='')

# Exercise 13.2
def after(t1,t2):
    if t1.hours > t2.hours:
        return True
    elif t1.hours == t2.hours:
        if t1.minutes > t2.minutes:
            return True
        elif t1.minutes == t2.minutes:
            if t1.seconds > t2.seconds:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Pure function
# It does not modify any of the objects passed to it as arguments and it has no
# side effects, such as displaying a value or getting user input.
def addTime(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    if sum.seconds >= 60:
        sum.seconds = sum.seconds - 60
        sum.minutes = sum.minutes + 1
    if sum.minutes >= 60:
        sum.minutes = sum.minutes - 60
        sum.hours = sum.hours + 1
    return sum

# Modifier function
# Modifies one or more of the objects it gets as arguments
def increment(time, seconds):
    time.seconds = time.seconds + seconds
    while time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1
    while time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours + 1

# Exercise 13.3.1, increment without loops
def increment_v2(time, seconds):
    secs = (time.seconds + seconds) % 60
    minutes = (time.seconds + seconds) // 60
    mins = (time.minutes + minutes) % 60
    hrs =  time.hours + (time.minutes + minutes) // 60
    time.seconds = secs
    time.minutes = mins
    time.hours = hrs

# Exercise 13.3.2a, increment as pure function
def increment_v3(time, seconds):
    import copy
    sum = copy.deepcopy(time)
    secs = (sum.seconds + seconds) % 60
    minutes = (sum.seconds + seconds) // 60
    mins = (sum.minutes + minutes) % 60
    hrs =  sum.hours + (sum.minutes + minutes) // 60
    sum.seconds = secs
    sum.minutes = mins
    sum.hours = hrs
    return sum

# Exercise 13.3.2b, function call to both upper versions
def increment_final(time, seconds, pure_or_modifier):
    if pure_or_modifier == 1:
        increment_v3(time, seconds)
    else:
        increment_v2(time, seconds)

def convertToSeconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    return seconds

def makeTime(seconds):
    time = Time()
    time.hours = seconds // 3600
    time.minutes = (seconds%3600) // 60
    time.seconds = seconds%60
    return time

def addTime_v2(t1, t2):
    seconds = convertToSeconds(t1) + convertToSeconds(t2)
    return makeTime(seconds)

# Exercise 13.5, rewrite increment_v3 with use of convertToSeconds() and makeTime()
def increment_v4(time, seconds):
    return makeTime(convertToSeconds(time) + seconds)

# Exercise 14.4 convert convertToSeconds() to method of class Time
# added printTime p.149, increment p.177, after p.178, __init__ p. 180
class Time:
    def printTime(self):
        print (str(self.hours) + ":" + \
        str(self.minutes) + ":" + \
        str(self.seconds))

    def increment(self, seconds):
        self.seconds = seconds + self.seconds
        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1
        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1

    def convertToSeconds(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

    def after(self, time2):
        if self.hour > time2.hour:
            return 1
        if self.hour < time2.hour:
            return 0
        if self.minute > time2.minute:
            return 1
        if self.minute < time2.minute:
            return 0
        if self.second > time2.second:
            return 1
        return 0

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def printTime(self):
        print('Time is ',str(self.hours),':',str(self.minutes),':',str(self.seconds), sep='')

# Exercise 14.5
def find_v2(str, ch, start = 0, end = 0):
    if end == 0:
        end = len(str)
    index = start
    for letter in str[start:end]:
        if letter == ch:
            return index
        index += 1
    return -1

# 14.7 Points revisited (p.181)
class  Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Exercise 14.8
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def reverse(self):
        self.x , self.y = self.y, self.x


# 14.9 Polymorphism (p.183)
def multadd (x, y, z):   # multadd(int, int,int) --> int | multadd(int, point,
    return x * y + z     # point) --> point | multadd (point, point, int) --> int

def frontAndBack(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print (str(front) + str(back))

# Fundamental rule of polymorphism:
# If all of the operations inside the function can be applied to
# the type, the function can be applied to the type.

# ...so in class Point we add reverse(), in order for frontAndBack() to work for
# Points. See reverse in class Point upper

# 15 Sets of objects
# 15.1 Composition
# 15.2 Card object

class Card:
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rankList[self.rank] + " of " + self.suitList[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... it's a tie
        return 0

# Exercise 15.4, modify _cmp_ so thay Aces are higer than Kings
#    def __cmp__(self, other):
#        if self.suit > other.suit: return 1
#        if self.suit < other.suit: return -1
#        if self.rank == 1:
#            selfrank = 14;
#        else:
#            selfrank = self.rank
#        if other.rank == 1:
#            otherrank = 14;
#        else:
#            otherrank = other.rank
#        if selfrank > otherrank: return 1
#        if selfrank < otherrank: return -1
#        return 0

# 15.5 Decks --- the append method

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def printDeck(self):
        for card in self.cards:
            print (card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " "*i + str(self.cards[i]) + "\n"
        return s

# 15.7 Shuffling the deck --- the randrange function
    def shuffle(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def popCard(self):
        return self.cards.pop()

    def isEmpty(self):
        return (len(self.cards) == 0)

    def deal(self, hands, nCards=999):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty(): break   # break if out of cards
            card = self.popCard()      # take the top card
            hand = hands[i % nHands]   # whose turn is next?
            hand.addCard(card)         # add the card to the hand

class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def addCard(self,card) :
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.isEmpty():
            return s + " is empty\n"
        else:
            return s + " contains\n" + Deck.__str__(self)

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):
    def removeMatches(self):
        count = 0
        originalCards = self.cards[:]
        for card in originalCards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print ("Hand %s: %s matches %s" % (self.name,card,match))
                count = count + 1
        return count

class OldMaidGame(CardGame):

    def play(self, names):
        # remove Queen of Clubs
        self.deck.removeCard(Card(0,12))

        # make a hand for each player
        self.hands = []
        for name in names :
            self.hands.append(OldMaidHand(name))

        # deal the cards
        self.deck.deal(self.hands)
        print ("---------- Cards have been dealt")
        self.printHands()

        # remove initial matches
        matches = self.removeAllMatches()
        print ("---------- Matches discarded, play begins")
        self.printHands()

        # play until all 50 cards are matched
        turn = 0
        numHands = len(self.hands)
        while matches < 25:
            matches = matches + self.playOneTurn(turn)
            turn = (turn + 1) % numHands

        print ("---------- Game is Over")
        self.printHands()

    def removeAllMatches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.removeMatches()
        return count

# Exercise 16.7 --- write printHands()
    def printHands(self):
        for hand in self.hands:
            print(hand)

    def playOneTurn(self, i):
        if self.hands[i].isEmpty():
            return 0
        neighbor = self.findNeighbor(i)
        pickedCard = self.hands[neighbor].popCard()
        self.hands[i].addCard(pickedCard)
        print ("Hand", self.hands[i].name, "picked", pickedCard)
        count = self.hands[i].removeMatches()
        self.hands[i].shuffle()
        return count

    def findNeighbor(self, i):
        numHands = len(self.hands)
        for next in range(1,numHands):
            neighbor = (i + next) % numHands
            if not self.hands[neighbor].isEmpty():
                return neighbor

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def printBackward(self):
        if self.next != None:
            tail = self.next
            tail.printBackward()
        print (self.cargo, sep='', end='')

def printList(node):
    while node:
        print (node, ' ', sep ='', end='')
        node = node.next
    print()

# Exercise 17.3, make printList to give output as list e.g. [1, 2, 3]
def printList(node):
    print('\n[', end='')
    while node:
        print (node, ', ', sep='', end='')
        node = node.next
    print('\b\b]\n')

def printBackward(list):
    if list == None: return
    head = list
    tail = list.next
    printBackward(tail)
    print (head, ' ', sep='', end='')

# You might wonder why printList and printBackward are functions and not
# methods in the Node class. The reason is that we want to use None to represent
# the empty list and it is not legal to invoke a method on None. This limitation
# makes it awkward to write list-manipulating code in a clean object-oriented style.

# The fundamental ambiguity theorem describes the ambiguity that is inherent
# in a reference to a node:
#       A variable that refers to a node might treat the node as a
#       single object or as the first in a list of nodes.

def removeSecond(list):
    if list == None: return
    first = list
    second = list.next
    # make the first node refer to the third
    first.next = second.next
    # separate the second node from the rest of the list
    second.next = None
    return second

# printBackwardNicely acts as a "wrapper", and it uses printBackward as a "helper"
def printBackwardNicely(list) :
    print ("[", sep='', end ='')
    printBackward(list)
    print ("]", sep='', end ='')

class LinkedList :
    def __init__(self) :
        self.length = 0
        self.head = None

    def printBackward(self):
        print ("[", sep='', end='')
        if self.head != None:
            self.head.printBackward()
        print ("]", sep='', end='')

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

class Stack :
    def __init__(self) :
        self.items = []
    def push(self, item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def isEmpty(self) :
        return (self.items == [])

# Exercise 18.7.1
# push 1, push 2, pop 1 & 2, add, result = 3, push 3, push 3, pop 3 & 3, multiply, result = 9, push 9 || (1+2)*3

# Exercise 18.7.2
# 1 + 2 * 3 = 1 + (2 * 3) || postfix notation : 1 2 3 * +

def evalPostfix(expr):
    import re
    tokenList = re.split("([^0-9])", expr)
    stack = Stack()
    for token in tokenList:
        if token == '' or token == ' ':
            continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
        while last.next:
            last = last.next
            # append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo

class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo

# Exercise 19.6.1 --- implement Queue ADT with list
class Queue_byList:
    def __init__(self):
        self.members = []
    def __str__(self): # I did it for my use
        return str(self.members)
    def isEmpty(self):
        return (len(self.members) == 0)
    def insert(self, cargo):
        self.members.append(cargo)
    def remove(self):
        if self.isEmpty():
            return None
        else:
            return self.members.pop(0)

class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def insert(self, item):
        self.items.append(item)
    def remove(self):
        maxi = 0
        for i in range(1,len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item

class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score= score
    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)
    def __cmp__(self, other):
        if self.score < other.score: return 1
        if self.score > other.score: return -1
        return 0

# Exercise 19.6.2 --- implement Priority Queue ADT with linked list
class PriorityQueue_byLinkedList:
    def __init__(self):
        pass
    def isEmpty(self):
        pass
    def insert(self):
        pass
    def remove(self):
        pass

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)

    def total(tree):
        if tree == None: return 0
        return total(tree.left) + total(tree.right) + tree.cargo

    def printTree(tree): #preorder
        if tree == None: return
        print (tree.cargo, ' ', sep='', end='')
        printTree(tree.left)
        printTree(tree.right)

    def printTreePostorder(tree):
        if tree == None: return
        printTreePostorder(tree.left)
        printTreePostorder(tree.right)
        print (tree.cargo, " ", sep= '', end='')

    def printTreeInorder(tree):
        if tree == None: return
        printTreeInorder(tree.left)
        print (tree.cargo, ' ', sep='', end='')
        printTreeInorder(tree.right)

# Exercise 20.5 --- expression string to token list
def stringToList(s):
    ret_list=[]
    for ch in s:
        ret_list.append(ch)
    return ret_list

def getToken(tokenList, expected):
    if tokenList[0] == expected:
        del tokenList[0]
        return True
    else:
        return False

#def getNumber(tokenList):
#    x = tokenList[0]
#    if not isinstance(x, int): return None
#    del tokenList[0]
#    return Tree (x, None, None)

def getNumber(tokenList):
    if getToken(tokenList, ’(’):
        x = getSum(tokenList)                         # get the subexpression
        if not getToken(tokenList, ’)’):              # remove the closing parenthesis
            raise ValueError, ’missing parenthesis’
        return x
    else:
        x = tokenList[0]
        if not isinstance(x, int): return None
        tokenList[0:1] = []
        return Tree (x, None, None)


def getProduct(tokenList):
    a = getNumber(tokenList)
    if getToken(tokenList, ’*’):
        b = getProduct(tokenList)
        return Tree (’*’, a, b)
    else:
        return a

def getSum(tokenList):
    a = getProduct(tokenList)
    if getToken(tokenList, ’+’):
        b = getSum(tokenList)
        return Tree (’+’, a, b)
    else:
        return a

def animal():
    # start with a singleton
    root = Tree("bird")

    # loop until the user quits
    while True:
        print
        if not yes("Are you thinking of an animal? "): break

        # walk the tree
        tree = root
        while tree.getLeft() != None:
            prompt = tree.getCargo() + "? "
            if yes(prompt):
                tree = tree.getRight()
            else:
                tree = tree.getLeft()

        # make a guess
        guess = tree.getCargo()
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print "I rule!"
            continue

        # get new information
        prompt = "What is the animal’s name? "
        animal = raw_input(prompt)
        prompt = "What question would distinguish a %s from a %s? "
        question = raw_input(prompt % (animal,guess))

        # add new information to the tree
        tree.setCargo(question)
        prompt = "If the animal were %s the answer would be? "
        if yes(prompt % animal):
            tree.setLeft(Tree(guess))
            tree.setRight(Tree(animal))
        else:
            tree.setLeft(Tree(animal))
            tree.setRight(Tree(guess))

def yes(ques):
    from string import lower
    ans = lower(raw_input(ques))
    return (ans[0] == ’y’)

# Exercise 20.7 --- Save knwledge to file
def save_knowledge():
    pass

