import random
from hangman_words import words_list
chosen_word= random.choice(words_list)
word_length= len(chosen_word)

end_of_game= False
lives=6

from hangman_art import logo
print (logo)

display=[ ]
for _ in range(word_length):
    display+="_"
    
while not end_of_game:
    guess= input("guess a letter:").lower( )
    if guess in display:
        print(f"you've already guessed {guess}")
        
    for position in range (word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"you guessed{guess}, that is notin the word. you loose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("you loose.")
    print(f"{' ' . join (display)}")
    if "_" not in display:
        end_of_game= True
        print("you win.")
    from hangman_art import stages
    print(stages[lives])