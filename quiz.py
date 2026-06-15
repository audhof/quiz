'''
Name: Audrey
Date: Friday, March 21, 2025
Lesson: MC Quiz Assignment (The Hunger Games)
'''

#Set variable score to keep track of score
score = 0

#Boolean- set variable for getting all answers correct
perfect = False

#Total questions variable
totalquestions= 10

#Introduction to Quiz
print('\t\t\tHunger Games Quiz\nThis is a multiple choice quiz with 10 questions to test your knowledge on The Hunger Games franchise. Good Luck!\n') 

#Question 1
q1 = (input('Question 1: What district is Katniss from?\na)12\nb)11\nc)10\nd)7\n'))

#use conditionals to check the right answer
#need to use if, elif and else 
if q1 == "a":
  print('You are correct!')
  score = score + 1
elif q1 == "b" or q1 == "c" or q1 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 2
q2 = (input('\nQuestion 2: Who is the mentor of Katniss and Peta?\na)Effie\nb)Haymitch\nc)Cinna\nd)Plutarch\n'))

#Conditionals
if q2 == "b":
  print('You are correct!')
  score = score+1
elif q2 =="a" or q2 =="c" or q2 =="d":
  print('You are incorrect :(')
else: 
  print('Invalid input. Please enter a, b, c or d')
  
#Question 3
q3 = (input("\nQuestion 3: What is Katniss' sister's name?\na)Pricilla\nb)Primrose\nc)Patricia\nd)Paula\n"))

#conditionals
if q3 == "b":
  print('You are correct!')
  score = score + 1
elif q3 == "a" or q3 == "c" or q3 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 4
q4 = (input('\nQuestion 4: How old is Katniss at the beginning of the first book?\na)14\nb)15\nc)16\nd)17\n'))

#conditionals
if q4 == "c":
  print('You are correct!')
  score = score + 1
elif q4 == "a" or q4 == "b" or q4 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 5
q5 = (input('\nQuestion 5: What does district 4 specialize in?\na)Mining\nb)Fishing\nc)Technology\nd)Lumber\n'))

#conditionals
if q5 == "b":
  print('You are correct!')
  score = score + 1
elif q5 == "a" or q5 == "c" or q5 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 6
q6 = (input('\nQuestion 6: The first book in the Hunger Games series was published in what year?\na)2007\nb)2004\nc)2005\nd)2008\n'))

#conditionals
if q6 =="d":
  print('You are correct!')
  score = score +1
elif q6 =="a" or q6 == "b" or q6 =="c":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 7
q7 = (input('\nQuestion 7: What skill was Gale better at than Katniss?\na)setting snares\nb)fishing\nc)trading\nd)using a knife\n'))
#conditionals
if q7 == "a":
  print('You are correct!')
  score = score + 1
elif q7 == "b" or q7 == "c" or q7 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 8
q8 = (input('\nQuestion 8: What does Katniss do when Rue is killed?\na)bury her body\nb)run away\nc)cover her body in flowers\nd)camouflage her body\n'))

#conditionals
if q8 == "c":
  print('You are correct!')
  score = score + 1
elif q8 == "a" or q8 == "b" or q8 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 9
q9 = (input('\nQuestion 9: How does Cato die?\na)the muttations kill him\nb)Katniss shoots him\nc)he starves\nd)tracker jackers kill him\n'))

#conditionals
if q9 == "b":
  print('You are correct!')
  score = score + 1
elif q9 == "a" or q9 == "c" or q9 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Question 10
q10 = (input('\nQuestion 10: Who wrote the Hunger Games books?\na)Suzanne Collins\nb)Mary Cartwright\nc)Allison Brown\nd)Cate Allister\n'))

#conditionals
if q10 == "a":
  print('You are correct!')
  score = score + 1
elif q10 == "b" or q10 == "c" or q10 == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')
  
#Bonus
qb = (input('\nBonus: What games did Haymitch win?\na)first quarter quell, 25th Hunger Games\nb)first quarter quell, 50th Hunger Games\nc)second quarter quell, 50th Hunger Games\nd)third quarter quell, 75th Hunger Games\n'))

#conditionals
if qb == "c":
  print('You are correct!')
  score = score + 1
elif qb == "a" or qb == "b" or qb == "d":
  print('You are incorrect :(')
else:
  print('Invalid input. Please enter a, b, c or d')

#End-check for perfect score
if score>=totalquestions:
  perfect=True
  
#Display results
print('final score: ', score, ' points')

if perfect:
  print("\nCongratulations you achieved a perfect score!")
elif score>6 and score<10:
  print("\nGood job your knowledge on the Hunger Games is impressive!")
else:
  print("\nYou should brush up on your Hunger Games knowlege and try the quiz again!")
  
#display correct answers
ak = input('Would you like to see the answer key? yes/no')
if not ak == "yes":
  print("Ok, thanks for playing!")
elif ak == "yes":
  print('\nAnswer Key:\n1:a\t2:b\t3:b\t4:c\t5:b\t6:d\t7:a\t8:c\t9:b\t10:a\tBonus:c')
else: 
  print('invalid input, please enter yes or no')
