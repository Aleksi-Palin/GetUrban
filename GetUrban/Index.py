#set all imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import warnings
from colorama import Fore, init

warnings.filterwarnings('ignore')

def GetUrbanW1():
    #try getting urban word
    
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

        example = driver.find_element(By.XPATH, "//div[@class='box']/blockquote").text

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        #try to get blockquote element if not existing skip
        init(convert=True)      
        Widness = len(example) + 2 
        print(f'{Fore.WHITE}_'*Widness)

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        print(f'{Fore.GREEN} {TheWord}')
                #print("-"*len(TheWord))
        print(" ")

        print(f'{Fore.MAGENTA} {explainer}')
        print(" ")
        print(f'{Fore.CYAN} {example}')

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        print(f'{Fore.WHITE}_'*Widness)

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)
                   
#get context-------------------------------------------------------------
            
        
        driver.quit()


#create function for getting urban word without example
def GetUrbanW2():
    #try getting urban word
    
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
        init(convert=True)      
        Widness = len(explainer) + 2 
        print(f'{Fore.WHITE}_'*Widness)

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        print(f'{Fore.GREEN} {TheWord}')
                #print("-"*len(TheWord))
        print(" ")

        print(f'{Fore.MAGENTA} {explainer}')

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)

        print(f'{Fore.WHITE}_'*Widness)

        #wait 0.1 seconds for whole page to load
        time.sleep(0.1)
                   
#get context-------------------------------------------------------------
            
        
        driver.quit()

#execute function in main
if __name__ == "__main__":
    try:
        GetUrbanW1()
    except:
        GetUrbanW2()
    

