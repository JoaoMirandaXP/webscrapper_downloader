from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import os
import time

def download(url,name):
    resp = requests.get(url)
    OUTPUT_DIR = 'output'
    local_arquivo = os.path.join(OUTPUT_DIR,name+".pdf")

    if resp.status_code == requests.codes.OK:
        with open(local_arquivo, 'wb') as arquivo:
            arquivo.write(resp.content)
        print("Download de {} Concluido! ".format(name))
    else:
        resp.raise_for_status()

def site(site,i):
    site = site.format(i)
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(5)
    link = driver.find_elements(By.TAG_NAME, "a")
    for l in link:
        if(l.text.startswith("Download")):
            url = l.get_attribute("href")
            nome_do_arquivo= l.text
            download(url,nome_do_arquivo)
    driver.close()

def formatacao(i):
    if i < 10:
        return '0{}'.format(i)
    else:
        return i

def get_pages(BASE_URL,numero):
    pages = []
    for i in range(1,numero+1):
        pages.append(BASE_URL.format(formatacao(i)))
    return pages
def salva_como_pdf(url, driver):
    driver.get(url)
# Essa função visa encontrar as informações desejadas para o download de maneira difusa para qualquer site.
def info_tracker(url, driver):
    print('Localizando as informações...')
    driver.get(url)
    body = driver.find_element_by_id('content')
    links = body.find_elements_by_tag_name('a')
    info = {}
    for link in links:
        #info["site"].append(link.get_attribute('href'))
        #info["name"].append(link.text)
        info[link.text] = (link.get_attribute('href'))
    return info
def open_print_dialog(info, driver):
    for arquivo, link in info.items():
        driver.get(link)
        print(arquivo)
        if input('') == '':
            driver.execute_script('window.print();')

if __name__ == "__main__":
    driver = webdriver.Chrome()
    #get_pages("http://fuvestibular.com.br/apostilas/fundamentos-da-matematica-elementar/vol-{}",11)
    #for page in pages:
    #    print(page)
    #    time.sleep(1)
    #    salva_como_pdf(page, driver)

    info = info_tracker('https://noic.com.br/curso-noic-de-matematica/', driver)
    open_print_dialog(info, driver)
