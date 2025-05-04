'''
MY PROG v1
author: Jackson Silvester

This is just a demo
'''

# import libraries
import os
import math

# set variables
boolchoice = False
str_userChoice = ''
my_Number = 0
#my_Number is a number that everytime you get a question right it adds 1 too like at line 53
#After you finish every question I use this to read you your score
print('some text')
answerlist = []
correctanswerlist = ('''A rural area of New Zealand",
"James Rolleston",
"He is in jail",
"That his dad is a super hero",
"Robbery",
"The impact of growing up without a father figure''')
#What I use answerlist for is everytime you answer a question it puts what you put you answered in there
#Then once you answer the final question it reads it out to you like at line 254 
#correct answer list is pretty similer except it doesnt change at all it just reads out the answers like at line 255
while boolchoice is False:
    name = input('What is your name')
    len(name)
    if(len(name)) > 10:
        print('To long under 10 characters please')
    elif(len(name)) < 1:
        print('To short at least one chaaracter please')
    else:
        boolchoice = True
#len counts how many digits are in any string in this case its counting the name our user puts in
#boolchoice makes it keep asking until they put in the correct amount of characters 1-10
#Once they do boolchoice also makes sure it moves on to the next question
#For example on line 39 and 40 "else:boolchoice = true"
#This makes it move onto line 44

    
while boolchoice is True:
    print('''1.What's the main setting of the film Boy
   A. A rural area of New Zealand
   B. A small town in Australia
   C. A busy city of New Zealand 
   D. A busy city of Australia''')
   #print('''''') just lets me put multible lines instead of just one
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        my_Number = my_Number + 1
        print("correct")
        answerlist.append('A rural area of New Zealand')
        #answerlist.append just adds what ever I put in the ('') to answerlist
        #like in this case its just "A rural area of New Zealand"
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('A small town in Australia')
    elif str_userChoice =='c':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('A busy city of New Zealand')
    elif str_userChoice =='d':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('A busy city of Australia')
    else:
        print("Lowercase or a b c d please")
