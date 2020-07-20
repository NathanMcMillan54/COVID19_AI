from datetime import date

currentDate = date.today()

# ask person questions
print("Type in lowercase")
question = input("Have you been in contact with anybody who has COVID19? ")


# talk about how flu and COVID19 symptoms are similar
def talkAboutFlu():
    print("COVID19 symptoms are similar to flu symptoms, you should also get tested for the flu.")


# ask if a person has COVID19 symptoms
def possiblePositiveCase():
    pPC = open("possiblePositiveCase.txt", "r+")
    pPC.read()
    lines = ["\nA positive case"]
    pPC.writelines(currentDate.strftime("%d/%m/%Y"))
    pPC.writelines(lines)
    pPC.read()


def possibleNegativeCase():
    pNC = open("possibleNegativeCase.txt", "r+")
    pNC.read()
    lines = ["\nA negative case"]
    pNC.writelines(currentDate.strftime("%d/%m/%Y"))
    pNC.writelines(lines)
    pNC.read()


def ask4Symptoms():
    symptoms = input("Have you had difficulty breathing, or had a fever? ")
    if symptoms == 'yes':
        print("Get tested or quarantine")
        possiblePositiveCase()
        talkAboutFlu()
    elif symptoms == 'ya':
        print("Get tested or quarantine")
        possiblePositiveCase()
        talkAboutFlu()
    else:
        print("Ok, you probably don't need to be tested")
        possibleNegativeCase()


# ask person question
if question == 'yes':
    ask4Symptoms()
elif question == 'ya':
    ask4Symptoms()
elif question == 'i dont know':
    ask4Symptoms()
else:
    ask4Symptoms()
    print("Good")
