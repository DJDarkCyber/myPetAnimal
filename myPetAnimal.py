#!/usr/bin/env python3

from email.headerregistry import ParameterizedMIMEHeader
import random
import time
import threading
from traceback import print_exc

usrStatus = {"money": 500, "yourPet": " "}
allPets   = {"cat": 300, "dog": 1200, "snake": 670, "squirrel": 50, "ghost": 10000, "chicken": 50}
usrFridge = {}

def petAnimals():
    print("+----------------+---------+")
    print("| Pet Animals    | Price   |")
    print("+----------------+---------+")
    print("|    Cat         | ₹ 300   |")
    print("+----------------+---------+")
    print("|    Dog         | ₹ 1200  |")
    print("+----------------+---------+")
    print("|   Snake        | ₹ 670   |")
    print("+----------------+---------+")
    print("|   Squirrel     | ₹ 250   |")
    print("+----------------+---------+")
    print("|    Chicken     | ₹ 50    |")
    print("+----------------+---------+")
    print("|     Ghost      | ₹ 10000 |")
    print("+----------------+---------+")
    
    
def displayHelp(usrCmd):
    try:
        temp = usrCmd[1]
    except Exception:
        print("buy <pet>   --> Buy Pets")
        print("foodstore   --> Print's Food Store")
        print("feed        --> Used to feed your pet")
        print("fridge      --> Display bought food items")
        print("help        --> Display's Help")
        print("help <cmd>  --> Display's help For The Specific command")
        print("money       --> Display's Your Money")
        print("mypet       --> Display's Your Current Pet")
        print("pets        --> Display's All Available Pets")
        print("petstatus   --> Display's Pet's Statuss")
        print("removepet   --> Remove your current pet")
        print("work <work> --> Work ")
        print("works       --> Display's Available Works!")
    try:
        if usrCmd[1] == "pets":
            print("-"*10)
            print(">_ pets")
            print()
            print("This command is used to display all available pets")
            print("Example : \n")
            print(">_ pets\n")
            print("-"*10)
        elif usrCmd[1] == "money":
            print("-"*10)
            print(">_ money\n")
            print("This command is used to display your pocket money")
            print("Example : \n")
            print(">_ money\n")
            print("-"*10)
        elif usrCmd[1] == "buy":
            print("-"*10)
            print(">_ buy <petName>\n")
            print("This command is used to buy a pet")
            print("Note: You can only buy only one pets")
            print("Example : \n")
            print(">_ buy cat\n")
            print("-"*10)
        elif usrCmd[1] == "mypet":
            print("-"*10)
            print(">_ mypet\n")
            print("This command is used to display the current pet")
            print("Example : \n")
            print(">_ mypet\n")
            print("-"*10)
        elif usrCmd[1] == "fridge":
            print("-"*10)
            print(">_ fridge\n")
            print("This command is use to display contents of the fridge")
            print("Example :\n")
            print(">_ fridge\n")
            print("-"*10)
        elif usrCmd[1] == "foodstore":
            print("-"*10)
            print(">_ foodstore display   --> Display's the contents of the foodstore")
            print(">_ foodstore buy       --> To buy item")
            print("Example :\n")
            print(">_ foodstore display")
            print(">_ foodstore buy\n")
            print("-"*10)
        elif usrCmd[1] == "petstatus":
            print("-"*10)
            print(">_ petstatus")
            print("This command used to display current status about your pet")
            print("Example :\n")
            print(">_ petstatus\n")
            print("-"*10)
        elif usrCmd[1] == "removepet":
            print("-"*10)
            print("This command is use to remove you pet!")
            print(">_ removepet")
            print("Example :\n")
            print(">_ removepet\n")
            print("-"*10)
        elif usrCmd[1] == "feed":
            print("-"*10)
            print(">_ feed <item>")
            print("This command is used to feed food for your pet to keep alive")
            print("Example :\n")
            print(">_ feed strawberries\n")
            print("-"*10)
        elif usrCmd[1] == "help":
            print("-"*10)
            print("This command is used to display available commands and help")
            print(">_ help")
            print("Example : \n")
            print(">_ help buy\n")
            print("-"*10)
        elif usrCmd[1] == "works":
            print("-"*10)
            print(">_ works")
            print("This command is used to display all available works")
            print("Example :\n")
            print(">_ works\n")
            print("-"*10)
        elif usrCmd[1] == "work":
            print("-"*10)
            print(">_ work")
            print("This command is used to go for work")
            print("Example :\n")
            print(">_ work police\n")
            print("-"*10)
        else:
            print("Oops! Something went wrong")
    except Exception:
        pass

