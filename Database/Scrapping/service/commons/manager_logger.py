from rich.console import Console
from rich.theme import Theme
from datetime import datetime
import sys
import os

class ManagerLogger:
    
    console = Console(theme=Theme({"success": "green", "error":"bold red"}))
    file_logs = f"logs/log_{datetime.now().strftime("%d%m%Y_%H%M%S")}.logs"

    
    def create_and_edit_log_file(self, message: str):
        os.makedirs("logs", exist_ok=True)
        with open(self.file_logs, 'a', encoding='utf-8') as arquivo:
            arquivo.write(message[message.find(']')+1:].replace('[/]', "")+"\n")
        
    
    def messageLogger(self, msg:str):
        self.console.print(msg)
        self.create_and_edit_log_file(msg)
    
    def getDate(self):
        return datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    def info(self) -> str:
        return f"[bold green][ {self.getDate()} ] [ INFO ][/]"
    
    def warn(self) -> str:
        return f"[bold yellow][ {self.getDate()} ] [ WARN ][/]"
    
    def error(self) -> str:
        return f"[error ][ {self.getDate()} ] [ ERRO ][/]"
    
    def exit(self) -> str:
        return f"[error][ {self.getDate()} ] [ EXIT ][/]"
    
    def exitApp(self) -> None:
        self.console.print(f"{self.exit()} Fechando aplicação devido a erros")
        sys.exit(1)