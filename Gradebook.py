def entry():
    name = input("What's your name: ")
    subject = input("What Subject is this: ")
    year = input("What year is this grade for: ")
    percent = int(input("What percent did you get: "))
    if percent >= 91:
        grade = "A"
    elif percent >= 81:
        grade = "B"
    elif percent >= 71:
        grade = "C"
    elif percent >= 61:
        grade = "D"
    elif percent < 61:
        grade = "F"
    file = open("Add directory here", "r+")
    file.write("\n"+ name +": "+ year +", " + subject +", "+ str(percent) +", "+ grade)
    file.close()

entry()