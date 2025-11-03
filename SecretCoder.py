# CODING DECODING GAME
import random
import string

def CodingFunc(word):
    # CODING
    if len(word) == 1:
        return word
    elif len(word) == 2:
        revWord = word[::-1]
        return revWord
    elif len(word) >= 3:
        firstLetter = word[0]
        newStr = word[1:]
        newStr2 = newStr + firstLetter
        ranStart = ''.join(random.choices(string.ascii_letters, k=3))
        ranEnd = ''.join(random.choices(string.ascii_letters, k=3))
        finalStr = ranStart + newStr2 + ranEnd
        return finalStr
    else:
        return "Invalid Input!"

word = input("Enter Word : ")
Result = CodingFunc(word)
print("Coded Result : " , Result)
    

def DecodingFunc(Result):
    if len(Result) < 3:
        revWord = Result[::-1]
        return revWord
    else:
        remove_rand = Result[3:len(Result)-3]
        last_Letter = remove_rand[-1:]
        mid_Str = remove_rand[:-1]
        Decoded_Str = last_Letter + mid_Str
        return Decoded_Str

Result2 = DecodingFunc(Result)
print("Decoded Result : " , Result2)


