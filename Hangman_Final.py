import os
import sys
from tkinter import *
import tkinter as tk
import random
import csv
from PIL import ImageTk, Image


# Open the CSV file and read the words into a list
with open('output_file.csv', 'r') as file:
    reader = csv.reader(file)
    words = [row[0].lower() for row in reader]

random_word = random.choice(words)
print(random_word)
guessed_letters = []
word_state = "_" * len(random_word)

# Define the number of guesses the player has
max_guesses = len(random_word)
num_guesses = 0


def save_letter(letter):
    global guessed_letters, word_state, random_word, num_guesses
    guessed_letters.append(letter)
    guessing_letters.config(text=f"Guessed Letters: {' '.join(guessed_letters).upper()}", font='arial') # update guessed letters label
    print(guessed_letters)
    guess = letter.lower()

    # Check if the guess is a valid letter and hasn't been guessed before
    if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:

        # Update the word state with the guessed letter
        new_word_state = ""
        for i in range(len(random_word)):
            if guess == random_word[i]:
                new_word_state += guess
            else:
                new_word_state += word_state[i]
        word_state = new_word_state
        word_to_guess.config(text=f'The word to guess is: {new_word_state.upper()}', font='arial')

        if guess in random_word:
            game_status.config(text=f'Status: Correct!', font='arial')
            print("Correct!")
        else:
            num_guesses += 1
            game_status.config(text=f'Status: Incorrect, you have {max_guesses - num_guesses} chances left', font='arial')
            print("Incorrect guess. You have", max_guesses - num_guesses, "guesses remaining.")

    print(f'You have {max_guesses - num_guesses} chances left')

    # Check if the player won or lost
    if "_" not in word_state:
        game_status.config(text=f'Status: Congratulations, you guessed the word {word_state}', font='arial')
        print("Congratulations, you guessed the word", random_word, "!")
    elif num_guesses >= max_guesses:
        game_status.config(text=f'Status: You run out of guesses, you lost. The word was {random_word}', font='arial')
        print("Sorry, you ran out of guesses. The word was", random_word, ".")


def restart_game():
    python = sys.executable
    os.execl(python, python, * sys.argv)


root = tk.Tk()
root.geometry('600x500')
root.title('Hangman Game')

image = Image.open("hangman.png")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, image=photo, anchor=tk.NW)


introlabel = Label(root, text=' Welcome to Hangaman Game', font='arial')
introlabel.place(x=200, y=0)

word_to_guess = Label(root, text=f'The word to guess is: {word_state}', font='arial')
word_to_guess.place(x=50, y=100)

guessing_letters = Label(root, text=f"Guessed Letters: {' '.join(guessed_letters)}", font='arial')
guessing_letters.place(x=50, y=125)

game_status = Label(root, text=f'Status: You have {max_guesses} chances', font='arial')
game_status.place(x=50, y=150)

restart_button = Button(root, text='Restart', font='arial', command=restart_game)
restart_button.place(x=50, y=175)


def make_buttons1():
    count = 0
    lst = []
    if count <= 10:
        for letter in 'ABCDEFGHIJ':
            lst.append(letter)
        for letter in lst:
            button = Button(master=root, text=letter, command=lambda letter=letter: save_letter(letter))
            button.place(x=50 + 50 * count, y=300)
            count += 1


def make_buttons2():
    count1 = 0
    lst1 = []
    if count1 <= 10:
        for letter in 'KLMNOPQRST':
            lst1.append(letter)
        for letter in lst1:
            buttons = Button(master=root, text=letter, command=lambda letter=letter: save_letter(letter))
            buttons.place(x=50 + 50 * count1, y=350)
            count1 += 1


def make_buttons3():
    count2 = 0
    lst2 = []
    if count2 <= 6:
        for letter in 'UVWXYZ':
            lst2.append(letter)
        for letter in lst2:
            buttons = Button(master=root, text=letter, command=lambda letter=letter: save_letter(letter))
            buttons.place(x=150 + 50 * count2, y=400)
            count2 += 1


make_buttons1()
make_buttons2()
make_buttons3()

root.mainloop()