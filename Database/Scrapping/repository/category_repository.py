from service.commons.manager_logger import ManagerLogger

class CategoryRepository():
    def __init__(self, manager_logger: ManagerLogger, conn):
        self.manager_logger: ManagerLogger = manager_logger
        self.conn = conn
        self.cur = self.conn.cursor()
        
    def get_all_categories(self) -> list:
        sql: str = "SELECT nm_categorie FROM public.t_sc_categories"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()

        all_categories: list = []
        for row in rows:
            all_categories.append(list(row)[0])
        return all_categories
    
    def get_insert_category(self, categories: list) -> None:
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Categorias a serem inseridas: {categories}")
        data = [(c,) for c in categories]
        sql: str = "INSERT INTO t_sc_categories (nm_categorie ) VALUES (%s)"
        self.cur.executemany(sql, data)
        self.conn.commit()
        self.manager_logger.messageLogger(f"{self.manager_logger.info()} Linhas inseridas com sucesso!")

    