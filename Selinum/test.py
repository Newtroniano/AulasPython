from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicia o WebDriver do Chrome
driver = webdriver.Chrome()

# Abre um site
driver.get('https://www.google.com')

# Localiza o campo de pesquisa e insere um termo
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Um homem com a cabeça de piroca')
search_box.send_keys(Keys.RETURN)

first_link = driver.find_element(By.CSS_SELECTOR, 'h3')


first_link.click()

# Aguarda um pouco para ver o resultado
driver.implicitly_wait(105)

# Fecha o navegador
driver.quit()
