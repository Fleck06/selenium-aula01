from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options = opts)

url = r'C:\Users\08137\Desktop\webscrap\webscrap\contato.html'
navegador.get(url)

campo_nome = navegador.find_element(By.ID, "nome")
campo_nome.send_keys("Paulo Tejano")
sleep(3)

campo_mensagem = navegador.find_element(By.ID, "mensagem")
campo_mensagem.send_keys("A Globo é um lixo")
sleep(3)

botao = navegador.find_element(By.XPATH, "/html/body/div/div/form/button")
botao.click()