import facebook
import requests
from selenium import webdriver
import json
import os

class Login(object):
    code = ""
    token = ""
    contents = ""

    def __init__(self):
        #self.skipLogin()
        with open("appinfo.json", 'r') as f:
            global contents
            contents = json.load(f)

    def initializeCode(self):
        app_id = contents['app']['id']
        canvas_url = "https://google.com"
        perms = ["manage_pages","publish_pages"]
        fb_login_url = facebook.GraphAPI().get_auth_url(app_id, canvas_url, perms)
        chromedriver = "./chromedriver78/chromedriverw"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #options = webdriver.ChromeOptions()
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument('--test-type')
        #options.binary_location = "/usr/bin/google-chrome"
        #options.binary_location = "\mnt\c\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        #driver = webdriver.Chrome(chromedriver, chrome_options=options)
        driver = webdriver.Chrome(chromedriver)
        driver.get(fb_login_url)

        while (True):
    
            if "https://www.google.com/?code=" in driver.current_url:
                global code
                code = driver.current_url[29:]
                break

    def initializeToken(self):
        URL = "https://graph.facebook.com/v4.0/oauth/access_token?"
        PARAMS = {'client_id': contents['app']['id'],
                  'redirect_uri': "https://google.com/",
                  'client_secret': contents['app']['secret'],
                  'code': code}
        response = requests.get(url=URL, params=PARAMS)
        responseJson = json.loads(response.text)
        tempToken = responseJson['access_token']
        
        longPARAMS = {'grant_type': "fb_exchange_token",    #get long access token
                      'client_id': contents['app']['id'],
                      'client_secret': contents['app']['secret'],
                      'fb_exchange_token': tempToken}
        
        longResponse = requests.get(url=URL, params=longPARAMS)
        longResponseJson = json.loads(longResponse.text)
        #print(longResponseJson)
        global token
        #token = responseJson['access_token']
        token = longResponseJson['access_token']

    def userLogin(self):
        self.initializeCode()
        self.initializeToken()

    def getToken(self):
        return token

    def skipLogin(self):
        global token
