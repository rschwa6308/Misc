from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep




def login_popup():
    try:
        username_field = driver.find_element_by_name("usernamemail")
        password_field = driver.find_element_by_name("password")

        username_field.send_keys("rschwa6308")
        sleep(1)
        password_field.send_keys("Ru5512345")
        sleep(1)
        password_field.send_keys(Keys.RETURN)
    except:
        print "No login popup"



def guess_and_advance():
    options = driver.find_elements_by_class_name("multiple-choice-question-options-option")
    option = options[0]
    option.click()


    select_button = driver.find_elements_by_class_name("unbutton")[-1]
    select_button.click()

    sleep(2)


    correct_p = driver.find_element_by_xpath('//*[@id="joyride-ie-question-list"]/div[2]/div/div/div/div/div/div/div[4]/div[3]/div[1]/div[1]/div/div/p[1]/strong')
    correct = correct_p.text[-2]

    # print correct


    next_button = driver.find_elements_by_class_name("unbutton")[-1]
    next_button.click()


    return correct




url = raw_input("Enter Url of first question: \n")


driver = webdriver.Chrome()

#driver.get("https://www.albert.io/ie/ap-art-history/function-of-prehistoric-sculpture?page=1&topic=Art%20on%20Different%20Continents&&guideLevelIds=0e1b6581-c121-427a-ac77-558356ce1bce&guideLevelId=0e1b6581-c121-427a-ac77-558356ce1bce&orderBy=difficulty")
#driver.get("https://www.albert.io/ie/ap-latin/pronoun-referent-i-64?page=1&topic=Lines%2064-80&&guideLevelIds=743b1657-7cf6-43c8-b177-ce15c2b78301&guideLevelId=743b1657-7cf6-43c8-b177-ce15c2b78301&orderBy=difficulty")
#driver.get("https://www.albert.io/ie/ap-computer-science-a/equivalent-methods-using-a-string-parameter?page=1&topic=Problem%20analysis&&guideLevelIds=a12345f7-0682-4c88-bea5-98e49d17709d&guideLevelId=a12345f7-0682-4c88-bea5-98e49d17709d&orderBy=difficulty")
#driver.get("https://www.albert.io/ie/ap-latin/metrical-pattern-ii-609?page=1&topic=Lines%20588-620&&guideLevelIds=1f574a05-9d6c-43c1-8a0d-1ec5df6a131c&guideLevelId=1f574a05-9d6c-43c1-8a0d-1ec5df6a131c&orderBy=difficulty")
driver.get(url)
sleep(2)


login_button = driver.find_element_by_class_name("log-in-link-button")
try:
    login_button.click()
except Exception:
    print "Error"
login_popup()
sleep(3)

for i in range(1, 100):
    print str(i) + ": " + guess_and_advance()
    print



sleep(10)

driver.quit()
