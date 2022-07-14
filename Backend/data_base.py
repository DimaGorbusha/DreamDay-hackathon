import psycopg2
from random import randint
# huy\\//govno228
class DB:
    """
        Класс базы данных со всеми методами для получения, изменения всех данных в таблицах.
        Существует три таблицы: users - таблица с пользователями и их данными (логин, пароль, уровень знания англа, имя для обращения в боте, количество очков), одна строка - один пользователь; free_tests - бесплатные вопросы и ответы (уровень, вопрос, ответ), одна строка - один вопрос/ответ; premium_tests - платные вопросы и ответы (уровень, вопрос, ответ), одна строка - один вопрос/ответ.
    """
    def __DB_connect(self) -> None: # Метод соединения с бд
        self.connection = psycopg2.connect(dbname='postgres', 
                                    user='postgres', 
                                    password='a*N//??0385-&&81',
                                    host='localhost')


    def __init__(self) -> None: # Метод инициализации объекта классаа
        self.__create_table()

    def __create_table(self) -> None: # Метод создания таблиц
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_create_tb_test_data_query = """CREATE TABLE IF NOT EXISTS users (
                    user_name TEXT PRIMARY KEY,
                    user_email TEXT, 
                    user_pass TEXT)""" # Создание таблицы пользователей
                cursor.execute(sql_create_tb_test_data_query)
                
                sql_create_tb_free_test_query = """CREATE TABLE IF NOT EXISTS dreams (
                    user_email TEXT,
                    dream_name TEXT PRIMARY KEY, 
                    img TEXT,
                    drean_tags TEXT,
                    dream_dt TEXT)""" # Создание таблицы dreams
                cursor.execute(sql_create_tb_free_test_query)

                sql_create_tb_premium_test_query = """CREATE TABLE IF NOT EXISTS goals(
                    user_email TEXT,
                    goal_name TEXT UNIQUE,
                    goal_descr TEXT,
                    goal_img TEXT,
                    goal_start_dt TIMESTAMP,
                    goal_success TEXT,
                    goal_end_dt TIMESTAMP,
                    goal_tags TEXT)""" # Создание таблицы goals
                cursor.execute(sql_create_tb_premium_test_query)

                sql_create_tb_premium_test_query = """CREATE TABLE IF NOT EXISTS tasks(
                    user_email TEXT,
                    task_name TEXT UNIQUE,
                    task_descr TEXT,
                    task_start_dt TIMESTAMP,
                    task_end_dt TIMESTAMP,
                    task_tags TEXT)""" # Создание таблицы tasks
                cursor.execute(sql_create_tb_premium_test_query)

                sql_create_tb_premium_test_query = """CREATE TABLE IF NOT EXISTS notes(
                    user_email TEXT,
                    note_name TEXT UNIQUE,
                    note_descr TEXT,
                    note_img TEXT,
                    note_dt TEXT,
                    note_tags TEXT)""" # Создание таблицы tasks
                cursor.execute(sql_create_tb_premium_test_query)
        finally:
            self.connection.close()


    def insert_data_user(self, name: str, user_email: str, user_pass: str) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO users (name, user_email, password) VALUES (%s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                             name, user_email, user_pass))
        finally:
            self.connection.close()


    def insert_data_dream(self, user_email: str, dream_name: str, img: str, dream_tags:str, dream_dt) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO dreams (user_email, dream_name, img, dream_tags, dream_dt) VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                             user_email, dream_name, img, dream_tags, dream_dt))
        finally:
            self.connection.close()


    def insert_data_goal(self, user_email: str, goal_name: str, goal_descr: str, goal_img:str, goal_start_dt, goal_success:str, goal_end_dt, goal_tags:str) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO goals (user_email, goal_name, goal_descr, goal_img, goal_start_dt, goal_success, goal_end_dt, goal_tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                             user_email, goal_name, goal_descr, goal_img, goal_start_dt, goal_success, goal_end_dt, goal_tags))
        finally:
            self.connection.close()


    def insert_data_tsak(self, user_email: str, task_name: str, task_descr: str, task_start_dt, task_end_dt, task_tags:str) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO tasks (user_email, task_name, task_descr, task_start_dt, task_end_dt, task_tags) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                             user_email, task_name, task_descr, task_start_dt, task_end_dt, task_tags))
        finally:
            self.connection.close()


    def insert_data_tsak(self, user_email: str, note_name: str, note_descr: str, note_img:str, notr_dt, note_tags:str) -> None: # Метод создания новой записи в таблице пользователей
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_insert_data_query = """INSERT INTO tasks (user_email, note_name, note_descr, note_img, notr_dt, note_tags) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql_insert_data_query, (
                             user_email, note_name, note_descr, note_img, notr_dt, note_tags))
        finally:
            self.connection.close()
    
    def delete_dream(self, dream_name: str) -> None: # Метод удаления dream 
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_delete_data_query = """DELETE FROM dreams WHERE dream_name = %s"""
                cursor.execute(sql_delete_data_query, (dream_name,))
        finally:
            self.connection.close()

    
    def delete_goal(self, goal_name: str) -> None: # Метод удаления goal
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_delete_data_query = """DELETE FROM goals WHERE goal_name = %s"""
                cursor.execute(sql_delete_data_query, (goal_name,))
        finally:
            self.connection.close()


    def delete_task(self, task_name: str) -> None: # Метод удаления task
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_delete_data_query = """DELETE FROM tasks WHERE task_name = %s"""
                cursor.execute(sql_delete_data_query, (task_name,))
        finally:
            self.connection.close()


    def delete_note(self, note_name: str) -> None: # Метод удаления note
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_delete_data_query = """DELETE FROM notes WHERE note_name = %s"""
                cursor.execute(sql_delete_data_query, (note_name,))
        finally:
            self.connection.close()

    # def update_user_name(self, new_name: str, chat_id: str) -> None: # Метод обновления имени
    #     self.__DB_connect()
    #     try:
    #         with self.connection.cursor() as cursor:
    #             self.connection.autocommit = True
    #             sql_update_user_name_query = """UPDATE users SET name = %s WHERE login = %s"""
    #             cursor.execute(sql_update_user_name_query, (new_name, chat_id))
    #     finally:

    #         self.connection.close()

    
    # def update_user_score(self, score: int, chat_id: str) -> None: # Метод обновления пароля в таблице пользователей
    #     self.__DB_connect()
    #     try:
    #         with self.connection.cursor() as cursor:
    #             self.connection.autocommit = True
    #             sql_update_user_name_query = """UPDATE users SET score = %s WHERE login = %s"""
    #             cursor.execute(sql_update_user_name_query, (score, chat_id))
    #     finally: 

    #         self.connection.close()


    # def update_user_password(self, new_password: str, chat_id: str) -> None: # Метод обновления пароля в таблице пользователей
    #     self.__DB_connect()
    #     try:
    #         with self.connection.cursor() as cursor:
    #             self.connection.autocommit = True
    #             sql_update_user_name_query = """UPDATE users SET password = %s WHERE chat_id = %s"""
    #             cursor.execute(sql_update_user_name_query, (new_password, chat_id))
    #     finally:

    #         self.connection.close()

    
    def get_user_data(self, user_email:str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT name, user_pass  FROM users WHERE user_email = %s"""
                cursor.execute(sql_find_login_query, (user_email,))
                return list(cursor.fetchone())
        finally:
            self.connection.close()

    
    def get_all_dream(self, user_email: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT dream_name, dream_dt, dream_tags  FROM users WHERE user_email = %s"""
                cursor.execute(sql_find_login_query, (user_email,))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_dream(self, user_email: str, dream_name: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT dream_name, img, dream_dt, dream_tags  FROM users WHERE user_email = %s, dream_name = %s"""
                cursor.execute(sql_find_login_query, (user_email, dream_name))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_all_goals(self, user_email: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT goal_name, goal_start_dt, goal_end_dt, goal_tags  FROM users WHERE user_email = %s"""
                cursor.execute(sql_find_login_query, (user_email,))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_goal(self, user_email: str, goal_name: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT goal_descr, goal_img, goal_start_dt, goal_success, goal_end_dt, goal_tags  FROM users WHERE user_email = %s, goal_name = %s"""
                cursor.execute(sql_find_login_query, (user_email, goal_name))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_all_tasks(self, user_email: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT task_name, task_end_dt, task_tags  FROM users WHERE user_email = %s"""
                cursor.execute(sql_find_login_query, (user_email,))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_task(self, user_email: str, task_name: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT task_descr, task_start_dt, task_end_dt, task_tags  FROM users WHERE user_email = %s, task_name = %s"""
                cursor.execute(sql_find_login_query, (user_email, task_name))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_all_notes(self, user_email: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT note_name, note_dt, note_tags  FROM users WHERE user_email = %s"""
                cursor.execute(sql_find_login_query, (user_email,))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()


    def get_note(self, user_email: str, note_name: str) -> list: # Метод получения всех данных пользователя
        self.__DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                sql_find_login_query = """SELECT note_descr, note_img, note_dt, task_tags FROM users WHERE user_email = %s, note_name = %s"""
                cursor.execute(sql_find_login_query, (user_email, note_name))
                return list(cursor.fetcgall())
        finally:
            self.connection.close()

