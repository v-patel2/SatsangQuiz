from QuizClass import Question
import random

print("Welcome to the Satsang Quiz! Test your knowledge by answering these questions.\n")

prompts = [
    "Which mandir did Shriji Maharaj build first?\n(a) Ahmedabad\n(b) Gadhada\n(c) Bhuj\n(d) Vadtal\n\n",
    "What year was Pramukh Swami Maharaj born in?\n(a) 1920\n(b) 1923\n(c) 1921\n(d) 1925\n\n",
    "Where did Maharaj meet Gunatitanand Swami Maharaj first?\n(a) Jetpur\n(b) Piplana\n(c) Vadtal\n(d) Bhadra\n\n",
    "Which mandir was Mahant Swami Maharaj the mahant of?\n(a) Ahmedabad\n(b) Sarangpur\n(c) Hyderabad\n(d) Mumbai\n\n",
    "Which of the following qualities of Bhagwan did Atmanand Swami not believe?\n(a) Sarvopari\n(b) Sakar\n(c) Pragat\n(d) Sarva-Karta\n\n"
]

questions = [
    Question(prompts[0], "a"),
    Question(prompts[1], "c"),
    Question(prompts[2], "b"),
    Question(prompts[3], "d"),
    Question(prompts[4], "b")
]
random.shuffle(questions)

def run_test(questions):
    points = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            points += 1
    print("Great work! " + "You got " + str(points) + "/" + str(len(questions)) + " points.")

run_test(questions)
