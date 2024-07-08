# file_path = 'Courses.txt'
file_path = 'CoursesWithPrerequisites.txt'

def findGroupOfCourses(search_group):
    with open(file_path, 'r') as file:
        count = 0
        for line in file:
            parts = line.strip().split(',')
            group = parts[0]
            nameAndCode = parts[1]
            link = parts[2]
            if (group == search_group):
                count += 1
                print(line)
        print(f'Found {count} classes')

# findGroupOfCourses("Computer Science")

def replaceCommasInDescription():
    with open("CoursesCleaned.txt", "w") as newFile:
        with open(file_path, "r") as file:
            for line in file:
                newLine = ''
                isDescription = False
                commaCount = 0
                for char in line:
                    if char == '"' and isDescription:
                        isDescription = False
                    elif char == '"' and not isDescription:
                        isDescription = True
                    
                    if char == ',':
                        commaCount += 1 

                    if (char == ',' and isDescription) or (char == ',' and commaCount > 5):
                        newLine += "~"
                    else:
                        newLine += char
                newFile.write(newLine)
            
# replaceCommasInDescription()

def checkLineOfFile():
    incorrectLines = []
    lineCount = 1
    with open(file_path, "r") as file:
        for line in file:

            parts = line.split(",")

            if len(parts) != 7:
                lineInfo = (lineCount, len(parts))
                incorrectLines.append(lineInfo)

            lineCount += 1
    
    if len(incorrectLines) == 0:
        print("All lines are correct")
    else:
        for incorrectLine in incorrectLines:
            print(f"Line {incorrectLine[0]} has {incorrectLine[1]} parts")
        print(f"There are {len(incorrectLines)} lines that are incorrect")

# checkLineOfFile()
            
def findLongestURL():
    urlLengths = []
    with open("CoursesCleaned.txt") as file:
        for line in file:
            parts = line.strip().split(',')
            url = parts[4]
            urlLengths.append(len(url))
    longestURL = max(urlLengths)
    averageLength = sum(urlLengths)/len(urlLengths)
    print(f'The longest URL is {longestURL}')
    print(f'The average length is {averageLength}')

# findLongestURL()


def prerequisiteData():
    lengthOfPrerequisites = []
    with open("CoursesWithPrerequisitesFixed.txt", "r") as file:
        for line in file:
            parts = line.strip().split(',')
            prerequisite = parts[6].strip().replace(";", ",")
            lengthOfPrerequisites.append(len(prerequisite))

    largest = max(lengthOfPrerequisites)
    lineNumber = lengthOfPrerequisites.index(largest) + 1
    print(f'Line {lineNumber} has the largest prerequisites')


# prerequisiteData()

def fixDoubleQuotes():
    with open("CoursesWithPrerequisites.txt") as file:
        with open("CoursesWithPrerequisitesFixed.txt", 'w') as file2:
            for line in file:
                lineText = f'{line}'
                fixedLine = lineText.replace('""', '"', 1)
                file2.write(fixedLine)
            
# fixDoubleQuotes()

