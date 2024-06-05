# Installation:

# py -m pip install webdriver-manager
# py -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



try:

    # Run without a GUI.  Note that the script didn't work
    # with Chrome without a GUI.  Firefox was successful.

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)


    # Read the courses website

    driver.get("https://www.byui.edu/catalog/#/courses")



    # Find all the course groups from the courses website

    groups = []

    buttons = driver.find_elements(By.XPATH,"//button[contains(@aria-label,'show')]")

    for button in buttons:

        groups.append(button.get_attribute("aria-controls"))


    print(f"Found {len(groups)} course groups.")

    print()

    # Find all the courses for each group.  There were 2 options here:
    # 1) Click on the buttons found above.  Tried this with mixed results.  It would often fail.
    #    There seemed to be a timing issue.
    # 2) Open up the course list page based on the course group name

    courses = []

    for group in groups:

        print(f"Processing: {group}")

        driver.get(f"https://www.byui.edu/catalog/#/courses/?group={group}")



        # Find the link for each course.  From the link, we can get the name of the course
        # and the link to the course information

        links = driver.find_elements(By.XPATH,"//a[contains(@href, 'bcItemType=courses')]")

        for link in links:

            courses.append((group,link.text,link.get_attribute("href")))

    # Display all of the courses.

    print()

    print("All Courses:")

    for course in courses:

        print(course)

    print()

    print(f"Total Courses: {len(courses)}")

    # Next step would be accessing specific courses by going to the links stored in the list above

    if (len(courses) > 0):
        with open("webPage.txt", "w") as file:
            file.write("Course Groups: ")
            file.write("\n".join(groups))
            file.write("")
            file.write("Courses: \n")
            for course in courses:
                group = course[0]
                nameAndCode = course[1]
                link = course[2]
                file.write(f'{group}, {nameAndCode}, {link}\n')


except Exception as e:
    print(e)

finally:
    driver.quit()