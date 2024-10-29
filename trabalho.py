from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options=opts)

precos = []

url1 = r'https://www.kabum.com.br'
navegador.get(url1)

# Busca 1
pesquisar_dell = navegador.find_element(By.ID, "input-busca")
pesquisar_dell.send_keys("Dell G15")
sleep(2)
pesquisar_dell.send_keys(Keys.RETURN)

# Preço do primeiro notebook (DELL G15)
preco1 = navegador.find_element(By.XPATH, "//span[contains(@class,'sc-e5003a21-2 jfrbst priceCard')]")
precos.append(f' Dell G15: {preco1.text}')
sleep(3)

# Busca 2
pesquisar_acer = navegador.find_element(By.ID, "input-busca")
pesquisar_acer.send_keys("Aspire 5")
sleep(2)
pesquisar_acer.send_keys(Keys.RETURN)

# Preço do segundo notebook (Acer Nitro 5)
preco2 = navegador.find_element(By.XPATH, "//span[contains(@class,'sc-e5003a21-2 iDHDTg priceCard')]")
precos.append(f' Dell Aspire 5: {preco2.text}')
sleep(3)

# Busca 3
pesquisar_lenovo = navegador.find_element(By.ID, "input-busca")
pesquisar_lenovo.send_keys("IdeaPad 1i")
sleep(2)
pesquisar_lenovo.send_keys(Keys.RETURN)

# Preço do segundo notebook (Acer Nitro 5)
preco3 = navegador.find_element(By.XPATH, "//span[contains(@class,'sc-e5003a21-2 jfrbst priceCard')]")
precos.append(f' IdeaPad 1i: {preco3.text}')
sleep(3)

with open('precos.txt', 'w', encoding='utf-8') as file:
    for preco in precos:
        file.write(preco + '\n')
