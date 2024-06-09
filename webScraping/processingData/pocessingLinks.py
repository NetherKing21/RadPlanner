from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


# Open file and start searching 
file_path = '../webPage.txt'
with open(file_path, 'r') as file:
    next(file)
    next(file)
    next(file)

    for line in file:
        parts = line.strip().split(',')
        nameAndCode = parts[1].split(" - ")

        group = parts[0].strip()
        code = nameAndCode[0].strip()
        name = nameAndCode[1].strip()
        link = parts[2].strip()

        print(f'Processing {code} - {name}...')

        try:

            # Run without a GUI.  Note that the script didn't work
            # with Chrome without a GUI.  Firefox was successful.

            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

            driver = webdriver.Firefox(options=options)
            driver.implicitly_wait(5)

            driver.get(f'{link}')

            description = driver.find_element(By.XPATH, "//div[@name='Description']//div[@class='course-view__pre___2VF54']/div").text
            credits = driver.find_element(By.XPATH, "//div[span/h3='Credits']//div[@class='course-view__pre___2VF54']/div/div").text

            description = description.replace("\n", "->")

            with open("Courses.txt", "a") as file2:
                course_info = f'{code}, {name}, {credits}, {group}, {link}, "{description}"\n'
                file2.write(course_info)

        except Exception as e:
            print(e)

        finally:
            driver.quit()

