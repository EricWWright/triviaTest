# Eric Wright
# 1/19
# Trivia Challenge
# Trivia game that reads a plain text file
import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia game, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his / her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    file_name ="hamTest.txt"
    mode = "r"
    the_file = open_file(file_name, mode)
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answers[i])
        userInput = input("Enter your guess: ").lower()
        if userInput == correct:
            print("Correct!", explanation)
            score += 1
        else:
            print("Incorrect...", explanation)
        print(score)
        category, question, answers, correct, explanation = next_block(the_file)
    the_file.close()
    print("You have reached the end of the test")
    print("Final Score:", score)
    input("press enter to exit")
    # sys.exit()

main()