while boolchoice is False:
    print('''2.Who plays the role of boy in the film?
   A. Taika Waititi
   B. James Rolleston
   C. Julian Dennison
   D. Cliff Curtis''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Taika Waititi')
    elif str_userChoice == 'b':
        print("correct")
        my_Number = my_Number + 1
        answerlist.append('James Rolleston')
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
    elif str_userChoice =='c':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Julian Dennison')
    elif str_userChoice =='d':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Cliff Curtis')
    else:
        print("Lowercase or a b c d please")
while boolchoice is True:
    print('''3.Where is boys dad at the start of the movie?
  A. He is in jail
  B. He is dead
  C. He is at a casino
  D. He lives far away''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        my_Number = my_Number +1
        answerlist.append('He is in jail')
        print("correct")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('He is dead')
    elif str_userChoice =='c':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('He is at a casino')
    elif str_userChoice =='d':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('He lives far away')
    else:
        print("Lowercase or a b c d please")
while boolchoice is False:
    print('''4. What does boy believe about his dad before he meets him?
  A. That his dad is a soldier
  B. That his dad is a world famous artist
  C. That his dad is a world famous musician
  D. That his dad is a super hero''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('That his dad is a soldier')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('That his dad is a world famous artist')
    elif str_userChoice =='c':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('That his dad is a world famous musician')
    elif str_userChoice =='d':
        my_Number = my_Number + 1
        answerlist.append('That his dad is a super hero')
        print("Correct")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
    else:
        print("Lowercase or a b c d please")
while boolchoice is True:
    print('''5.What did boys dad get arrested for?
  A. Tax fraud
  B. Assault
  C. Robbery
  D. Trespassing''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Tax fraud')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Assault')
    elif str_userChoice =='c':
        my_Number = my_Number + 1
        print("Correct")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Robbery')
    elif str_userChoice =='d':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('Trespassing')
    else:
        print("Lowercase or a b c d please")
while boolchoice is False:
    print('''6.What is the main theme explored in Boy?
  A. The importance of education
  B. The power of friendship
  C. The struggle for financial stability
  D. The impact of growing up without a father figure''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = True
        answerlist.append('The importance of education')
        print(f'Your final score is {my_Number}/6')
        print(f'        Your answers were{answerlist}')
        print(f' The correct answers were{correctanswerlist}')
        print(f'Thank you for playing {name}')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = True
        answerlist.append('The power of friendship')
        print(f'Your final score is {my_Number}/6')
        print(f'        Your answers were{answerlist}')
        print(f' The correct answers were{correctanswerlist}')
        print(f'Thank you for playing {name}')
    elif str_userChoice =='c':
        print("False")
        boolchoice = True
        answerlist.append('The struggle for financial stability')
        print(f'Your final score is {my_Number}/6')
        print(f'        Your answers were{answerlist}')
        print(f' The correct answers were{correctanswerlist}')
        print(f'Thank you for playing {name}')
    elif str_userChoice =='d':
        my_Number = my_Number + 1
        answerlist.append('The impact of growing up without a father figure')
        print("Correct")
        boolchoice = True
        print(f'Your final score is {my_Number}/6')
        print(f'Your answers were{answerlist}')
        print(f' The correct answers were\n{correctanswerlist}')
        print(f'Thank you for playing {name}')
    else:
        print("Actual answer please")'''
MY PROG v1
author: Jackson Silvester

This is just a demo
'''

# import libraries
import os
import math

# set variables
float_decimalNumber = '1'
boolchoice = True
str_userChoice = ''
my_Number = 0
print('some text')
answerlist = []
correctanswerlist = ["a","b","a","d","c","d"]
while boolchoice is True:
    print('''1.What's the main setting of the film Boy?
   A. A rural area of New Zealand
   B. A small town in Australia
   C. A busy city of New Zealand 
   D. A busy city of Australia''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        my_Number = my_Number + 1
        print("correct")
        answerlist.append('a')
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('b')
    elif str_userChoice =='c':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('c')
    elif str_userChoice =='d':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('d')
    else:
        print("Lowercase or a b c d please")
while boolchoice is False:
    print('''2.Who plays the role of boy in the film?
   A. Taika Waititi
   B. James Rolleston
   C. Julian Dennison
   D. Cliff Curtis''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('a')
    elif str_userChoice == 'b':
        print("correct")
        my_Number = my_Number + 1
        answerlist.append('b')
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
    elif str_userChoice =='c':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('c')
    elif str_userChoice =='d':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('d')
    else:
        print("Lowercase or a b c d please")
while boolchoice is True:
    print('''3.Where is boys dad at the start of the movie?
  A. He is in jail
  B. He is dead
  C. He is at a casino
  D. He lives far away''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        my_Number = my_Number +1
        answerlist.append('a')
        print("correct")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('b')
    elif str_userChoice =='c':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('c')
    elif str_userChoice =='d':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('d')
    else:
        print("Lowercase or a b c d please")
while boolchoice is False:
    print('''4. What does boy believe about his dad before he meets him?
  A. That his dad is a soldier
  B. That his dad is a world famous artist
  C. That his dad is a world famous musician
  D. That his dad is a super hero''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('a')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('b')
    elif str_userChoice =='c':
        print("False")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('c')
    elif str_userChoice =='d':
        my_Number = my_Number + 1
        answerlist.append('d')
        print("Correct")
        boolchoice = True
        print("Your score is")
        print(f'{my_Number}/6')
    else:
        print("Lowercase or a b c d please")
while boolchoice is True:
    print('''5.What did boys dad get arrested for?
  A. Tax fraud
  B. Assault
  C. Robbery
  D. Trespassing''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('a')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('b')
    elif str_userChoice =='c':
        my_Number = my_Number + 1
        print("Correct")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('c')
    elif str_userChoice =='d':
        print("False")
        boolchoice = False
        print("Your score is")
        print(f'{my_Number}/6')
        answerlist.append('d')
    else:
        print("Lowercase or a b c d please")
while boolchoice is False:
    print('''6.What is the main theme explored in Boy?
  A. The importance of education
  B. The power of friendship
  C. The struggle for financial stability
  D. The impact of growing up without a father figure''')
    str_userChoice = input("Please pick A B C D ")
    if str_userChoice == 'a':
        print("False")
        boolchoice = True
        print("Your final score is")
        print(f'{my_Number}/6')
        answerlist.append('a')
    elif str_userChoice == 'b':
        print("False")
        boolchoice = True
        print("Your final score is")
        print(f'{my_Number}/6')
        answerlist.append('b')
    elif str_userChoice =='c':
        print("False")
        boolchoice = True
        print("Your final score is")
        print(f'{my_Number}/6')
        answerlist.append('c')
    elif str_userChoice =='d':
        my_Number = my_Number + 1
        answerlist.append('d')
        print("Correct")
        boolchoice = True
        print("Your final score is")
        print(f'{my_Number}/6')
        print(f'        Your answers were{answerlist}')
        print(f' The correct answers were{correctanswerlist}')
    else:
        print("Actual answer please")
