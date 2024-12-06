from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import config  # Importar credenciais do arquivo config.py

# Configuração do GeckoDriver com User-Agent personalizado
service = Service("/usr/local/bin/geckodriver")

options = Options()
options.set_preference(
    "general.useragent.override",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

# Inicializar o WebDriver com as opções configuradas
driver = webdriver.Firefox(service=service, options=options)

def wait_for_page_load(timeout=30):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        print("Página carregada completamente.")
    except Exception as e:
        print(f"Timeout ao esperar o carregamento da página: {e}")

def login_with_google(email):
    driver.get("https://www.linkedin.com/login")
    wait_for_page_load()
    time.sleep(5)

    try:
        # Captura de tela para depuração fora dos iframes
        driver.save_screenshot("before_google_signin_click.png")
        print("Captura de tela salva como 'before_google_signin_click.png'.")

        # Tentar localizar o botão "Sign in with Google" diretamente no contexto principal
        google_signin_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Sign in with Google']"))
        )
        google_signin_button.click()
        print("Clicou no botão 'Sign in with Google'.")

    except Exception as e:
        print(f"Erro durante o login: {e}")
        driver.save_screenshot("error_google_signin.png")
        print("Captura de tela salva como 'error_google_signin.png'.")

    finally:
        driver.quit()

if __name__ == "__main__":
    login_with_google(config.LINKEDIN_EMAIL)
