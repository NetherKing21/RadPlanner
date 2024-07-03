from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
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
            #everythingElse[subConditions[i]] is the current subcondition that is being built 
            currentSubCondition = everythingElse[subConditions[i]]
            # The subRequirements for the currentSubCondition are the next index of everythingElse till the next subCondition 
            # unless the subCondition is the last in the list in which case the subRequirements are the next index of everythingElse till the end
            if i+1 in range(len(subConditions)):
                subRequirements = everythingElse[subConditions[i]+1:subConditions[i+1]]
            else:
                subRequirements = everythingElse[subConditions[i]+1:]

            #Create subRequirement as a tuple of the currentSubCondition and a list of all its subRequirements
            subRequirement = (currentSubCondition, subRequirements)
            #That subRequirment is then added to the overall Requirements to eventually be returned as the formatted data
            requirements.append(subRequirement)

    formattedData = (condition, requirements)
    return formattedData




#Here are the test links
links = ["https://www.byui.edu/catalog/#/courses/rJuLFSw3X?group=Computer%20Science&bc=true&bcCurrent=CSE100%20-%20Introduction%20to%20Computing&bcGroup=Computer%20Science&bcItemType=courses",
            "https://www.byui.edu/catalog/#/courses/NJHlnlnoW?group=Computer%20Science&bc=true&bcCurrent=CSE453%20-%20Computer%20Security&bcGroup=Computer%20Science&bcItemType=courses",
            "https://www.byui.edu/catalog/#/courses/r1cbEzA2X?group=Computer%20Science&bc=true&bcCurrent=CSE473%20-%20Process%20Improvement&bcGroup=Computer%20Science&bcItemType=courses",
            "https://www.byui.edu/catalog/#/courses/rJy7aiD2Q?group=Computer%20Science&bc=true&bcCurrent=CSE430%20-%20Architectural%20Design&bcGroup=Computer%20Science&bcItemType=courses",
            "https://www.byui.edu/catalog/#/courses/N1l4e2e2iW?group=Computer%20Science&bc=true&bcCurrent=CSE450%20-%20Machine%20Learning&bcGroup=Computer%20Science&bcItemType=courses"]

startTime = time.time()
timePerLink = []
counter = 0


for link in links:
    tempStartTime = time.time()
    counter += 1
    print(f'Processing link {counter}...')

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
        #if there are no prerequisites save the link and null to the file
        with open('prerequisitesTest.txt', 'a') as file2:
            if prerequisites == 'null':
                file2.write(f"{link}, {prerequisites}\n")
            #If there are prerequisites then format the data then save the link and the formatted data
            else:
                formattedData = f'{formatData(prerequisites)}'
                #replace commas with ;
                formattedData = formattedData.replace(',', ';')
                file2.write(f'{link}, {formattedData}\n')


        tempEndTime = time.time()
        timeToComplete = tempEndTime - tempStartTime
        timePerLink.append(timeToComplete)

        print(f"Finished Link {counter}")
        print(f"Time: {timeToComplete:.2f}")

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

