import random
class red_question:
  def __init__ (self, questions, answer, choices):
    self.questions = questions
    self.answer = answer
    self.choices = choices

class green_question:
  def __init__ (self, questions, answer, choices):
    self.questions = questions
    self.answer = answer
    self.choices = choices

class blue_question:
  def __init__ (self, questions, answer, choices):
    self.questions = questions
    self.answer = answer
    self.choices = choices

class purple_question:
  def __init__ (self, questions, answer, choices):
    self.questions = questions
    self.answer = answer
    self.choices = choices

characters = ["George Washington", "Abraham Lincoln", "Martin Luther King Jr.", "Rosa Parks", "Elizabeth Cady Stanton"]

colors = [("Red", "Laws"), ("Green", "People"), ("Blue", "Technology"), ("Purple", "Events")]

dice_roll = random.choice(colors) #mimics dice roll
input(f"You rolled {dice_roll[0]}, which is the {dice_roll[1]} category!")

red_questions = [("Which was NOT a part of the New Deal?", "a. National Recovery Administration  b.Agricultural Adjustment Act  c. Free Silver"),]

green_questions = [("Who came up with the New Deal plan?", "a. Franklin D Roosevelt  b. Theodore Roosevelt  c. Thurman Arnold"),
("Who wrote about the importance of the navy?", "a. Susan B. Anthony", "b. Mark Twain", "c. Alfred Thayer Mahan"), ]

blue_questions = [("What was the largest public works project as of 1880?", "a. ____" "b. TVA")]

purple_questions = [()]

if dice_roll[0] == "Red":
  random.choice(red_questions[0])
  print(red_questions[1])

#class Cards:
  #def __init__ (self, )