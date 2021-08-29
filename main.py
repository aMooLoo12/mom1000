from Question import Question

question_prompts = [
    "How do you do a print statement?\n(a) print'poop'\n(b) print(poop)\n(c) Print('poop')\n(d) print('poop')\n\n",
    "How do do a variable\n(a) i = \n(b) p Moo\n(c)she + \n\n",
    "How do you do a string\n(a) string\n(b) ()\n(c)'' \n\n",
    "How do you do a input\n(a) i input\n(b) i = input ()\n(c)input \n\n",
]

questions = [
    Question(question_prompts[0], "d"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("you got", score, "out of", len(questions))


run_test(questions)











