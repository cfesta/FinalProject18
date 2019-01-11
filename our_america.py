player = input("What is your name?")
print(f"Hello, {player} welcome to the American History trivia game, Our America!")

score = 0

class Question:

    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

q1 = Question("Which item was used for entertainment and news during World War 1?", "c. radio", ["a. telephone", "b. hammer", "c. radio"])
q2 = Question("Who wrote about the importance of the navy?", "c. Alfred Thayer Mahan", ["a. Susan B. Anthony", "b. Mark Twain", "c. Alfred Thayer Mahan"])
q3 = Question("Who came up with the New Deal plan?", "a. Franklin D. Roosevelt", ["a. Franklin D Roosevelt  b. Theodore Roosevelt  c. Thurman Arnold"])
q4 = Question("Which was NOT a part of the New Deal?", "c. Free Silver", ["a. National Recovery Administration",  "b.Agricultural Adjustment Act",  "c. Free Silver"])
q5 = Question("Who was NOT a part of the Big 4 in the League of Nations?", "d. Herbert Hoover", ["a. David Lloyd George", "b. Vittorio Emanuele Orlando", "c. Georges Clemenceau", "d. Herbert Hoover", "e. Woodrow Wilson"])
q6 = Question("Who founded and was the president of the environmental association known as the Sierra Club?", "b. John Muir", ["a. Woodrow Wilson", "b. John Muir", "c. Theodore Roosevelt"])
#q7 = Question()
#q8 = Question()
#q9 = Question()
#q10= Question()

questions = [q1, q2, q3, q4, q5, q6]
#questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

current_question = questions.pop(0)

#for x in range whatever just to run through the determining whether or not its right mechanism

print(f"Question: {current_question.question}")
print(f"Choices: {current_question.choices}")
user_answer = input("What is your answer?")

if user_answer != current_question.choices:
  input("That is not one of the answer choices. Please try again.")
elif user_answer == current_question.answer:
  score += 1
  print("You got it right and have earned a point!")
else:
  print("Good try, but not quite!")

print(f"Answer: {current_question.answer}")