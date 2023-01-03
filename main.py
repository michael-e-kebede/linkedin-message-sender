from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from selenium.webdriver.common.by import By

username = 'tamsayne@gmail.com'
password = 'D5T3mVzFaU%yyPqc'

chrome_path = 'driver/chromedriver'

driver = webdriver.Chrome(chrome_path)
driver.get('https://www.linkedin.com/uas/login')

elementID = driver.find_element(By.ID, 'username')
elementID.send_keys(username)

sleep(randint(3, 6))

elementID = driver.find_element(By.ID, 'password')
elementID.send_keys(password)

elementID.submit()


links = []

#This is for the "CONNECTION" button div
xpath_conn = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button'
xpath1_conn = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button'

#This is for the "MORE" button
xpath_more = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/button'
xpath_more1 = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/button'

#This is for the "CONNECT" button in the "MORE" section
xpath_more_connect = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/div/div/ul/li[4]/div'
xpath_more_connect_1 = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/div/div/ul/li[4]/div'

for link in links:
    driver.get(link)
    sleep(randint(5, 10))

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    connect_sec = soup.find(class_ = 'pv-top-card-v2-ctas')
    pre_div = connect_sec.find(class_ = 'pvs-profile-actions__action')
    connect_or_follow = pre_div.text.strip()

#If there is a connect button

    if connect_or_follow == 'Connect':
        try:
            connectID = driver.find_element(By.XPATH, xpath_conn)
            connectID.click()

        except Exception as e:
            connectID = None

        if connectID is None:
            try:
                connectID = driver.find_element(By.XPATH, xpath1_conn)
                connectID.click()

            except Exception as e:
                connectID = None

        add_noteID = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
        add_noteID.click()

        sleep(randint(3, 6))       

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        person_Name = soup.find('div', {'class' : 'artdeco-modal__header ember-view'}).find('h2').text.strip()
        person_Name = person_Name.split()
        person_Name = person_Name[1]


        message = f"""Hi {person_Name}, 

Hope you are doing well.

I might have an offer for you as a Back-End Web Application Developer. Would that be of interest to you? Your profile seems to be a good fit for our client.

Warm regards,
Rahel"""

        messageID = driver.find_element(By.ID, 'custom-message')
        messageID.send_keys(message)

        sleep(randint(8, 15))

        message_sent = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
        message_sent.click()

        print("Connect Account Sent")
        print('---'*40)

        sleep(randint(10, 20))

#If there is NO connect button and the button is Message

    elif connect_or_follow == 'Message':

        #Try for the More button
        try:
            moreID = driver.find_element(By.XPATH, xpath_more)
            moreID.click()

            sleep(randint(5, 9))
        except Exception as e:
            moreID = None

        if moreID is None:
            try:
                moreID = driver.find_element(By.XPATH, xpath_more1)
                moreID.click()

                sleep(randint(5, 9))
            except Exception as e:
                moreID = None


        #Try for the Connect button in more
        try:
            Connect_moreID = driver.find_element(By.XPATH, xpath_more_connect)
            Connect_moreID.click()

            sleep(randint(5, 9))
        except Exception as e:
            Connect_moreID = None

        if Connect_moreID is None:
            try:
                Connect_moreID = driver.find_element(By.XPATH, xpath_more_connect_1)
                Connect_moreID.click()

                sleep(randint(5, 9))
            except Exception as e:
                moreID = None
        

        how_Connect_moreID = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/button[4]')
        how_Connect_moreID.click()

        sleep(randint(5, 9))

        Connect_final = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
        Connect_final.click()

        add_noteID = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
        add_noteID.click()

        sleep(randint(5, 9))

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        person_Name = soup.find('div', {'class' : 'artdeco-modal__header ember-view'}).find('h2').text.strip()
        person_Name = person_Name.split()
        person_Name = person_Name[1]

        message = f"""Hi {person_Name},

Hope you are doing well.

I might have an offer for you as a Back-End Web Application Developer. Would that be of interest to you? Your profile seems to be a good fit for our client.

Warm regards,
Rahel"""

        messageID = driver.find_element(By.ID, 'custom-message')
        messageID.send_keys(message)

        sleep(randint(8, 15))

        message_sent = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
        message_sent.click()

        print("Message Account Sent")
        print('---'*40)

        sleep(randint(10, 20))


#If there is NO connect button and the button is Follow

    elif connect_or_follow == 'Follow':
        #Try for the More button
        try:
            moreID = driver.find_element(By.XPATH, xpath_more)
            moreID.click()

            sleep(randint(5, 9))
        except Exception as e:
            moreID = None

        if moreID is None:
            try:
                moreID = driver.find_element(By.XPATH, xpath_more1)
                moreID.click()

                sleep(randint(5, 9))
            except Exception as e:
                moreID = None


        #Try for the Connect button in more
        try:
            Connect_moreID = driver.find_element(By.XPATH, xpath_more_connect)
            Connect_moreID.click()

            sleep(randint(5, 9))
        except Exception as e:
            Connect_moreID = None

        if Connect_moreID is None:
            try:
                Connect_moreID = driver.find_element(By.XPATH, xpath_more_connect_1)
                Connect_moreID.click()

                sleep(randint(5, 9))
            except Exception as e:
                moreID = None


        add_noteID = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
        add_noteID.click()

        sleep(randint(5, 9))

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        person_Name = soup.find('div', {'class' : 'artdeco-modal__header ember-view'}).find('h2').text.strip()
        person_Name = person_Name.split()
        person_Name = person_Name[1]

        message = f"""Hi {person_Name},

Hope you are doing well.

I might have an offer for you as a Back-End Web Application Developer. Would that be of interest to you? Your profile seems to be a good fit for our client.

Warm regards,
Rahel"""

        messageID = driver.find_element(By.ID, 'custom-message')
        messageID.send_keys(message)

        sleep(randint(8, 15))

        message_sent = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
        message_sent.click()
        print("Follow Account Sent")
        print('---'*40)

        sleep(randint(10, 20))
        
