#set all imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


#create function for getting urban word
def GetUrban():
    #try getting urban word
    try:

        #set chrome options
        cOptions = Options()
        cOptions.headless = True

        #set chromedriver path
        drive_path = os.path.abspath(os.curdir) + "\chromedriver.exe"
        driver = webdriver.Chrome(executable_path= drive_path,chrome_options=cOptions)

        #get wanted url
        driver.get('https://urbaanisanakirja.com/random')     

        #wait 1 seconds for whole page to load
        time.sleep(1)    

        #accept cookies
        accept_div = driver.find_element(By.CSS_SELECTOR,'button.css-47sehv')
        accept_div.click()
        
#get context-------------------------------------------------------------

        #get the word
        TheWord = driver.find_element(By.XPATH,"//div[@class='box']/a/h1").text

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        #get the part that explains the word
        explainer = driver.find_element(By.XPATH,"//div[@class='box']/p").text

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        #try to get blockquote element if not existing skip
        try:
            #get the example for the word
            example = driver.find_element(By.XPATH,"//div[@class='box']/blockquote").text
        except:
            print("there is not blockquote element")
            
        finally:
            
#get context-------------------------------------------------------------

            #sum up output
            output = TheWord + "\n" + explainer + "\n" + example

            #print output
            print(output)
        
    except Exception as e:
        #print error
        print(e)
    finally:
        #when all succeed close browser
        driver.quit()

#execute function in main
if __name__ == "__main__":
    GetUrban()
    

