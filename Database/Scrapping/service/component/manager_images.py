import requests
import re

class ManagerImages():
        
    def __clear_name(self, name):
        return re.sub(r'[^a-zA-Z0-9]', '', name)
        
    def clear_link(sself, links: str) -> str:
        link: list = links.split(",")
        value: list = []
        for lk in link:
            value.append(lk.strip()[0: lk.strip().index(" ")].strip())
            
        return value[len(value)-1]
    
    def download_image_for_link(self, link: str, file_extension: str) -> str:
        response = requests.get(link)
    
        if response.status_code == 200:
            
            link = link[::-1]
            position:int = link.index("/")
            lk = link[0: position][::-1].replace(f".{file_extension}", "")
            
            file_name: str = f"{self.__clear_name(lk)}.{file_extension}"
            
            with open(f"output/{file_name}", 'wb') as file:
                file.write(response.content)
            
            return file_name
        return ""
            
    def get_extension(self, link: str) -> str:
        return link[::-1][0: 3][::-1]
                