def displayMoney():
    print("Your current Money : ₹ " + str(usrStatus["money"]))
    
def currentPet():
    if usrStatus["yourPet"] == " ":
        print("Your didn't own any pet :/")
    else:
        print("Your current Pet : " + str(usrStatus["yourPet"]))

def buyPets(usrCmd):
    if usrStatus["yourPet"] != " ":
        print("You already own a pet!")
        return 0
    usrPet = ""
    try:
        if usrCmd[1] == "cat":
            usrPet = "cat"
        elif usrCmd[1] == "dog":
            usrPet = "dog"
        elif usrCmd[1] == "snake":
            usrPet = "snake"
        elif usrCmd[1] == "squirrel":
            usrPet = "squirrel"
        elif usrCmd[1] == "ghost":
            usrPet = "ghost"
        elif usrCmd[1] == "chicken":
            usrPet = "chicken"
        else:
            print("Pet not available!")
            return 0
    except Exception:
        pass
    petPrice = allPets[usrPet]
    
    if petPrice > usrStatus["money"]:
        print("You don't have enough money to buy :/")
        return 0
    else:
        usrStatus["money"] = usrStatus["money"] - petPrice
        usrStatus["yourPet"] = usrPet
        print("Pet Bought Successfully!")
        
def displayWorks():
    print("+------------------+---------+")
    print("| Available Works  | Earn    |")
    print("+------------------+---------+")
    print("|     Solver       | ₹ 5     |")
    print("+------------------+---------+")
    print("|    Police        | ₹ 150   |")
    print("+------------------+---------+")
    print("|    Slave         | ₹ 25    |")
    print("+------------------+---------+")
    print("|    Wife          | ₹ 20    |")
    print("+------------------+---------+")
    print("|      Helper      | ₹ 100   |")
    print("+------------------+---------+")

def solver():
    words = ["hey, How are you!", "Call me at evening", "I am going for vaccation",
             "Hope you are doing fine", "Where do you kept my pc", "We will back soon",
             "What has changed?", "We came back", "Hello", "What are you doing now?",
             "Let's Go out", "Shall we meet at Shop?"]
    randNum = random.randint(0, len(words) - 1)
    randWord = words[randNum]
    trickyWord = ""
    print("hello")
    for mywords in randWord:
        randBool = random.randint(0, 3)
        if randBool == 0:
            randDig = random.randint(0, 9)
            trickyWord += mywords
            trickyWord += str(randDig)
        else:
            trickyWord += mywords
    print(trickyWord)
    usrWord = str(input("Enter the corrected message : "))
    if usrWord == randWord:
        print("Modi : I am proud to hire you!. Here it is, take your money")
        print("Modi Gave you ₹5 for solving his message!")
        usrStatus["money"] += 5
        return 0
    else:
        print("Modi : You damn idiot! You are fired from this job")
        usrStatus["money"] = 0
        return 0

