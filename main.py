print("Type in lowercase")
question = input("Have you been in contact with anybody who has COVID19? ")


# ask for symptoms of COVID19
def ask4Symptoms():
    symptoms = input("Have you had difficulty breathing, or had a fever? ")
    if symptoms == 'yes':
        print("Get tested or quarantine")
        talkAboutFlu()
    elif symptoms == 'ya':
        print("Get tested or quarantine")
        talkAboutFlu()
    else:
        print("Ok, you probably don't need to be tested")


# questions to determine if a person has COVID19
if question == 'yes':
    ask4Symptoms()
elif question == 'ya':
    ask4Symptoms()
elif question == 'i dont know':
    ask4Symptoms()
else:
    print("Good")
    ask4Symptoms()


# talk about flu
def talkAboutFlu():
    print("COVID19 symptoms are similar to flu symptoms, you should also get tested for the flu.")

