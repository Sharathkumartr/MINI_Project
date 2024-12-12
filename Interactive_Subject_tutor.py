# -- coding: utf-8 --
"""
Created on Mon Dec  2 00:36:35 2024

@author: thorj
"""
#Tutor in a range of preferred subjects
# Import necessary libraries
from IPython.display import clear_output
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to read the text aloud."""


    engine.say(text)
    engine.runAndWait()

# Define lessons and quizzes for different subjects
def math_tutor():
    clear_output(wait=True)
    # Lesson 1: Basics of Addition
    lesson1 = "Lesson 1: Basics of Addition. Example: 2 plus 2 equals 4."
    
    # Lesson 2: Basics of Multiplication
    lesson2 = "Lesson 2: Basics of Multiplication. Example: 3 times 4 equals 12."
    
    # Lesson 3: Pythagorean Theorem
    lesson3 = (
        "Lesson 3: The Pythagorean Theorem. "
        "The Pythagorean Theorem states that in a right triangle, "
        "the square of the hypotenuse (the side opposite the right angle) is equal "
        "to the sum of the squares of the other two sides. "
        "This is expressed as a² + b² = c², where a and b are the lengths of the legs, "
        "and c is the length of the hypotenuse."
    )
    
    print(lesson1)
    print(lesson2)
    print(lesson3)
    
    # Option to read out lessons
    choice = input("Type 'R' to read out the lessons or any other key to continue: ").strip().lower()
    if choice == 'r':
        speak(lesson1)
        speak(lesson2)
        speak(lesson3)

    print("\nNow it's your turn!")
    
    # Quiz 1: Basics of Addition
    answer1 = input("Quiz 1: What is 7 + 6? ")
    if answer1 == "13":
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is 13.")
    
    # Quiz 2: Basics of Multiplication
    answer2 = input("Quiz 2: What is 5 x 3? ")
    if answer2 == "15":
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is 15.")
    
    # Quiz 3: Pythagorean Theorem
    print("\nQuiz 3: Pythagorean Theorem")
    print("A right triangle has legs of lengths 3 and 4. What is the length of the hypotenuse?")
    print("Hint: Use the formula a² + b² = c²")
    answer3 = input("Your answer: ")
    if answer3 == "5":
        print("Correct! The hypotenuse is 5.")
    else:
        print("That's incorrect. The correct answer is 5.")
def science_tutor():
    clear_output(wait=True)
    lesson1 = "Welcome to the Science Tutor! Lesson 1: Basics of Photosynthesis. Plants use sunlight to convert carbon dioxide and water into oxygen and glucose."
    lesson2 = "Lesson 2: States of Matter. There are three common states of matter: Solid, Liquid, and Gas."
    print(lesson1)
    print(lesson2)
    choice = input("Press 'R' to read out the lessons or any other key to continue: ").strip().lower()
    if choice == 'r':
        speak(lesson1)
        speak(lesson2)

    print("\nNow it's your turn!")
    answer1 = input("Quiz 1: What is the primary gas produced during photosynthesis? ").strip().lower()
    if answer1 == "oxygen":
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is oxygen.")
    
    answer2 = input("Quiz 2: What are the three common states of matter? (Separate with commas) ").strip().lower()
    if "solid" in answer2 and "liquid" in answer2 and "gas" in answer2:
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is Solid, Liquid, and Gas.")

def history_tutor():
    clear_output(wait=True)
    lesson1 = "Welcome to the History Tutor! Lesson 1: The American Revolution. The American Revolution was a war between the 13 American colonies and Britain from 1775 to 1783."
    lesson2 = "Lesson 2: The Industrial Revolution. The Industrial Revolution was a period of major industrialization during the late 1700s and early 1800s."
    print(lesson1)
    print(lesson2)
    choice = input("Press 'R' to read out the lessons or any other key to continue: ").strip().lower()
    if choice == 'r':
        speak(lesson1)
        speak(lesson2)

    print("\nNow it's your turn!")
    answer1 = input("Quiz 1: In which year did the American Revolution end? ")
    if answer1 == "1783":
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is 1783.")
    
    answer2 = input("Quiz 2: During which centuries did the Industrial Revolution take place? ")
    if answer2 == "18th and 19th":
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is the 18th and 19th centuries.")

def geography_tutor():
    clear_output(wait=True)
    lesson1 = "Welcome to the Geography Tutor! Lesson 1: Continents of the World. There are seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America."
    lesson2 = "Lesson 2: The Oceans. The Earth's oceans are: Pacific, Atlantic, Indian, Arctic, and Southern."
    print(lesson1)
    print(lesson2)
    choice = input("Press 'R' to read out the lessons or any other key to continue: ").strip().lower()
    if choice == 'r':
        speak(lesson1)
        speak(lesson2)

    print("\nNow it's your turn!")
    answer1 = input("Quiz 1: How many continents are there on Earth? ")
    if answer1 == "7":
        print("Correct!")
    else:
        print("That's incorrect. The correct answer is 7.")
    
    answer2 = input("Quiz 2: Name two of Earth's oceans. (Separate with commas) ").strip().lower()
    oceans = {"pacific", "atlantic", "indian", "arctic", "southern"}
    provided = set(map(str.strip, answer2.split(',')))
    if provided & oceans:
        print("Correct!")
    else:
        print("That's incorrect. The correct answers include Pacific, Atlantic, Indian, Arctic, or Southern.")

# Define the main menu
def main_menu():
    while True:
        clear_output(wait=True)
        print("Welcome to the Tutoring Program!")
        print("Choose a subject to learn:")
        print("1. Math")
        print("2. Science")
        print("3. History")
        print("4. Geography")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            math_tutor()
        elif choice == "2":
            science_tutor()
        elif choice == "3":
            history_tutor()
        elif choice == "4":
            geography_tutor()
        elif choice == "5":
            print("Thank you for using the Tutoring, If you want any help please reach out. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")

# Run the program
main_menu()                                                     
2