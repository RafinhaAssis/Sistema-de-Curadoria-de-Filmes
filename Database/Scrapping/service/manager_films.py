from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from model.films_model import FilmsModel
from service.commons.manager_logger import ManagerLogger

import time
import random

class ManagerFilms():
    def __init__(self, web_driver: webdriver, pages: int, manager_logger: ManagerLogger):
        self.web_driver: webdriver = web_driver
        self.pages = pages
        self.manager_logger = manager_logger

    def open_link(self, link: str):
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Abrindo o Link: {link}")
        self.web_driver.get(link)
                
    def page_down(self, count: int):
        for _ in range(count):
            self.web_driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            time.sleep(random.randint(1, 10)/5)
            
    def page_up(self, count: int):
        for _ in range(count):
            self.web_driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
            time.sleep(random.randint(1, 10)/5)
            
    def content(self, link: str) -> list:
        films: list = []
        
        count: int = self.pages*2
        
        self.open_link(link)
        self.page_down(count)
        self.web_driver.find_element(By.ID, "pagination_page_1").find_element(By.CSS_SELECTOR, ".no_click.load_more").click()
        self.page_up(count)
        
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Capturando os filmes.")
        for i in range(self.pages):
            elements = self.web_driver.find_element(By.ID, f"page_{i+1}").find_elements(By.CSS_SELECTOR, ".card.style_1")
            for element in elements:
                try:
                    
                    films.append(FilmsModel(
                        element.find_element(By.CLASS_NAME, "image").find_element(By.TAG_NAME, "img").get_attribute("src"),
                        element.find_element(By.CLASS_NAME, "content").find_element(By.TAG_NAME, "h2").text,
                        element.find_element(By.CLASS_NAME, "content").find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").get_attribute("href"),
                        element.find_element(By.CLASS_NAME, "content").find_element(By.TAG_NAME, "p").text
                    ))
                    time.sleep(random.randint(1, 10)/10)
                except:
                    self.manager_logger.messageLogger(f"{self.manager_logger.warn()} Elemento buscado não existe.")
                
                time.sleep(random.randint(1, 10)/10)   
        
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Titulos capturados com sucesso.")
        return films

        