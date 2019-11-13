# Day Of The Programmer

# Function to check  if the year is julian leap year
def isJulianLeap(yyyy):
    return "Leap" if yyyy % 4 == 0 else "Normal"

def isGreogrianLeap(yyyy):
    return "Leap" if (yyyy % 400 == 0) or ((yyyy % 4 == 0) and (yyyy % 100 != 0)) else "Normal"

def dayOfProgrammer(yyyy):
    if yyyy == 1918:
        return "26.09.1918"
    elif 1700 <= yyyy <= 1917:
        return "12.09." + str(yyyy) if isJulianLeap(yyyy) == "Leap" else ("13.09." + str(yyyy))
    elif 1919 <= yyyy <= 2700:
        return "12.09." + str(yyyy) if isGreogrianLeap(yyyy) == "Leap" else "13.09." + str(yyyy)

print(dayOfProgrammer(int(input())))