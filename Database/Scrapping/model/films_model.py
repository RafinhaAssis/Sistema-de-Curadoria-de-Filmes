
class FilmsModel():
    def __init__(self, link_image: str, name: str, link_page: str, dt_film: str):
        self.link_image = link_image
        self.name = name
        self.link_page = link_page
        self.dt_film = dt_film
        self.age_recomendation: str = ""
        self.time_film: str = ""
        self.category: list = []
        self.sinopse: str = ""
        self.image_nice: str = ""
        
        
    def to_string(self) -> str:
        return f"""
    {{
    "link_image": "{self.link_image}",
    "name": "{self.name}",
    "link_page": "{self.link_page}",
    "dt_film": "{self.dt_film}",
    "age_recomendation": "{self.age_recomendation}",
    "time_film": "{self.time_film}",
    "category": {self.category},
    "sinopse": "{self.sinopse}",
    "image_nice": "{self.image_nice}"
    }}
    """   
    def set_dt_film(self, dt_film: str) -> None:
        self.dt_film = dt_film
        
    def set_age_recomendation(self, age_recomendation: str) -> None:
        self.age_recomendation = age_recomendation
        
    def set_time_film(self, time_film: str) -> None:
        self.time_film = time_film  
              
    def set_sinopse(self, sinopse: str) -> None:
        self.sinopse = sinopse      
          
    def set_category(self, category: str) -> None:
        self.category.append(category)
        
    def set_image_nice(self, image_nice: str) -> None:
        self.image_nice = image_nice        
                
    def get_link_image(self) -> str:
        return self.link_image
    
    def get_name(self) -> str:
        return self.name
    
    def get_link_page(self) -> str:
        return self.link_page
    
    def get_dt_film(self) -> str:
        return self.dt_film
    
    def get_category(self) -> list:
        return self.category
    
