player = input("What is your name?")
print(f"Hello, {player}! Welcome to the American History trivia game, Our America!")

score = 0

keep_playing = input("Would you like to keep playing? Type y for yes or n for no.")

class Question:

    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices


q1 = Question("Which item was used for entertainment and news during World War 1?", "c. radio" , ["a. telephone", "b. hammer", "c. radio"])

q2 = Question("Who wrote about the importance of the navy?", "c. Alfred Thayer Mahan", ["a. Susan B. Anthony", "b. Mark Twain", "c. Alfred Thayer Mahan"])

q3 = Question("Who came up with the New Deal plan?", "a. Franklin D Roosevelt", ["a. Franklin D Roosevelt", "b. Theodore Roosevelt",  "c. Thurman Arnold"])

q4 = Question("Which was NOT a part of the New Deal?", "c. Free Silver", ["a. National Recovery Administration",  "b.Agricultural Adjustment Act",  "c. Free Silver"])

q5 = Question("Who was NOT a part of the Big 4 in the League of Nations?", "d. Herbert Hoover", ["a. David Lloyd George", "b. Vittorio Emanuele Orlando", "c. Georges Clemenceau", "d. Herbert Hoover", "e. Woodrow Wilson"])

q6 = Question("Who founded and was the president of the environmental association known as the Sierra Club?", "b. John Muir", ["a. Woodrow Wilson", "b. John Muir", "c. Theodore Roosevelt"])

q7 = Question("Who invented the assembly line?", "c. Henry Ford", ["a. The Wright Brothers", "b. Thomas Edison", "c. Henry Ford"])

q8 = Question("Which of the following was NOT one of the main causes of the Great Depression?", "a. Treaty of Versailles", ["a. Treaty of Versailles", "b. Stock Market Crash", "c. War Debt"])

q9 = Question("What is a bill initiated by the people?", "b. initiative", ["a. referendum", "b. initiative", "c. people bill"])
q10= Question("Who was the reform governor from Wisconsin?", "a. La Follette", ["a. La Follette", "b. FDR", "c. Theodore Roosevelt"])

q11 = Question("Which belief is defined as native-born Americans being against immigration?", "a. Nativism", ["a. Nativism", "b. Anti-Immigration", "c. Immigration Restriction League"])

q12 = Question("Which of the following was a law passed in 1882 to keep Chinese people from immigrating to the United States?", "c. Chinese Exclusion Act", ["a. Anti-Immigration Act", "b. Pacific Immigration Exclusion Act", "c. Chinese Exclusion Act"])

q13 = Question("Who founded the American Protective Association?", "b. Henry Bowers", ["a. Horace Greeley", "b. Henry Bowers", "c. James Madison"])

q14 = Question("Which of the following was NOT an organization against immigration?", "a. Anti-Immigration League", ["a. Anti-Immigration League", "b. American Protective Association", "c. Immigration Restriction League"])

q15 = Question("Which of the following was NOT an organization against immigration?", "a. Anti-Immigration League", [ "a. Anti-Immigration League", "b. American Protective Association", "c. Immigration Restriction League"])

q16 = Question("Who was the populist who said raise less corn and more hell?", "c. Mary E. Lease", ["a. Tom Watson", "b. Leonidas L. Polk", "c. Mary E. Lease"])

#q17 =

#q18 =

#q19 =

#q20 =

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,q12, q13, q14, q15, q16] #q17, q18, q19, q20]

#for x in range whatever just to run through the determining whether or not its right mechanism

score == 0

for current_question in questions:
  print(f"Question: {current_question.question}")
  print(f"Choices: {current_question.choices}")
  user_answer = input("What is your answer?")

  if user_answer not in current_question.choices:
    input("That is not one of the answer choices. Please try again.")
  elif user_answer == current_question.answer:
    score += 1
    print("You got it right and have earned a point!")
  else:
    print("Good try, but not quite!")
    print(f"Answer: {current_question.answer}")

  print (f"You have {score} points.")

  if score == 3:
    print("You have won the game and are the ultimate American History Trivia Master! Thanks for playing!")
print(f"{keep_playing}"
if keep_playing = "y":
  #reenter for loop
else:
  stop