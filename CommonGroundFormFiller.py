import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import streamlit as st
import csv
import io
import pandas as pd

def process_csv_file(csv_file):
    csv_data = []
    text_io = io.TextIOWrapper(csv_file, encoding='utf-8-sig')
    reader = csv.DictReader(text_io)
    print(reader.fieldnames)  # Print the column names
    for row in reader:
        csv_data.append(row)
    return csv_data


def convert_df(df):
    return df.to_csv().encode('utf-8')

def fill_form_with_selenium(csv_data):
    
    plan_dict = {
        'Chorus Catastrophic': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl02_Apply',
        'Chorus Core Bronze': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl03_Apply',
        'Chorus Bronze': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl04_Apply',
        'Chorus Silver Choice': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl05_Apply',
        'Chorus Bronze HDHP': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl06_Apply',
        'Chorus Bronze Copay': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl07_Apply',
        'Chorus Core Silver': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl08_Apply',
        'Chorus Silver': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl09_Apply',
        'Chorus Silver Select': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl10_Apply',
        'Chorus Standard Silver': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl11_Apply',
        'Chorus Core Gold': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl12_Apply',
        'Chorus Silver Copay': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl13_Apply',
        'Chorus Gold': 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_grdPlans_ctl14_Apply',
        # Add more plan names and form IDs as needed
    }
    for row in csv_data:
        # information for Employee and Spouse
        try:
            dict = {
                'Application Type': row.get('Application Type'),
                'Student': row.get('Student'),
                'Tobacco': row.get('Tobacco'),
                'Gender': row.get('Gender'),
                'DOB-Month': row.get('DOB-Month'),
                'DOB-Day': row.get('DOB-Day'),
                'DOB-Year': row.get('DOB-Year'),
                'Zip Code': row.get('Zip Code'),
                'Plan': row.get('Plan'),
                'First Name': row.get('First Name'),
                'Last Name': row.get('Last Name'),
                'Email': row.get('Email'),
                'SSN': row.get('SSN'),
                'Marital Status': row.get('Marital Status'),
                'Street Address 1': row.get('Street Address 1'),
                'City': row.get('City'),
                'Phone': row.get('Phone'),
                'Citizenship': row.get('Citizenship'),
                'Current Coverage': row.get('Current Coverage'),
                'Spouse Student': row.get('Spouse Student'),
                'Spouse Tobacco': row.get('Spouse Tobacco'),
                'Spouse First Name': row.get('Spouse First Name'),
                'Spouse Last Name': row.get('Spouse Last Name'),
                'Spouse Gender': row.get('Spouse Gender'),
                'Spouse DOB': row.get('Spouse DOB'),
                'Spouse Marital Status': row.get('Spouse Marital Status'),
                'Spouse SSN': row.get('Spouse SSN'),
                'Spouse DOB-Month': row.get('DOB-Month'),
                'Spouse DOB-Day': row.get('DOB-Day'),
                'Spouse DOB-Year': row.get('Spouse DOB-Year'),
            }

            #st.write(dict)
            for child_number in range(1, 11):
                child_key = 'Child ' + str(child_number)
                #st.write(child_key)
                dict[child_key + ' First Name'] = row.get(child_key + ' First Name')
                dict[child_key + ' Last Name'] = row.get(child_key + ' Last Name')
                dict[child_key + ' SSN'] = row.get(child_key + ' SSN')
                dict[child_key + ' Gender'] = row.get(child_key + ' Gender')
                dict[child_key + ' Marital Status'] = row.get(child_key + ' Marital Status')
                dict[child_key + ' DOB-Month'] = row.get(child_key + ' DOB-Month')
                dict[child_key + ' DOB-Day'] = row.get(child_key + ' DOB-Day')
                dict[child_key + ' DOB-Year'] = row.get(child_key + ' DOB-Year')
                dict[child_key + ' Tobacco'] = row.get(child_key + ' Tobacco')
                dict[child_key + ' Student'] = row.get(child_key + ' Student')
            
            

            #st.write(dict)
            #break

            driver = webdriver.Chrome()  
            # Assuming you have ChromeDriver installed and added to PATH

            wait = WebDriverWait(driver, 10)

            # Navigate to the login page
            driver.get('https://cghcuat.jet-insure.com/formConsumerLogin.aspx')
            
            # Fill in login credentials
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlMembershipSignIn_txtUserName'))).send_keys('BS6487452')

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlMembershipSignIn_txtPassword'))).send_keys('Fall2022!')
            # ... fill out more form fields as needed

            # Submit the form
            login_button = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlMembershipSignIn_btnSignIn')))

            login_button.click()


            dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Get Quote']")))

                

            action = ActionChains(driver)
            action.move_to_element(dropdown).perform()


            wait = WebDriverWait(driver, 10)
            option = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_PlaceHolderBodyMain_hlnkIFPQuote')))

            option.click()

            

            dropdown = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl02_ddlGender')

            dropdown.click()


            if(dict['Gender'] == 'MALE'):
                option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Male']")))
            if(dict['Gender'] == 'FEMALE'):
                option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Female']")))
                
            option.click()
            

            #Month
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl02_ucDOBChild_txtMonth'))).send_keys(str(dict['DOB-Month']))

            #Day
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl02_ucDOBChild_txtDay'))).send_keys(str(dict['DOB-Day']))

            #Year
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl02_ucDOBChild_txtYear'))).send_keys(str(dict['DOB-Year']))

            if(dict['Tobacco'] == 'YES'):
                    checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl02_rblSmoker')

                    checkbox.click()

            
            if(dict['Application Type'] == 'EE + SPOUSE' or dict['Application Type'] == 'EE + FAMILY'): 
                dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_ddlGender')

                dropdown2.click()

                if(dict['Spouse Gender'] == 'MALE'):
                    option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_ddlGender']/option[text()='Male']")))
                if(dict['Spouse Gender'] == 'FEMALE'):
                    option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_ddlGender']/option[text()='Female']")))

                option2.click()

                #Month
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_ucDOBChild_txtMonth'))).send_keys(str(dict['Spouse DOB-Month']))

                #Day
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_ucDOBChild_txtDay'))).send_keys(str(dict['Spouse DOB-Day']))

                #Year
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_ucDOBChild_txtYear'))).send_keys(str(dict['Spouse DOB-Year']))
                
                if(dict['Spouse Tobacco'] == 'YES'):
                    checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl03_rblSmoker')

                    checkbox.click()
                

            if(dict['Application Type'] == 'EE + Child' or dict['Application Type'] == 'EE + FAMILY'):
                dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_ddlGender')

                dropdown2.click()

                if(dict['Child 1 Gender'] == 'MALE'):
                    option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_ddlGender']/option[text()='Male']")))
                if(dict['Child 1 Gender'] == 'FEMALE'):
                    option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_ddlGender']/option[text()='Female']")))

                option2.click()

                #Month
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 1 DOB-Month']))

                #Day
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_ucDOBChild_txtDay'))).send_keys(str(dict['Child 1 DOB-Day']))

                #Year
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_ucDOBChild_txtYear'))).send_keys(str(dict['Child 1 DOB-Year']))

                if(dict['Child 1 Tobacco'] == 'YES'):
                    checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl04_rblSmoker')

                    checkbox.click()

                if(dict['Child 2 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_ddlGender')

                    dropdown2.click()

                    if(dict['Child 2 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_ddlGender']/option[text()='Male']")))
                    if(dict['Child 2 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 2 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_ucDOBChild_txtDay'))).send_keys(str(dict['Child 2 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_ucDOBChild_txtYear'))).send_keys(str(dict['Child 2 DOB-Year']))

                    if(dict['Child 2 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl05_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)

                if(dict['Child 3 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_ddlGender')

                    dropdown2.click()

                    if(dict['Child 3 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_ddlGender']/option[text()='Male']")))
                    if(dict['Child 3 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 3 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_ucDOBChild_txtDay'))).send_keys(str(dict['Child 3 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_ucDOBChild_txtYear'))).send_keys(str(dict['Child 3 DOB-Year']))

                    if(dict['Child 3 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl06_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)

                if(dict['Child 4 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_ddlGender')

                    dropdown2.click()

                    if(dict['Child 4 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_ddlGender']/option[text()='Male']")))
                    if(dict['Child 4 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 4 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_ucDOBChild_txtDay'))).send_keys(str(dict['Child 4 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_ucDOBChild_txtYear'))).send_keys(str(dict['Child 4 DOB-Year']))

                    if(dict['Child 4 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl07_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)
                
                if(dict['Child 5 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_ddlGender')

                    dropdown2.click()

                    if(dict['Child 5 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_ddlGender']/option[text()='Male']")))
                    if(dict['Child 5 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 5 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_ucDOBChild_txtDay'))).send_keys(str(dict['Child 5 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_ucDOBChild_txtYear'))).send_keys(str(dict['Child 5 DOB-Year']))

                    if(dict['Child 5 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl08_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)

                if(dict['Child 6 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_ddlGender')

                    dropdown2.click()

                    if(dict['Child 6 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_ddlGender']/option[text()='Male']")))
                    if(dict['Child 6 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 6 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_ucDOBChild_txtDay'))).send_keys(str(dict['Child 6 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_ucDOBChild_txtYear'))).send_keys(str(dict['Child 6 DOB-Year']))

                    if(dict['Child 6 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl09_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)
                
                if(dict['Child 7 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_ddlGender')

                    dropdown2.click()

                    if(dict['Child 7 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_ddlGender']/option[text()='Male']")))
                    if(dict['Child 7 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 7 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_ucDOBChild_txtDay'))).send_keys(str(dict['Child 7 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_ucDOBChild_txtYear'))).send_keys(str(dict['Child 7 DOB-Year']))

                    if(dict['Child 7 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl10_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)

                if(dict['Child 8 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_ddlGender')

                    dropdown2.click()

                    if(dict['Child 8 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_ddlGender']/option[text()='Male']")))
                    if(dict['Child 8 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 8 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_ucDOBChild_txtDay'))).send_keys(str(dict['Child 8 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_ucDOBChild_txtYear'))).send_keys(str(dict['Child 8 DOB-Year']))

                    if(dict['Child 8 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl11_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)

                if(dict['Child 9 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_ddlGender')

                    dropdown2.click()

                    if(dict['Child 9 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_ddlGender']/option[text()='Male']")))
                    if(dict['Child 9 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 9 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_ucDOBChild_txtDay'))).send_keys(str(dict['Child 9 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_ucDOBChild_txtYear'))).send_keys(str(dict['Child 9 DOB-Year']))

                    if(dict['Child 9 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl12_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)

                if(dict['Child 10 First Name'] != 'NULL'):
                    

                    dropdown2 = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl13_ddlGender')

                    dropdown2.click()

                    if(dict['Child 10 Gender'] == 'MALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl13_ddlGender']/option[text()='Male']")))
                    if(dict['Child 10 Gender'] == 'FEMALE'):
                        option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl3_ddlGender']/option[text()='Female']")))

                    option2.click()

                    #Month
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl13_ucDOBChild_txtMonth'))).send_keys(str(dict['Child 10 DOB-Month']))

                    #Day
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl13_ucDOBChild_txtDay'))).send_keys(str(dict['Child 10 DOB-Day']))

                    #Year
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl13_ucDOBChild_txtYear'))).send_keys(str(dict['Child 10 DOB-Year']))

                    if(dict['Child 10 Tobacco'] == 'YES'):
                        checkbox = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_gvApplicantInfo_ctl13_rblSmoker')

                        checkbox.click()

                    addChild = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_lbtAddChild')

                    addChild.click()

                    time.sleep(2)
            #time.sleep(100)
            #break

            #Zip Code
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_txtZipCode'))).send_keys(str(dict['Zip Code']))

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_txtEmail'))).send_keys(str(dict['Email']))
            # qualifying reason dropdown
            # dropdown = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_ddlQualifyingReason')

            # dropdown.click()

            # qualifying reason select
            # option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Newly eligible for ICHRA']")))

            # option.click()

            #get quote (next page)
            option = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_FamilyInsuranceQuoteInfo1_btnGetQuote')))

            option.click()

            #plan select 
            option = wait.until(EC.visibility_of_element_located((By.ID, plan_dict[dict['Plan']])))

            option.click()




            #Next Page
            option = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ucPlanComparison_rptPlanNames_ctl00_lnkApplyOne')))

            option.click()

            #Next Page
            option = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_lnkNext')))

            option.click()

            #fill account forms
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtEmpFirstName'))).send_keys(str(dict['First Name']))

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtEmpLastName'))).send_keys(str(dict['Last Name']))

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtEmpDOB_txtDate'))).send_keys(str(dict['DOB-Month']+'/'+str(dict['DOB-Day']+'/'+str(dict['DOB-Year']))))

            element = wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtEmpSSN')))

            # Send the last 4 digits of SSN to the input field
            element.send_keys(str(dict['SSN'][-4:]))

            # Send the "Enter" key separately
            element.send_keys(Keys.ENTER)

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtEmail'))).send_keys(str(dict['Email']))

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtReEmail'))).send_keys(str(dict['Email']))

            #wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtEmail'))).send_keys(str(dict['Email']))
            

            

            #Next Page
            a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_btnSubmit')

            a_element.click()
            

            #SSN
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['SSN']))

            #Marital Status Dropdown
            dropdown = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ddlMaritalStatus')

            dropdown.click()

            #Marital Status Select
            if(dict['Marital Status'] == 'SINGLE'):
                option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Single']")))
            if(dict['Marital Status'] == 'MARRIED'):
                option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Married']")))

            option.click()

            #Preferred Phone
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtHomePhone1'))).click()

            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtHomePhone1'))).send_keys(str(dict['Phone']))

            #previous coverage
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

            #disabled
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

            
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_grdAddresses_ctl02_imgEdit'))).click()

            #address 1
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_txtSmartyAddress'))).send_keys(str(dict['Street Address 1']))

            #state (WI)
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_ddlSmartyState'))).send_keys("WI")

            #City
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_txtSmartyCity'))).send_keys(str(dict['City']))

            #Verify
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_btnVerify'))).click()

            #Save
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_btnSmartySave'))).click()

            time.sleep(3)

            #Same as Physical
            wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_ctrlSmarty_grdAddresses_ctl03_chkSameAsCorporateAddress'))).click()


        


            #Next Page
            a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

            a_element.click()

            #time.sleep(60)

            time.sleep(10)
            if(dict['Application Type'] == 'EE + SPOUSE' or dict['Application Type'] == 'EE + FAMILY'):
                #Spouse First Name
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Spouse First Name']))

                #Spouse Last Name
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Spouse Last Name']))

                #Spouse SSN
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Spouse SSN']))

                #previous coverage
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                #disabled
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                #Next Page
                a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                a_element.click()

                time.sleep(5)

            if(dict['Application Type'] == 'EE + Child' or dict['Application Type'] == 'EE + FAMILY'):
                #Child 1 First Name
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 1 First Name']))

                #Child 1 Last Name
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 1 Last Name']))

                #Child 1 SSN
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 1 SSN']))

            

                #previous coverage
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                #disabled
                wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                    

                #Next Page
                a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                a_element.click()

                time.sleep(5)

                if(dict['Child 2 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 2 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 2 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 2 SSN']))



                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 3 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 3 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 3 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 3 SSN']))



                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 4 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 4 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 4 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 4 SSN']))


                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 5 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 5 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 5 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 5 SSN']))



                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 6 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 6 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 6 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 6 SSN']))



                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 7 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 7 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 7 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 7 SSN']))



                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 8 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 8 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 8 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 8 SSN']))



                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 9 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 9 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 9 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 9 SSN']))

    


                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)

                if(dict['Child 10 First Name'] != 'NULL'):

                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtFirstName'))).send_keys(str(dict['Child 10 First Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtLastName'))).send_keys(str(dict['Child 10 Last Name']))


                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_txtSSN'))).send_keys(str(dict['Child 10 SSN']))


                    #previous coverage
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblOtherInsurance_1'))).click()

                    #disabled
                    wait.until(EC.visibility_of_element_located((By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_rdblIsDisabled_1'))).click()

                        
                    a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

                    a_element.click()

                    time.sleep(5)
                



            #Next Page
            a_element = driver.find_element(By.ID, 'ctl00_ctl00_ContentPlaceHolderBody_PlaceHolderBodyMain_jetMUApplicationFooter_btnNext')

            a_element.click()

            time.sleep(30) 

            # Close the browser
            driver.quit()
        except Exception as e:
            st.write(f"Error: {row['First Name']} {row['Last Name']}")
            error_row = pd.DataFrame({'First Name': [row['First Name']], 'Last Name': [row['Last Name']], 'Error Message': [str(e)]})
            pd.concat([failed, error_row])
            driver.quit()
            continue


failed = pd.DataFrame(columns=['First Name', 'Last Name', 'Error Message'])
# Create a file uploader widget
st.header('Common Ground AUTO FILLER')
prod = st.checkbox('PROD')
csv_file = st.file_uploader("Upload a CSV file", type="csv")


download_button = st.download_button(
        label = "Download data of Failed Applications",
        data = convert_df(failed),
        file_name = 'failed.csv',
        mime='text'
    )

if csv_file is not None:
    # Process the CSV file
    csv_data = process_csv_file(csv_file)
    fill_form_with_selenium(csv_data)
    st.success("Form filling completed successfully!")