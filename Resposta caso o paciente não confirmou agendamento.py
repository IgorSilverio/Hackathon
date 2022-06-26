import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Instanciando as options para o webdriver
options = webdriver.ChromeOptions()


# options para manter o usuario da conta do google logada.
options.add_argument(
    "--user-data-dir=C:/Users/MV002/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Default")


# comando para executar o Chromedrive
driver = webdriver.Chrome(options=options, executable_path='C:\Users\igor\OneDrive\Imagens\bots\whatsappEnvioDeArquivos\chromedriver.exe')


# abre o site Whatsapp Web - Não pode haver janelas do chrome abertas
driver.get('https://web.whatsapp.com/')


# da um sleep de 15 segundos, tempo para scannear o QRCODE
time.sleep(15)


# Comando para buscar contatos que Não confirmaram agendamento
contatosProducao = ['Marco', 'Hackathon', 'Marcia', 'Guilherme']


# Mensagem - Mensagem que sera enviada
mensagem = 'O que vode deseja'
mensagem2 = '1-reagendar'
mensagem3 = '2-cancelar o medicamento'
mensagem4 = '3-sair'


# Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1)

    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


# Funcao que envia a mensagem
def enviar_mensagem(texto1, texto2):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)

    campo_mensagem[1].send_keys(str(texto1) + str(''))
    campo_mensagem[1].send_keys(Keys.ENTER)
    campo_mensagem[1].send_keys(str('') + str(texto2))
    campo_mensagem[1].send_keys(Keys.ENTER)


# fechar google chorome
    driver.close()
    driver.quit()
    sys.exit()
