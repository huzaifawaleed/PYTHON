# Exercise 4.

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

while True:
    print("---Secret Coding Language--")
    print("1: Code")
    print("2: Decode")
    print("3: Exit")
    opt = int(input("Select the option: "))  
    
    match opt:
        case 1:
            word = input("Enter a word: ")

            if len(word) <= 3:
              rev_word = word[:: -1]
              print("The Code Word is = ",rev_word)
            else:
              modified = word[1:] + word[0]
              random_start = ''.join(random.choices(string.ascii_lowercase, k=3))
              random_end = ''.join(random.choices(string.ascii_lowercase, k=3))
              modified = random_start + modified + random_end
              print("The Code Word is", modified)
        case 2:
          word2 = input("Enter a word: ")
          if len(word2) <= 3:
             word_rev = word2[:: -1] 
             print("The Decode Word is = ",word_rev)  
          else:
             new = word2[3:-3]
             new2 = new[-1] + new[:-1]
             print("The Decode Word is ",new2)   
        case 3:
          print("Thank You For Using!")
          break


0...................................................