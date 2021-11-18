letter='''Dear <NAME>,
you are selected !
Date:<date>
'''
name= input("Enter your name:")
date = input("Enter Date:")
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)