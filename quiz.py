#!/usr/bin/python
import csv
import random
import os
import sys

total_questions = 0
testing = True
current_answer = ''
try:
	question_file = str(sys.argv[1])
except:
	print("usage: quiz.py [question-file]")
	sys.exit()

questions = csv.DictReader(open(question_file))

for question in questions:
	total_questions += 1
	
while testing:
	os.system('clear')
	questions = csv.DictReader(open(question_file))
	current_question = random.randrange(1,total_questions+1)
	for question in questions:
		if int(question["question_id"]) == current_question:
			print(question["question"])
			print("\n")
			print("(A) " + question["answer_a"])
			print("(B) " + question["answer_b"])
			print("(C) " + question["answer_c"])
			print("(D) " + question["answer_d"])
			current_answer = question["correct_answer"]
			
	print("\n")
	choice = input("Enter answer or q to quit: ")
	
	print("\n")
	if choice == 'q':
		os.system('clear')
		break
	if choice.upper() == current_answer.upper():
		print("Correct!")
	else:
		print("Incorrect!")
		print("\n")
		print("The correct answer was " + current_answer)
		
	print("\n")
	input("Press [ENTER] to continue...")
