from selenium import webdriver
from selenium.webdriver.common.by import By

from service.component.manager_images import ManagerImages
from service.validation.manager_validation import ManagerValidation
from service.commons.manager_logger import ManagerLogger

from model.films_model import FilmsModel

class ManagerPages():
    def __init__(self, web_driver: webdriver, manager_images: ManagerImages, manager_validation: ManagerValidation, manager_logger: ManagerLogger ):
        self.web_driver: webdriver = web_driver
        self.manager_images = manager_images
        self.manager_validation = manager_validation
        self.manager_logger = manager_logger
        
    def open_link(self, link: str) -> None:
        self.web_driver.get(link)
        
    def get_content(self, film: FilmsModel) -> FilmsModel:
        age_reecomendation: list  = self.web_driver.find_elements(By.CLASS_NAME, "certification")
        if age_reecomendation:
            film.set_age_recomendation(age_reecomendation[0].text)
        
        film.set_time_film(self.manager_validation.convert_hour(self.web_driver.find_element(By.CLASS_NAME, "runtime").text))
        film.set_dt_film(self.manager_validation.convert_date(film.get_dt_film()))
        
        for element in self.web_driver.find_element(By.CLASS_NAME, "genres").find_elements(By.TAG_NAME, "a"):
            film.set_category(element.text)
            
            
        content = self.web_driver.find_element(By.CLASS_NAME, "header_info")
        
        film.set_sinopse(content.find_element(By.CLASS_NAME, "overview").text)
        
        link_poster: str = self.manager_images.clear_link(self.web_driver.find_element(By.CSS_SELECTOR, ".poster.w-full").get_attribute("srcset"))
        extension = self.manager_images.get_extension(link_poster)
        
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Realizando o download do poster do filme.")
        film.set_image_nice(self.manager_images.download_image_for_link(link_poster, extension) )
        
        
        return film
        
        
        
            