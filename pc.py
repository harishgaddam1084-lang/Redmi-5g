from itertools import permutations
def word_combinations(word):
    y= 0
    for p in permutations(word):
        y+=1
        combined_word = ''.join(p)
        print(y,":",combined_word)
        	

input_word= input("enter your word : ")
word_combinations(input_word)
