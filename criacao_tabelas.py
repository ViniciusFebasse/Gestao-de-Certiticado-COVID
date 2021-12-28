# Importação da biblioteca para gestão do banco de dados
import sqlite3

# Criação do banco de dados
banco = sqlite3.connect('certificado-covid.db')

# Criação do cursor para manipulação do banco de dados
cursor = banco.cursor()

# Criação da tabela de utentes
cursor.execute("""CREATE TABLE IF NOT EXISTS "utentes" (
	            "NUS"	INTEGER NOT NULL UNIQUE,
                "NOME"	TEXT,
                "TELEMOVEL"	TEXT,
                "MORADA"	TEXT,
                "CARTAO_CIDADAO"	TEXT,
                "DATA_NASCIMENTO"	INTEGER,
                "DOENCA"	INTEGER,
                PRIMARY KEY("NUS" AUTOINCREMENT)
                );""")

# Criação da tabela de testes
cursor.execute("""CREATE TABLE IF NOT EXISTS "testes" (
                "id" INTEGER NOT NULL UNIQUE,
                "NUS"	INTEGER,
                "Data_Teste"	DATETIME,
                "Resultado"	TEXT,
                "Tipo_Teste"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT),
                FOREIGN KEY("NUS") REFERENCES "utentes"("NUS")
            );""")

# Criação da tabela de vacinação
cursor.execute("""CREATE TABLE IF NOT EXISTS "vacinacao" (
                "id" INTEGER NOT NULL UNIQUE,
                "NUS"	INTEGER,
                "Tipo_Vacina"	TEXT,
                "Dosagem"	REAL,
                "Data"	DATETIME,
                "Toma"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT),
                FOREIGN KEY("NUS") REFERENCES "utentes"("NUS")
            );""")

# Criação da tabela de certificados
cursor.execute("""CREATE TABLE IF NOT EXISTS "certificados" (
                "id"	INTEGER NOT NULL UNIQUE,
                "NUS"	INTEGER,
                "quantidade_vacina"	INTEGER,
                "ultimo_teste"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT),
                FOREIGN KEY("NUS") REFERENCES "utentes"("NUS"),
                FOREIGN KEY("ultimo_teste") REFERENCES "testes"("id")
            );""")


# Criação da tabela de log
cursor.execute("""CREATE TABLE IF NOT EXISTS "log" (
                "id" INTEGER NOT NULL UNIQUE,
                "NUS"	INTEGER,
                "atualiza_vacina"	TEXT,
                "atualiza_teste"	TEXT,
                "atualiza_utente"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT),
                FOREIGN KEY("NUS") REFERENCES "utentes"("NUS")
            );""")


