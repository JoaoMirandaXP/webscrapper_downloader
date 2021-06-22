from selenium import webdriver
from selenium.webdriver.common.by import By 
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

def get_pages(BASE_URL,numero):
    for i in range(1,numero+1):
        site(BASE_URL,i)
if __name__ == "__main__":
    get_pages("http://fuvestibular.com.br/apostilas/fundamentos-da-matematica-elementar/vol-{}",11)