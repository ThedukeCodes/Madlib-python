# -*- coding: utf-8 -*-
from __future__ import unicode_literals



# -------------------------------------THE GAME STARTS HERE--------------------------------------------------------------------------------------------------

#In this preliminary section we will collect all the necessary definitions for the game in general. Let's call them "primary input"

prompt = 'Please select a game difficulty by typing it in!'
prompt2 = "Choice must be: 'easy', 'medium', or 'hard'  >>>>>"
spaces = ["___1___", "___2___" , "___3___", "___4___" ]
good_answer = "This answer is correct!"
bad_answer = "Nope, try again!"
question = "What's the answer for word"
questionmark = "?"
levelchoices = ["easy", "medium", "hard"]


# ---- Sentence + answerlist for all levels

sample_sentences =["___1___ is the capital of Belgium.___2___ is the capital of France. ___3___ is the capital of America. ___4___ is the capital of England. (CAPITAL LETTERS AS A FIRST LETTER IS REQUIRED) ", "A cat likes to drink ___1___ . A cow eats ___2___ . A lezard is a __3___  . The ___4___ is the species of the dolphin.", "Stradivarius is a  ___1___ (instrument) .  ___2___ wrote the 5th symphony (the deaf guy). It is 2 : 30 AM in Belgium and I am really ___3___ , but when I start coding I can't stop until I resolved the problem and this is a real problem for my sleeping pattern. Python is more of a ___4___ science language than a weblanguage."]
answerlist_all_level= [["Brussels", "Paris", "Washington", "London"],["milk", "grass", "reptile", "fish"], ["violin", "Beethoven", "tired", "computing"]]

#This is the game function for ALL LEVELS



def levelplaygame(x):
	completion1 = sample_sentences[x].replace(spaces[0],answerlist_all_level[x][0])
	completion2 = completion1.replace(spaces[1], answerlist_all_level[x][1]) 			##### Those inputs, are "secondary" will vary on their indicelevel define above, according to the indice level and get the right sentence with the right answer.
	completion3 = completion2.replace(spaces[2], answerlist_all_level[x][2])				#####Those are the inputs of the main function playgame.
	completion_list = [sample_sentences[x], completion1, completion2, completion3]
	count = 0
	while count < 4: #This is the loop when answers are corrects it took me hours to figure out how to shorten it likt this
		print completion_list[count]
		user_input2 = raw_input(question+spaces[count]+questionmark)
		if user_input2 == answerlist_all_level[x][count]:
			print good_answer
			count = count + 1
			if count == 4: #This is the loop break when all the answers are corrects.
				print "-"*40 + "Goodbye!" + "-"*40
				break
		elif user_input2 != answerlist_all_level[x+0+count]: #This is the cycle for bad answers
			print bad_answer
			count = count


	
#######################################################################################################
#This is the fist stage of the game where the user must chose his level.



def levelchoice():
	levelselected = raw_input(prompt+prompt2)
	if levelselected in levelchoices:
		if levelselected == levelchoices[0]: #We use if statements to redirect the user to the right level depending of whether he typed in "easy, hard or medium"
			return levelplaygame(0)
			print "You have selected: " + levelselected
		elif levelselected == levelchoices[1]:
			return levelplaygame(1)
			print "You have selected: " + levelselected
		elif levelselected == levelchoices[2]:
			return levelplaygame(2)
			print "You have selected: " + levelselected
	else:
		return levelchoice()
print levelchoice()

"""
This function will return back if the user input does not correspond to one of the levelchoices
"""




	







