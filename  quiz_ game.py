def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print('Correct!')
        return 1
    else:
        print('Incorrect')
        return 0

print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
score = 0

score += ask_question("What does CPU stand for? ", "central processing unit")
score += ask_question("What does RAM stand for? ", "random access memory")
score += ask_question("What does GPU stand for? ", "graphics processing unit")
score += ask_question("What does PSU stand for? ", "power supply unit")

print("You got " + str(score) + " questions correctly!")
print("You got " + str((score / 4) * 100) + "%")
