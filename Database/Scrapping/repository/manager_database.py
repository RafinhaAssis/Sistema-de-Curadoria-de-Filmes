from service.commons.manager_logger import ManagerLogger

import psycopg2
import sys

class ManagerDatabase():
    def __init__(self, manager_logger:ManagerLogger,  database: str, user: str, host: str, password: str, port: int):
        self.manager_logger = manager_logger
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Estabelecendo conexão com a base de dados")
        
        try:
            self.conn = psycopg2.connect(database = database, 
                            user = user, 
                            host= host,
                            password = password,
                            port = port)
            self.manager_logger.messageLogger(f"{self.manager_logger.info()} Conexão estabelecida com sucesso.")

        except Exception as e:
            self.manager_logger.messageLogger(f"{self.manager_logger.error()} Erro ao estabelecer conexão")
            sys.exit(0)
    
    def get_connection(self):
        return self.conn
    
    def close_connection(self) -> None:
        self.conn.close()