def policeWork():
    randomNum = random.randint(1, 1000)
    tries = 10
    while tries != 0:
        usrGuess = input("Enter the house number to check : ")
        if usrGuess.isdecimal() == False:
            print("There are only door numbers")
        elif usrGuess == randomNum:
            print("You found the thief and arrested in jail")
            print("You got paid ₹150 for this Job")
            usrStatus["money"] += 150
            return 0
        elif int(usrGuess) > 1000 or int(usrGuess) < 1:
            print("Are you mad? You went of the street. Check the house door numbers between 1 and 1000")
        elif int(usrGuess) > randomNum:
            print("House Guy : I think, you need to check house with lower door number than me :/")
            tries -= 1
        elif int(usrGuess) < int(randomNum):
            print("House Guy : I think, you need to check house with higher door number than me :/")
            tries -= 1
        
    print()
    print("The theif shoot you in the head!")
    usrStatus["money"] = 0
    return 0

def slaveWork():
    print("Press <Enter> to continue")
    input()
    secretNum = random.randint(600000000, 699999999)
    print("\rThe Secret Agency says : " + str(secretNum), end=" ")
    time.sleep(10)
    usrRep = int(input("\rThe Kings Ask you : What does the secret code number said by secret agency? : "))
    if usrRep == secretNum:
        print("King : You done a wonderful Job as slave!")
        print("You got paid ₹25 for working as slave")
        usrStatus["money"] += 25
        return 0
    else:
        print("King to Soldier: Hang this slave ")
        usrStatus["money"] = 0
        return 0

def wifeWork():
    print("Press <Enter> to continue")
    input()
    words = ["All worries are less with wine", "Cooking is about surrender", "Cooking is an art and also science", 
             "whatever the soup is getting cold", "No one became a great cook just by reading recipes", "I am no longer a wife except by legal fiction",
             "The pleasant thing a wife can do is to please her husband", "A happy husband makes a happy home", "He is not an ideal husband I am his wife"]
    randQuote = random.randint(0, len(words) - 1)
    print("\rRemeber This : " + str(words[randQuote]), end=" ")
    time.sleep(10)
    print("\r" + " "*100, end=" ")
    usrRep = str(input("\rEnter the Quote >_ ")).lower()
    if usrRep == words[randQuote].lower():
        print("Husband : I am happy to have you as my wife!")
        print("You got ₹20")
        usrStatus["money"] += 20
        return 0
    else:
        print("Crap!, Your husband stolen your  purse and kicked you out :/")
        usrStatus["money"] = 0
        return 0
    
