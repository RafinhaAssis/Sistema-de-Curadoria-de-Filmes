from pathlib import Path
from service.commons.manager_logger import ManagerLogger

def folder_create(path: str, manager_logger: ManagerLogger):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        manager_logger.messageLogger(f"{manager_logger.info()} A pasta: {path} foi criada com sucesso.")
    except Exception as e:
        manager_logger.messageLogger(f"{manager_logger.error()} Não foi possivel criar a pasta: {path}")
        manager_logger.exitApp()
