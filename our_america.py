player = input("What is your name?")
print(f"Hello, {player}! Welcome to the American History trivia game, Our America!")

score = 0

class Question:
    """Gives the attributes of the question"""
    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices


q1 = Question("Which item was used for entertainment and news during World War 1?", "c. radio" , ["a. telephone", "b. hammer", "c. radio"])

q2 = Question("Who wrote about the importance of the navy?", "c. Alfred Thayer Mahan", ["a. Susan B. Anthony", "b. Mark Twain", "c. Alfred Thayer Mahan"])

q3 = Question("Who came up with the New Deal plan?", "a. Franklin D Roosevelt", ["a. Franklin D Roosevelt", "b. Theodore Roosevelt",  "c. Thurman Arnold"])

q4 = Question("Which was NOT a part of the New Deal?", "c. Free Silver", ["a. National Recovery Administration",  "b.Agricultural Adjustment Act",  "c. Free Silver"])

q5 = Question("Who was NOT a part of the Big 4 in the League of Nations?", "d. Herbert Hoover", ["a. David Lloyd George", "b. Vittorio Emanuele Orlando", "c. Georges Clemenceau", "d. Herbert Hoover", "e. Woodrow Wilson"])

q6 = Question("Who founded and was the president of the environmental association known as the Sierra Club?", "b. John Muir", ["a. David Muir", "b. John Muir", "c. Theodore Roosevelt"])

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

q17 = Question("Who of the following was NOT involved in the Social Gospel?", "a. John Muir", ["a. John Muir", "b. Walter Rauschenbusch", "c. Jacob Riis"])

q18 = Question("Who wrote a book about the meatpacking industry called, The Jungle?", "b. Upton Sinclair", ["a. Kate Chopin", "b. Upton Sinclair", "c. Henry Adams"])

q19 = Question("Winslow Homer, John Singer Sargent, and George Bellows belonged to what society?", "a. Ashcan School", ["a. Ashcan School", "b. Rocky Mountain Club", "c. National Federation of Painters"])

q20 = Question("What was the belief that people should  rely for guidance on scientific inquiry not morals?", "c. Pragmatism", ["a. Inquiry Method", "b. Scientific Revolution", "c. Pragmatism"])

q21 = Question("Which law had to do with schools being built?", "b. Morril Land Grant Act", ["a. School Foundation Fund", "b. Morril Land Grant Act", "c. Emergency Education Act"])

q22 = Question("Who of the following was NOT involved in the Social Gospel?", "a. John Muir", ["a. John Muir", "b. Walter Rauschenbusch", "c. Jacob Riis"])

q23 = Question("Roscoe Conkling led what Republican political group?", "c. Stalwarts", ["a. Muggles", "b. Haf Breeds", "c. Stalwarts"])

q24 = Question("Who were the Half Breeds led by?", "c. James G. Blaine", ["a. Dr. Samuel Burchard", "b. Rutherford B. Hayes", "c. James G. Blaine"])

q25 = Question("Which of the following was passed in an attempt to crack down on unfair business combinations?", "c. Sherman Antitrust Act", ["a. McKinley Tariff", "b. Mckinley Antitrust Act", "c. Sherman Antitrust Act"])

q26 = Question("Which law's goal was to make railroad rates fair?", "c. Interstate Commerce Act", ["a. Railroad Standards Act", "b. McKinley Antitrust Act", "c. Interstate Commerce Act"])

q27 = Question("What did the Crime of '73 (1873) have to do with?", "c. currency", ["a. Garfield's assination", "b. bank robbery", "c. currency"])

q28 = Question("Who wrote the book, Coin's Financial School?", "a. William H. Harvey", ["a. William H. Harvey Act", "b. Horace Greeley", "c. Mark Twain"])

q29 = Question("Which nation did Valeriano Weyler fight for?", "b. Spain", ["a. Cuba", "b. Spain", "c. USA"])

q30 = Question("Who led the Cuban Revolution Party?", "c. Jose Marti", ["a. Nelson Miles", "b. Pascual Cerveza", "c. Jose Marti"])

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30]
#creates the list of questions

score == 0
#creates the player's score

for current_question in questions:
  print(f"Question: {current_question.question}")
  print(f"Choices: {current_question.choices}")
  user_answer = input("What is your answer?")
#question and choice printing mechanism and the input area for the player's answer

  if user_answer not in current_question.choices:
    input("That is not one of the answer choices. Please try again.")
    #checks to see if player's answer is one of the answer choices
  elif user_answer == current_question.answer:
    score += 1
    #adds a point to the player's score if they get a question correct
    print("You got it right and have earned a point!")
  else:
    print("Good try, but not quite!")
    print(f"Answer: {current_question.answer}")
#prints the answer to the question

  print (f"You have {score} points.")
#shows player their score

  if score == 12:
    print("You have won the game and are the ultimate American History Trivia Master!")
    print(f"keep_playing")
  else:
    pass
#checks to see whether or not the player has won the game

  keep_playing = input("Would you like to keep playing? Type y for yes or n for no.")
#creates the option for the player to stop playing

  if keep_playing == "y":
    print("Ok let's keep going!")
    #reenter for loop
  else:
    print("Play again sometime!")
    break
    #exit for loop