def helperWork():

    # [Gaming, Music]    
    category = ["Gaming", "Music", "Languages", "Geography"]
    # [[Gaming Questions], [Music Questions]]
    question = [["Ηοrizοn: Zеrο Dаѡn: Whаt is thе nаmе οf thе hеаⅾpiеcе thаt hеlps Alοу hυnt аnⅾ fight еаsiеr?", "Whаt is Bеаrⅾο's pеrsοnаlitу", "Animal Grossing : Whаt is Tοm's Ьirthⅾау (mοnth nаmе fοllοѡеⅾ Ьу ⅾау nυmЬеr)"], #Gaming
                
                ["ѡhο rеlеаsеⅾ 'timе, lοѵе аnⅾ tеnⅾеrnеss' in 1981", "Nаmе Thе Artist: Rυnаrουnⅾ Sυе", "Nаmе Thе Artist: Ηi‐Dе‐Ηο", "Nаmе Thе ʏеаr: ᛖichаеl Jаcksοn, singеr, Ьοrn.", "Bеаtlеs First Wοrⅾs: First ѡοrⅾ οf \"Dау Trippеr\"", "ѡith ѡhich sοng ⅾiⅾ frаnkiе аѵаlοn Ьеgin his cаrееr"],   # Music
                
                ["(Ⅰt.) ‐ A rеst (nοt а pаυsе).", "(Ԍеr.) ‐ Lightlу."], # Languages
                
                ["Thе Sουthеrn Alps аrе fουnⅾ in ѡhich cουntrу", "Which citу hοstеⅾ thе 1960 Olуmpic Sυmmеr Ԍаmеs Ηеlⅾ"]] # Geography
    # [[Gaming Answers], [Music Answers]]
    answers  = [["Focus", "Smug", "December 10"], # Gaming
                ["Michael bolton", "Leif garrett", "Blood, sweat and tears", "1958", "Got", "Dede dinah"], # Music 
                ["Pausa", "Leicht"], # Languages
                ["New zealand", "Rome"]] # Geography
    # [[Gaming Clues], [Music Clues]]
    # [[[Gaming Clue Qns1], [Gaming Clue Qns2]], [[Music Clue Qns1], [Music Clue Qns2]]]
    clues    = [[["5 letters long. Starts with 'F' and ends with 's'", "Pig Latin: ocusfay"], ["Similar to Curlos", "Not like Cleo"], ["Twelvth month of the year", "Day is \"x\": 50 - x = 40\n<month> <day>"]], # Gaming
                
                [["Scrambled Answer : monlclb hoitae", "Pig Latin: ichaelmay oltonbay"], ["Scrambled Answer: aetrir efgtl", "Pig Latin: eiflay arrettgay"], ["B####, ##### ### #####", "Pig Latin: ood,blay eatsway anday earstay"], ["Year first McDonald's opened in Illinois, plus minimum people needed for a riot", "Octal: 3646"], ["3 letters long. Starts with \'G\' and ends with \'t\'.", "Pig Latin: otgay"], ["9 letters long. Starts with 'D' and ends with 'h'.", "Pig Latin: ededay inahday"]], # Music
                
                [["P####", "Pig Latin: ausapay"], ["L#####", "Pig Latin: eichtlay"]], # Languages
                
                [["Scrambled Answer: lnaadznee w", "Pig Latin: ewnay ealandzay"], ["R###", "Pig Latin: omeray"]]] # Geography
    randCategory = random.randint(0, len(category)-1)
    randQuestion = random.randint(0, len(question[randCategory]) - 1)
    answer       = answers[randCategory][randQuestion].lower()
    print("Category : " + str(category[randCategory]))
    print("Question : \n")
    print(question[randCategory][randQuestion])
    print()
    print("Clue 1 : " + clues[randCategory][randQuestion][0])
    print("Clue 2 : " + clues[randCategory][randQuestion][1])
    tries = 3
    while tries != 0:
        print("Tries left : " + str(tries))
        usrInp = input("Your Answer >_ ").lower()
        if usrInp == answer:
            print("Correct Answer")
            print("You earned ₹100")
            usrStatus["money"] += 100
            return 0
        tries -= 1
    print(answer)
    print("Great! The guy who hired you got failed in his exam. He kicked on your head and your face rolled away from this Earth")
    usrStatus["money"] = 0
    return 0
    
def workForMoney(usrCmd):
    try:
        if usrCmd[1] == "solver":
            print("Modi has some difficulties while chatting with some one. He used to press some numbers in his keybaord accidently")
            print("You are hired to solve his message in readable form. Do worry brb, you will get paid for this work!")
            print("\nNote : Messages are case sensitive and also don't mis special character too\n")
            solver()
        elif usrCmd[1] == "police":
            print("You got a call from a village, saying, \"Hey I saw a theif that you guys looking for decays is in the terrain Street\"")
            print("You took your jeep and went to the street and you found 1000 houses in that street(each house has door number from 1 to 1000). Find the thief!")
            policeWork()
        elif usrCmd[1] == "slave":
            print("Now you are the slave for the King. King has difficulties in remembering the codes told by other secret agencies.")
            print("Your only job is to remeber the secret code said by the secret agencies and tell to king whenever the king asks to you!")
            
            slaveWork()
        elif usrCmd[1] == "wife":
            print("You are now a wife. You need to remember something to be a good wife")
            wifeWork()
        elif usrCmd[1] == "helper":
            print("Due to the online exams, a guy hired you to help him with test. You just need to answer the questions\n\n")
            time.sleep(3)
            helperWork()
        else:
            print("Invalid Work")
    except Exception:
        pass

