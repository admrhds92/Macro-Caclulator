import tkinter


#Main function
def main():
    greetUser()
    printResults()

#Gathers users age
def getAge():
    age = int(input("What is your age? \n"))
    return age

#Gathers users gender
def getGender():
    gender = input("Are you male or female? M/F? \n")
    return gender

#Gathers users height
def getHeight():
    heightPref = input("Do you prefer ft or cm?")
    heightInCm = 0
    if heightPref == "ft":
        heightInFeet = input("How tall are you? Feet? \n")
        heightInInches = input("and how many inches? \n")
        heightInInches = int(heightInInches) * 0.1
        heightSum = int(heightInFeet) + (heightInInches)
        heightInCm = heightSum * 30.48
    elif heightPref == "cm":
        heightInCm = float(input('How many cm\'s tall are you?'))
    return heightInCm

# Gets weight in either kgs or lbs
def getWeight():
    weightPref = input('Do you prefer lbs or kg?')
    weightToKg = 0
    if weightPref == "lbs":
        weight = input("How much do you weigh in lbs \n")
        weightToKg = int(weight) / 2.205

    elif weightPref == "kg":
        weight = input("How much do you weigh in kilograms?")
        weightToKg = float(weight)

    return weightToKg

# asks the user about their activity level and assigns a multiplier based on activity level
def getActivity():
    activity = int(input("Choose your activity (1-5) \n 1. Sedentary\n 2. Lightly active\n 3. Moderately active\n 4. Very active\n 5. Extremely active \n"))

    activityMultiplier = 0
    if activity == 1:
        activityMultiplier = 1.2
    elif activity == 2:
        activityMultiplier = 1.375
    elif activity == 3:
        activityMultiplier = 1.55
    elif activity == 4:
        activityMultiplier = 1.725
    elif activity == 5:
        activityMultiplier = 1.9
    else:
        print("Not valid input")

    return activityMultiplier

#Calculates macros based on return of previous functions
def calculateMacros():

    macroCalc = 0

    getGender()

    if getGender == "M" or getGender == "m" or getGender == "Male" or getGender == "male":
        macroCalc = (10 * getWeight()) + (6.25 * getHeight()) - (5 * getAge()) + 5
    else:
        macroCalc = (10 * getWeight()) + (6.25 * getHeight()) - (5 * getAge()) - 161

    macroCalc = round(macroCalc * getActivity(), 2)
    


    # userGoal = input("Are you looking to lose weight (1), gain weight (2), or maintain weight (3).")
    # if userGoal == '1' or userGoal ==  'lose weight':
    #     macroCalc *= .8
    # elif userGoal == '2' or userGoal == 'gain weight':
    #     macroCalc *= 1.2
    # else:
    #     pass

    return macroCalc



def greetUser():
    print("************************************************************")
    print("*** Lets see how many calories you should have in a day! *** ")
    print("************************************************************\n\n")

def printResults():
    finalResults = calculateMacros()
    print("You should consume " + str(finalResults) + " calories a day to maintain your weight")
    print("To lose weight you should try to consume " + str(finalResults * .8) + " calories a day")
    print("To gain weight you should try to consume " + str(finalResults * 1.2) + " calories a day")

main()



