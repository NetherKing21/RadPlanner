from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Open file and start searching 
file_path = 'CoursesCleaned.txt'
with open(file_path, 'r') as file:

    for line in file:
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

            driver.get(f'{link}')

            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "noBreak")))
            try:
                prerequisites = driver.find_element(By.XPATH, "")
            except:
                prerequisites = 'null'

            with open("Courses.txt", "a") as file2:
                course_info = f'{code}, {name}, {credits}, {group}, {link}, "{description}"\n'
                file2.write(course_info)

        except Exception as e:
            print(e)

        finally:
            driver.quit()

