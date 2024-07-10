import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(f'Pssst, the solution is {chosen_word}.')

lives = 6
found_word = False
underscore = "_"
display = [underscore] * len(chosen_word)
print(" ".join(display))

already_guessed = []
while underscore in display and lives > 0:
  found_word = False
  guess_letter = input("Guess a letter:").lower()
  if guess_letter in already_guessed:
    print("You have already guessed this letter")
  else:
    already_guessed.append(guess_letter)
  
  index = 0
  while index < len(chosen_word):
    if chosen_word[index] == guess_letter:
      display[index] = guess_letter
      found_word = True
    index += 1

  if found_word == False:
    print(f"{guess_letter} letter is not found in the word. You lose a life.")
    lives -= 1
    print(hangman_art.stages[lives])
    
  print(" ".join(display))

if lives > 0:
  print("You Won")
else:
  print("You Lose")
