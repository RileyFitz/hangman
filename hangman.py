from csv import reader
from random import choice

def main():
    # Load word bank
    words = get_wordbank()
    for word in words:
        print(word)

def get_wordbank():
    try:
        with open('wordbank.csv', newline='') as csvfile:
            csv_words =  reader(csvfile)
            words = list(csv_words)
            return words[0]
    except Exception as e:
        print(e)
        print("There above error occured while trying to load the wordbank..\nQuitting")
        quit()

if __name__=="__main__":
    main()
