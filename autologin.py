#!/usr/bin/env python3

# -*- coding: utf-8 -*-
__VERSION__ = '0.1.0'

import argparse
import getpass
import time
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--classroom', help='Inicia sesión en classroom', action='store_true')
parser.add_argument('-g', '--gmail', help='Inicia sesión en gmail', action='store_true')
parser.add_argument('-d', '--drive', help='Inicia sesión en drive', action='store_true')

args = parser.parse_args()

def connect():
	try:
		urllib.request.urlopen('http://google.com')
		return False
	except:
		return True


def classroom():
	try:
		email = input("Correo: ")
		passwd = getpass.getpass(prompt= 'Contraseña Gmail: ')
		driver = webdriver.Firefox()
		driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh%3Fhl%3Des&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh%3Fhl%3Des&hl=es&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
		driver.find_element(By.ID, "identifierId").send_keys(email) # INTRODUCIR CORREO
		driver.find_element(By.ID, "identifierNext").click()

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
		time.sleep(2)
		driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passwd)
		driver.find_element(By.ID, "passwordNext").click()
		time.sleep(3)
	except (ElementClickInterceptedException, TimeoutException, NoSuchWindowException, WebDriverException) as e:
		print("Ha ocurrido un error")

def gmail():
	try:
		email = input("Correo: ")
		passwd = getpass.getpass(prompt= 'Contraseña Gmail: ')
		driver = webdriver.Firefox()
		driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
		driver.find_element(By.ID, "identifierId").send_keys(email) # INTRODUCIR CORREO
		driver.find_element(By.ID, "identifierNext").click()

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
		time.sleep(2)
		driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passwd)
		driver.find_element(By.ID, "passwordNext").click()
		time.sleep(3)
	except (ElementClickInterceptedException, TimeoutException, NoSuchWindowException, WebDriverException) as e:
		print("Ha ocurrido un error")

def drive():
	try:
		email = input("Correo: ")
		passwd = getpass.getpass(prompt= 'Contraseña Drive: ')
		driver = webdriver.Firefox()
		driver.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
		driver.find_element(By.ID, "identifierId").send_keys(email) # INTRODUCIR CORREO
		driver.find_element(By.ID, "identifierNext").click()

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
		time.sleep(2)
		driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passwd)
		driver.find_element(By.ID, "passwordNext").click()
		time.sleep(3)
	except (ElementClickInterceptedException, TimeoutException, NoSuchWindowException, WebDriverException) as e:
		print("Ha ocurrido un error")

while connect():
	try:
		connect()
	except:
		print("Ha ocurrido un error")
		continue


def main():
	if not (args.classroom or args.gmail or args.drive ):
		parser.error('Se requiere al menos una opción.')
	elif args.classroom:
		classroom()
	elif args.gmail:
		gmail()
	elif args.drive:
		drive()
	else:
		print('Error: opción incorrecta. Usa -h o --help para mas ayuda')


if __name__ == "__main__":
	main()


