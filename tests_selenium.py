import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import config as cfg

# fonction de test
def test_firefox_resultats_biberons():

	with webdriver.Firefox() as driver:

		driver.get(cfg.site['url'])
		bouton = driver.find_element_by_xpath('//button[contains(text(),"Tout accepter")]')
		bouton.click()
		recherche = driver.find_element_by_id('query')
		recherche.send_keys("biberon")
		recherche.send_keys(Keys.ENTER)

		# attente que la page résultats se charge
		WebDriverWait(driver, 15).until(EC.url_changes(cfg.site['url']))

		# nouvelle URL
		new_url = driver.current_url

		# on vérifie qu'il y ait bien 172 résultats
		assert '172' in driver.find_element_by_id('categ-count').text
		# on vérifie le nom de la nouvelle url
		assert new_url == 'https://www.bebe9.com/recherche?query=biberon'

def test_chrome_resultats_biberons():

	with webdriver.Chrome() as driver:

		driver.get(cfg.site['url'])
		bouton = driver.find_element_by_xpath('//button[contains(text(),"Tout accepter")]')
		bouton.click()
		recherche = driver.find_element_by_id('query')
		recherche.send_keys("biberon")
		recherche.send_keys(Keys.ENTER)

		# attente que la page résultats se charge
		WebDriverWait(driver, 15).until(EC.url_changes(cfg.site['url']))

		# nouvelle URL
		new_url = driver.current_url

		# on vérifie qu'il y ait bien 172 résultats
		assert '172' in driver.find_element_by_id('categ-count').text
		# on vérifie le nom de la nouvelle url
		assert new_url == 'https://www.bebe9.com/recherche?query=biberon'