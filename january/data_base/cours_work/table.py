import sqlite3


def just_sql_command(sql_command):
    connection = sqlite3.connect("Store.db")
    cursor = connection.cursor()
    sql = sql_command
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    connection.close()


def create_table_and_triggers():

    sql_create_table_movements = """CREATE TABLE IF NOT EXISTS "movements" (
	"id_movement"	INTEGER NOT NULL,
	"id_product"	INTEGER,
	"count"	INTEGER,
	"id_organization"	INTEGER,
	"data"	TEXT,
	"id_who_made_movement"	INTEGER,
	PRIMARY KEY("id_movement")
);"""
    just_sql_command(sql_create_table_movements)


    just_sql_command(sql_create_table_movements)
    sql_cleate_table_organization = """CREATE TABLE IF NOT EXISTS "organization" (
	"id_organization"	INTEGER,
	"name_organization"	TEXT UNIQUE,
	PRIMARY KEY("id_organization")
);
    """
    just_sql_command(sql_cleate_table_organization)


    sql_cleate_table_product = """CREATE TABLE IF NOT EXISTS "product" (
	"id_product"	INTEGER UNIQUE,
	"name_product"	TEXT,
	PRIMARY KEY("id_product" AUTOINCREMENT)
);"""
    just_sql_command(sql_cleate_table_product)


    sql_cleate_table_users = """CREATE TABLE IF NOT EXISTS "users" (
	"id_user_in_users"	INTEGER NOT NULL,
	"login_user_in_users"	TEXT,
	"password_user_in_users"	TEXT,
	"name_surname_in_users"	TEXT,
	PRIMARY KEY("id_user_in_users" AUTOINCREMENT)
);"""
    just_sql_command(sql_cleate_table_users)



    sql_create_table_log_delete = """CREATE TABLE IF NOT EXISTS "log_delete" (
        "id_movement"	INTEGER,
        "id_product"	INTEGER,
        "count"	INTEGER,
        "id_organization"	INTEGER,
        "data"	TEXT,
        "id_who_made_movement"	INTEGER,
        "data_when_made_delete"	TEXT
    );"""
    just_sql_command(sql_create_table_log_delete)

    ## создание триггера после удаление  мы все записываем в отдельную таблицу
    sql_create_trigger_after_del = """CREATE TRIGGER IF NOT EXISTS after_del  AFTER DELETE  
    ON movements
    BEGIN
    INSERT INTO log_delete(id_movement, id_product, count, id_organization, data, id_who_made_movement, data_when_made_delete) 
    VALUES (old.id_movement, old.id_product, old.count, old.id_organization, old.data, old.id_who_made_movement, datetime('now'));
    END;"""
    just_sql_command(sql_create_trigger_after_del)


    sql_create_table_log_update = """CREATE TABLE IF NOT EXISTS "log_update" (
	"id"	INTEGER,
	"id_movement"	INTEGER,
	"id_product"	INTEGER,
	"count"	INTEGER,
	"id_organization"	INTEGER,
	"data"	TEXT,
	"id_who_made_movement"	INTEGER,
	"new_id_product"	INTEGER,
	"new_count"	INTEGER,
	"new_id_organization"	INTEGER,
	"new_data"	TEXT,
	PRIMARY KEY("id")
);"""
    just_sql_command(sql_create_table_log_update)


    sql_delete_after_test = "DROP TRIGGER IF EXISTS after_update"
    just_sql_command(sql_delete_after_test)

    sql_create_trigger_update = """CREATE TRIGGER IF NOT EXISTS after_update AFTER UPDATE  
    ON movements
    BEGIN
    INSERT INTO log_update(id_movement, id_product, count, id_organization, data, id_who_made_movement, new_id_product, new_count, new_id_organization, new_data ) 
    VALUES (old.id_movement, old.id_product, old.count, old.id_organization, old.data, old.id_who_made_movement, new.id_product, new.count, new.id_organization, datetime('now'));
    END;"""

    just_sql_command(sql_create_trigger_update)
