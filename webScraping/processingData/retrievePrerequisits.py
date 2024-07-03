from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Functions
def formatData(data):
    parts = data.split("\n")
    condition = parts[0] #Main initial condition
    everythingElse = parts[1:] #Everything below it (Need to find subconditions)
    subConditions = []
    requirements = []

    for i in range(len(everythingElse)): #Finds subconditions
        if "take" in everythingElse[i].lower() or "complete" in everythingElse[i].lower():
            subConditions.append(i)

    
    #Main happy path (no subconditions)
    if len(subConditions) == 0:
        requirements = everythingElse
    else: #There are subconditions
        for i in range(len(subConditions)):
            #everythingElse[subConditions[i]] is the current subCondition that is being built 
            currentSubCondition = everythingElse[subConditions[i]]
            # The subRequirements for the currentSubCondition are the next index of everythingElse till the next subCondition 
            # unless the subCondition is the last in the list in which case the subRequirements are the next index of everythingElse till the end
            if i+1 in range(len(subConditions)):
                subRequirements = everythingElse[subConditions[i]+1:subConditions[i+1]]
            else:
                subRequirements = everythingElse[subConditions[i]+1:]

            #Create subRequirement as a tuple of the currentSubCondition and a list of all its subRequirements
            subRequirement = (currentSubCondition, subRequirements)
            #That subRequirement is then added to the overall Requirements to eventually be returned as the formatted data
            requirements.append(subRequirement)

    formattedData = (condition, requirements)
    return formattedData


# Open file and start searching 
file_path = 'CoursesCleaned.txt'
with open(file_path, 'r') as file:

    #Get initial start time
    startTime = time.time()
    #List of time for all links
    timePerLink = []


    for line in file:
        #time for this link
        tempStartTime = time.time()

        parts = line.strip().split(',')
        
        code = parts[0].strip()
        name = parts[1].strip()
        credits = parts[2].strip()
        group = parts[3].strip()
        link = parts[4].strip()
        description = parts[5].strip()

        print(f'Processing {code} - {name}...')

        try:

            # Run without a GUI.  Note that the script didn't work
            # with Chrome without a GUI.  Firefox was successful.

            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

            driver = webdriver.Firefox(options=options)
            driver.implicitly_wait(5)

            #open link in driver
            driver.get(f'{link}')

            #try to find the prerequisites and save the text
            try:
                prerequisites = driver.find_element(By.XPATH, "//div[span/h3='Prerequisites']//li").text

            except Exception as somethingsWrong: #if it can't find the prerequisites say it's null
                # print(somethingsWrong)
                prerequisites = 'null'

            
            #PROCESSING THE PREREQUISITES
            #If there are prerequisites then format the data 
            if prerequisites != 'null':
                formattedData = f'{formatData(prerequisites)}'
                #replace commas with ;
                prerequisites = formattedData.replace(',', ';')

            #save course info WITH PREREQUISITES
            with open("CoursesWithPrerequisites.txt", "a") as file2:
                course_info = f'{code}, {name}, {credits}, {group}, {link}, "{description}, {prerequisites}"\n'
                file2.write(course_info)


            tempEndTime = time.time()
            timeToComplete = tempEndTime - tempStartTime
            timePerLink.append(timeToComplete)
            print(f"Finished {code} - {name} Time: {timeToComplete:.2f}")

        except Exception as e:
            print(e)

        finally:
            driver.quit()

    endTime = time.time()
    totalTimeSeconds = endTime - startTime
    hours = totalTimeSeconds // 3600
    minutes = (totalTimeSeconds % 3600) // 60
    seconds = totalTimeSeconds % 60

    averageTime = sum(timePerLink)/len(timePerLink)
    print(f"Total time: {hours} hours {minutes} minutes and {seconds:.0f} seconds")
    print(f"Average time pre link: {averageTime:.2f} seconds")