def myLocalShop(usrWish, viewItems=False):
    if usrWish[1] == "display":
        viewItems = True
    if viewItems == True:
        print("1. Strawberries             --> ₹50")
        print("2. Fromm Gold Nutrition     --> ₹1257")
        print("3. Greeines SmarBites Skin  --> ₹130")
        print("4. Diamond Natural Beef     --> ₹1300")
        print("5. 4-star Duck Veg Dry      --> ₹370")
        print("6. Marshall                 --> ₹820")
        print("7. eCotrition               --> ₹240")
        return
    myItems    = ["Strawberries", "Fromm Gold Nutrition", "Greeines SmarBites Skin", "Diamond Natural Beef", 
                "4-star Duck Veg Dry", "Marshall", "eCotrition"]
    itemsVal = [50, 1257, 130, 1300, 370, 820, 240]
    if usrWish[1] == "buy":
        while True:
            usrBuy = input("Enter an Item number to buy >_ ")
            if usrBuy.isdecimal() == False:
                print("Please enter the item number!")
            elif int(usrBuy) > 7:
                print("Invalid Item!")
            elif int(usrBuy) < 1:
                print("Invalid Item!")
            else:
                break
    if usrStatus["money"] < itemsVal[int(usrBuy) - 1]:
        print("You Don't have enough money to buy " + str(myItems[int(usrBuy) -1]) + "!")
    else:
        usrStatus["money"] -= itemsVal[int(usrBuy) - 1]
        if myItems[int(usrBuy) -1] in usrFridge.keys():
            usrFridge[myItems[int(usrBuy) -1]] += 1
        else:
            usrFridge[myItems[int(usrBuy) -1]] = 1
        print("Bought Succesfully")

def displayFridge():
    for usrs in usrFridge.keys():
        print(str(usrs) + "    > " + str(usrFridge[usrs]))
petHealth   = 100
petStomach  = 100
petStamina  = 100
def petAnimalStatusUpdater():
    global petHealth
    global petStomach
    global petStamina
    while True:
        if usrStatus["yourPet"] == " ":
            pass
        else:
            while True:
                time.sleep(10)
                randGen = random.randint(1, 4)
                if randGen == 1:
                    petHealth -= 2
                elif randGen == 2:
                    petStamina -= 2
                else:
                    petStomach -= 2
                if petHealth <= 0 or petStomach <= 0 or petStamina <= 0:
                    print("Pet died")
                    petHealth  = 100
                    petStomach = 100
                    petStamina = 100
                    usrStatus["yourPet"] = " "
                    break

