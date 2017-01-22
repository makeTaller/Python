#This a program that makes an Acronym of a phrase entered
# by: Kirk Tolliver

def main():
    phrase = input("Enter the Phrase to Acronynize: ")
    words = phrase.title()
    acrony = " "

    for w in words.split():
        word = w[0]
        acrony = acrony + word
    print("This Acronym is:", acrony,end=' ')
    #pre_phrase = phrase.split()
    #print(pre_phrase)
main()
