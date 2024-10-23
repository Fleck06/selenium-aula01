from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options = opts)

url1 = r'https://magazineluiza.com.br/'