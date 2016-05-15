#   Latin Insult Generator.py
#   Author: Gloria
#
#   A program that randomly creates insults with Latin
#   adjectives and nouns. It either uses masculine or
#   feminine words based on the user's choice. 
#

import random

print"This randomly generates an insulting phrase in Latin by combining a noun and adj."
print"Nota Bene: Insults are created in the nominative case."
print""

#Translation of adjectives and nouns.
adjTrans = ['stupid', 'ugly', 'big', 'that darned', 'vile', 'annoying', 'mean', 'accursed']     
nounTrans = ['cow', 'kid', 'person', 'snake', 'mule', 'horse', 'beast', 'jackal', 'slug', 'dolphin', 'demon', 'worm']

#Handles masculine insults.
def insultMasc(adjIndex, nounIndex, adjTrans, nounTrans):
    #Hardcoded lists of adjectives and nouns.
    mascAdj = ['stultus' , 'foedus', 'magnus', 'iste', 'vilis', 'incommodus', 'caninus', 'sacer']
    mascNoun = ['vison', 'puer', 'homo', 'anguis', 'mulus', 'equus', 'ferus', 'canes', 'limax', 'delphinus', 'daemon', 'cossis']
    
    adj = mascAdj[adjIndex]
    noun =  mascNoun[nounIndex]

    #This allows for the translation to occur.
    transA = adjTrans[adjIndex]
    transN =  nounTrans[nounIndex]
        
    print adj,noun
    print transA, transN

#Handles feminine insults.
def insultFem(adjIndex, nounIndex, adjTrans, nounTrans):
    femAdj = ['stulta', 'foeda','magna', 'ista', 'vilis', 'incommoda', 'canina', 'sacra']
    femNoun = ['bos', 'puella', 'homo', 'serpens', 'mula', 'equa', 'bestia', 'canes', 'limax', 'delphina', 'lamia', 'cantharis']
    
    adj = femAdj[adjIndex]
    noun =  femNoun[nounIndex]

    transA = adjTrans[adjIndex]
    transN =  nounTrans[nounIndex]
        
    print adj,noun
    print transA, transN

#Allows a user to generate an insult in the gender of their choice.
def chooseGender():
    while True:                 #Allows insults to be generated without restarting the interpreter.
        choice = raw_input("Do you want an insult declined in the masculine or feminine gender? Type 'm' or 'f'.")
        choice = choice.lower()

        #Randomizes the index to randomly select words.
        adjIndex = random.randint(0, 7)
        nounIndex = random.randint(0, 11)
        
        #Calls method for appropriate gender.
        if(choice ==  'm'):
            insultMasc(adjIndex, nounIndex, adjTrans)
        elif(choice == 'f'):
            insultFem(adjIndex, nounIndex, adjTrans, nounTrans)

        loop = raw_input("Generate again? Type 'y' if so. Any other key to quit.")
        loop = loop.lower()
        if(loop == 'y'):
            chooseGender()
        else: 
            break                       #Ends program by breaking out of while loop.
    
chooseGender()
