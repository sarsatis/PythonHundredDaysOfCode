import random
import hangman_art

words = ['sarthak', 'arch', 'divya']

stages = hangman_art.stages

random_word = random.choice(words)
print(f'random word is {random_word}')

display = []

for _ in range(len(random_word)):
    display += "_"

lives = len(stages)

print(hangman_art.logo)
while "_" in display and lives > 0:
    guess = input('Enter a letter to guess a word: ')
    if guess in display:
        print("You've already guessed that letter")
    for index, letter in enumerate(random_word):
        if guess == letter:
            display[index] = letter
    print(display)
    if guess not in random_word:
        lives -= 1
        print(f"You've guess an incorrect letter and you have {lives} remaining")
        print(stages[lives])


if lives > 0:
    print('You win')
else:
    print('You Lose')
