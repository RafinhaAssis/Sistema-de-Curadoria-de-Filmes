from selenium import webdriver
from selenium.webdriver.edge.options import Options

from service.manager_films import ManagerFilms
from service.manager_page import ManagerPages
from service.component.manager_images import ManagerImages
from service.validation.manager_validation import ManagerValidation
from service.commons.manager_logger import ManagerLogger
from service.component.manager_configs import ConfigLoader

from service.component.initializer_app_component import folder_create

import time
import random

def main():
    manager_logger: ManagerLogger =  ManagerLogger()
    manager_logger.messageLogger(f"{manager_logger.info()} Definindo configuração da aplicação.")
    
    configs = ConfigLoader().CONFIGS
    
    link: str = f"{configs['LINK_WEBSITE']}/movie"
    
    
    manager_logger.messageLogger(f"{manager_logger.info()} Definindo configuração do navegor")
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
    options.add_argument("--log-level=3") 
    
    manager_logger.messageLogger(f"{manager_logger.info()} Criando pasta de saida.")
    folder_create("output", manager_logger)
    
    manager_logger.messageLogger(f"{manager_logger.info()} Abrindo navegador.")
    web_driver = webdriver.Edge(options=options)
    web_driver.maximize_window()
    
    manager_validation: ManagerValidation = ManagerValidation()
    manager_films: ManagerFilms = ManagerFilms(web_driver, 1, manager_logger)
    manager_images: ManagerImages = ManagerImages()
    manager_pages: ManagerPages = ManagerPages(web_driver, manager_images, manager_validation, manager_logger)
    
    
    films: list = manager_films.content(link)

    manager_logger.messageLogger(f"{manager_logger.info()} Capturando detalhe de cada filme.")
    
    categories_insert: list = []
    for film in films:
        manager_logger.messageLogger(f"{manager_logger.info()} Buscando dados do filme: {film.get_name()}")
        manager_pages.open_link(film.get_link_page())
        film_manipulat = manager_pages.get_content(film)
        
        categories: list = film_manipulat.get_category()
        for category in categories:
            if category not in categories_insert:
                categories_insert.append(category)
            
        time.sleep(random.randint(1, 10)/5)
        
    web_driver.quit()
    print(categories_insert)
    


if __name__ == "__main__":
    main()