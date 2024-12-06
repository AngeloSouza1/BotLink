from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Substitua pelo caminho completo do geckodriver
service = Service("/usr/local/bin/geckodriver")

# Configuração do WebDriver
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com")

print("Título da página:", driver.title)  # Deve exibir "Google"
driver.quit()
