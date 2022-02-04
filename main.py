# Write your code here
import random

print('H A N G M A N')
while True:
    print('Type "play" to play the game, "exit" to quit:', end='')
    play = input()
    if play == 'play':
        break
word_list = ['python', 'java', 'kotlin', 'javascript']
true_word = random.choice(word_list)
text = '-' * len(true_word)
text = list(text)
text_set = set(true_word)
text_spam_set = set(true_word)
count = len(true_word)
text_contr = set()

num = 8
while num != 0:
    print()
    print(''.join(text))
    print('Input a letter:',end='')
    mistic_sym = input()
    
    if len(mistic_sym) != 1:
        print('You should input a single letter')
        continue
        
    if mistic_sym not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a lowercase English letter')
        continue

    if mistic_sym in text_set:
        text_set.discard(mistic_sym)
        text[true_word.find(mistic_sym)] = mistic_sym
        count -= 1
        text_contr.add(mistic_sym)
        if true_word.find(mistic_sym) >= 0:
            text[true_word.rfind(mistic_sym)] = mistic_sym
            count -= 1
    elif mistic_sym in text_contr:
        print("You've already guessed this letter")
    elif mistic_sym not in text_spam_set:
        print("That letter doesn't appear in the word")
        num -= 1    
    if len(text_set) == 0:
        print('You guessed the word', ''.join(text), '!')
        print('You survived!')
        break
    text_contr.add(mistic_sym)
else:
    print("That letter doesn't appear in the word")
    print('You lost!')
#print("Thanks for playing!")
#print("We'll see how well you did in the next stage")