def petAnimalStatusDisplay():
    if usrStatus["yourPet"] == " ":
        print("Please won a pet")
        return 
    print("Pet Health   > " + str("█"*(petHealth//10)) + "   " + str(petHealth))
    print()
    print("Pet Hunger   > " + str("█"*(petStomach//10)) + "   " + str(petStomach)) 
    print()
    print("Pet Stamina  > " + str("█"*(petStamina//10)) + "   " + str(petStamina))

def removePet():
    if usrStatus["yourPet"] == " ":
        print("First own a pet and decide to kick it out of your house")
        return
    while True:
        usrRep = input("Do you want to really miss your " + str(usrStatus["yourPet"]) + "? (Y/N)").lower()
        if usrRep == "n":
            print("Nice decision!")
            return
        elif usrRep == "y":
            print("You kicked your pet away from your house!")
            usrStatus["yourPet"] = " "
            return
        else:
            pass

def feedPet(usrCmd):
    global petHealth
    global petStomach
    global petStamina
    if usrStatus["yourPet"] == " ":
        print("First buy a pet to feed!")
        return
    allItems = ["strawberries", "fromm", "greeines", "diamond", "4-star", "marshall", "ecotrition"]
    orgItems = ["Strawberries", "Fromm Gold Nutrition", "Greeines SmarBites Skin", "Diamond Natural Beef", 
                "4-star Duck Veg Dry", "Marshall", "eCotrition"]
    usrFridgeItems = []
    for usrItems in usrFridge.keys():
        for myIndex, word in enumerate(usrItems):
            if word == " ":
                usrItems = usrItems[:myIndex]
                break
        usrItems = usrItems.lower()
        usrFridgeItems.append(usrItems)
    if usrCmd[1].lower() not in usrFridgeItems:
        print("Item not available in your 'fridge'")
        return
    else:
        pass
    if usrCmd[1] == allItems[0]:
        petHealth  += 10
        petStomach += 20
        petStamina += 5
        usrFridge[orgItems[0]] -= 1
        if usrFridge[orgItems[0]] == 0:
            usrFridge.pop(orgItems[0])
    elif usrCmd[1] == allItems[1]:
        petHealth  += 80
        petStomach += 80
        petStamina += 80
        usrFridge[orgItems[1]] -= 1
        if usrFridge[orgItems[1]] == 0:
            usrFridge.pop(orgItems[1])
    elif usrCmd[1] == allItems[2]:
        petHealth  += 30
        petStomach += 40
        petStamina += 20
        usrFridge[orgItems[2]] -= 1
        if usrFridge[orgItems[2]] == 0:
            usrFridge.pop(orgItems[2])
    elif usrCmd[1] == allItems[3]:
        petHealth  += 90
        petStomach += 90
        petStamina += 90
        usrFridge[orgItems[3]] -= 1
        if usrFridge[orgItems[3]] == 0:
            usrFridge.pop(orgItems[3])
    elif usrCmd[1] == allItems[4]:
        petHealth  += 40
        petStomach += 60
        petStamina += 70
        usrFridge[orgItems[4]] -= 1
        if usrFridge[orgItems[4]] == 0:
            usrFridge.pop(orgItems[4])
    elif usrCmd[1] == allItems[5]:
        petHealth  += 60
        petStomach += 78
        petStamina += 50
        usrFridge[orgItems[5]] -= 1
        if usrFridge[orgItems[5]] == 0:
            usrFridge.pop(orgItems[5])
    elif usrCmd[1] == allItems[6]:
        petHealth  += 40
        petStomach += 60
        petStamina += 50
        usrFridge[orgItems[6]] -= 1
        if usrFridge[orgItems[6]] == 0:
            usrFridge.pop(orgItems[6])
    else:
        print("Terrible happened!")
    
    if petHealth > 100:
        petHealth = 100
    if petStomach > 100:
        petStomach = 100
    if petStamina > 100:
        petStamina = 100
    print("Feeded!")

def main():
    try:
        usrCmd = str(input(">_ ")).lower().split(" ")
        if usrCmd[0] == "help":
            displayHelp(usrCmd)
        elif usrCmd[0] == "pets":
            petAnimals()
        elif usrCmd[0] == "money":
            displayMoney()
        elif usrCmd[0] == "buy":
            buyPets(usrCmd)
        elif usrCmd[0] == "mypet":
            currentPet()
        elif usrCmd[0] == "works":
            displayWorks()
        elif usrCmd[0] == "work":
            workForMoney(usrCmd)
        elif usrCmd[0] == "fridge":
            displayFridge()
        elif usrCmd[0] == "foodstore":
            myLocalShop(usrCmd)
        elif usrCmd[0] == "petstatus":
            petAnimalStatusDisplay()
        elif usrCmd[0] == "removepet":
            removePet()
        elif usrCmd[0] == "feed":
            feedPet(usrCmd)
        else:
            print("Type 'help' to see available commands")
    except Exception:
        print("Something went wrong :/, Type 'help " + str(usrCmd[0]) + "'")
        
th1 = threading.Thread(target=petAnimalStatusUpdater)
th1.start()
while True:
    main()
