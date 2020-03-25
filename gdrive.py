import os, time

import random, requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

USER_AGENTS = [
            "Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0",
           ]

email='hello@surekoala.com.au'; password='7xAuQpnhTkdh'

POST_LOGIN_URL = 'https://www.dropshipzone.com.au/customer/account/loginPost/referer/aHR0cHM6Ly93d3cuZHJvcHNoaXB6b25lLmNvbS5hdS8_X19fU0lEPVU,/'
REQUEST_URL = 'https://www.dropshipzone.com.au/rsdropship/download/downloadSkuList/'
ua = random.choice(USER_AGENTS)
payload = {
	'login[username]': email,
	'login[password]': password,
}

# cookies=dict(cookies_are='working')
print("[DropShipZone Bot] Attempting to login to Account")
session = requests.Session()
session.get('https://www.google.com', headers={'User-agent': ua})
# try:
post = session.post(POST_LOGIN_URL, headers={'User-agent': ua}, cookies=dict(session.cookies), data=payload, timeout=(30, 60))
post = session.post('https://www.dropshipzone.com.au/rsds/download/skus/', headers={'User-agent': ua}, cookies=session.cookies, data=payload, timeout=(30, 60))

if post.ok:
	print("[DropShipZone Bot] Login Successful")
	print("[DropShipZone Bot] File Download Initiated")
	r = session.get(REQUEST_URL, headers={'User-agent': ua}, stream=True, cookies=dict(session.cookies), timeout=(30, 60))
	# r = session.get(REQUEST_URL, headers={'User-agent': random.choice(USER_AGENTS)}, cookies=dict(session.cookies), timeout=(30, 120))
	filename = r.headers['Content-Disposition'].split('=')[-1].strip()
	with open(filename, 'wb') as file:
		print(f"[DropShipZone Bot] Downloading {filename} .. This file is quite large and might take a little while to finish downloading.")
		for chunk in r.iter_content(10000):
			if chunk:
				file.write(chunk)
	print(f"[DropShipZone Bot] Done Downloading {filename} ...")
else:
	print("[DropShipZone Bot] Login Failure")





# # STORE CREDENTIALS
# USERNAME = 'gilsanarisse'
# PASSWORD = 'koaunqFKhG2E3qkoala'

# IGNORED_EXCEPTIONS = (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException, TimeoutException)

# def make_driver_settings(driver_path=r"..\CDN\chromedriver.exe"):
# 	opts = webdriver.ChromeOptions()
# 	# chrome_prefs = {}
# 	# opts.experimental_options["prefs"] = chrome_prefs
# 	# chrome_prefs["profile.default_content_settings"] = {"images" : 2}
# 	# chrome_prefs["profile.managed_default_content_settings"] = {"images" : 2}
# 	# opts.add_argument('--headless')
# 	driver = webdriver.Chrome(driver_path, options = opts)
# 	driver.implicitly_wait(30)
# 	return driver

# def logout(driver):
# 	# logout procedure
# 	button = driver.find_element_by_id('netoToolbar').find_element_by_css_selector('a[class=sign-out-link]')
# 	driver.get(button.get_attribute('href'))
# 	time.sleep(2)
# 	driver.close()

# def initial_steps(driver, USERNAME=USERNAME, PASSWORD=PASSWORD):
# 	# login prodedures
# 	driver.get("https://www.surekoala.com.au/_cpanel")
# 	driver.find_element_by_id('username').send_keys(USERNAME)
# 	driver.find_element_by_id('password').send_keys(PASSWORD)
# 	driver.find_element_by_css_selector('button[type="submit"]').click()
# 	# if driver.current_url != "https://www.surekoala.com.au/_cpanel":
# 	driver.get('https://www.surekoala.com.au/_cpanel/dsimport?limitmod=DS_inventory&limittmp=n')

# def wait_until(secs=300):
# 	for i in range(secs):
# 		stat = driver.execute_script('return document.readyState;')
# 		if stat == 'complete':
# 			return



# # def main_actions(driver):
# driver = make_driver_settings()
# initial_steps(driver)
# tags = driver.find_elements_by_tag_name('tbody tr')
# tags[4].find_element_by_id('chkbox2').click()
# #####
# # upload neto csv
# tags[5].find_element_by_css_selector('[type="file"]').send_keys(os.path.abspath('neto.csv'))
# time.sleep(1)
# driver.execute_script('javascript:doAction("run");')
# driver.switch_to.alert.accept()

# # wait for some seconds till you see the link
# link = WebDriverWait(driver, 180, ignored_exceptions=IGNORED_EXCEPTIONS).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="netoPage--content--page currentTkn--dsimport"] a')))
# next_link = link.get_attribute('href')

# # next_link = driver.find_element_by_css_selector('div[class="netoPage--content--page currentTkn--dsimport"] a').get_attribute('href')
# driver.get(next_link)
# driver.find_element_by_css_selector('input[type="checkbox"]').click()
# driver.execute_script("javascript:doActionSingle('run','0');")

# @classmethod
# def nucleus(cls):
# cls.main_actions(driver)
# cls.logout(driver)













# import pickle
# import os.path
# from googleapiclient import errors
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

# class FilterSheet:
# 	@classmethod
# 	def get_scripts_service(cls):
# 		SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
# 		creds = None
# 		if os.path.exists('token.pickle'):
# 			with open('token.pickle', 'rb') as token:
# 				creds = pickle.load(token)
# 		if not creds or not creds.valid:
# 			if creds and creds.expired and creds.refresh_token:
# 				creds.refresh(Request())
# 			else:
# 				flow = InstalledAppFlow.from_client_secrets_file(
# 					'client_secrets.json', SCOPES) 
# 				creds = flow.run_local_server(port=0)
# 			with open('token.pickle', 'wb') as token:
# 				pickle.dump(creds, token)

# 		return build('script', 'v1', credentials=creds)

# 	@classmethod
# 	def action(cls):
# 		service = cls.get_scripts_service()
# 		API_ID = "MgWJvW4FegI-NDpFLP44x-vLSJHYMIpDM" 
# 		request = {"function": "filterSheet"} 
# 		try:
# 			response = service.scripts().run(body=request, scriptId=API_ID).execute()
# 			print(response)
# 		except errors.HttpError as error:
# 			# The API encountered a problem.
# 			print(error.content)