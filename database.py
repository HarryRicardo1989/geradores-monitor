import mariadb
import dbAccount as db
import datetime as dt


class DATABASE:
    def __init__(self):
        self .connect = mariadb.connect(
            user=db.user,
            password=db.password,
            host=db.host,
            database=db.database
        )
        pass

    def insert_DB(self, hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local, corrente_fase_A, corrente_fase_B, corrente_fase_C, corrente_Neutro, status_energia):

        conn = self.connect
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO gerador_dados_tbl ( hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local,corrente_fase_A,corrente_fase_B, corrente_fase_C, corrente_Neutro, status_energia) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local, corrente_fase_A,corrente_fase_B, corrente_fase_C, corrente_Neutro, status_energia))
            print("ok")
        except mariadb.Error as e:
            print(f'Error: {e}')
        conn.commit()
        conn.close()

    def select_DB(self, horas_de_coleta=1.0):
        timedelta = dt.timedelta(hours=horas_de_coleta)
        data = dt.datetime.now() - timedelta
        tempo = data.strftime("%Y-%m-%d %H:%M:%S")
        conn = self.connect
        cur = conn.cursor()
        cur.execute(
            f'SELECT hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local, corrente_fase_A, corrente_fase_B, corrente_fase_C, corrente_Neutro,status_energia FROM gerador_dados_tbl where data_hora > "{tempo}" order by data_hora desc;')
        # cur.execute(f'SELECT * FROM tb_airquality order by ID desc')
        row_list = []
        for data in cur:
            row_list.append(data)

        conn.commit()
        conn.close()
        return row_list

    def min_max_med_DB(self, dias=0.0):
        timedelta = dt.timedelta(days=dias)
        data = dt.datetime.now() - timedelta
        tempo = data.strftime("%Y-%m-%d")
        conn = self.connect
        cur = conn.cursor()
        cur.execute(
            f' SELECT hostname, data_hora,MIN(temperatura_ar) AS min_temperatura,MAX(temperatura_ar) AS max_temperatura, AVG(temperatura_ar) AS med_temperatura, MIN(temperatura_orvalho) AS min_temperatura_orvalho, MAX(temperatura_orvalho) AS max_temperatura_orvalho, AVG(temperatura_orvalho) AS med_temperatura_orvalho,  MIN(umidade) AS min_umidade, MAX(umidade) AS max_umidade, AVG(umidade) AS med_umidade, MIN(pressao_local) AS min_pressao_local, MAX(pressao_local) AS max_pressao_local, AVG(pressao_local) AS med_pressao_local,MIN(corrente_fase_A) AS min_corrente_fase_A, MAX(corrente_fase_A) AS max_corrente_fase_A, AVG(corrente_fase_A) AS med_corrente_fase_A,MIN(corrente_fase_B) AS min_corrente_fase_B, MAX(corrente_fase_B) AS max_corrente_fase_B, AVG(corrente_fase_B) AS med_corrente_fase_B, MIN(corrente_fase_C) AS min_corrente_fase_C, MAX(corrente_fase_C) AS max_corrente_fase_C, AVG(corrente_fase_C) AS med_corrente_fase_C,MIN(corrente_Neutro) AS min_corrente_Neutro, MAX(corrente_Neutro) AS max_corrente_Neutro, AVG(corrente_Neutro) AS med_corrente_Neutro,MIN(status_energia) AS min_status_energia, MAX(status_energia) AS max_status_energia, AVG(status_energia) AS med_status_energiaFROM gerador_dados_tbl WHERE DATE(data_hora) >= "{tempo}"   GROUP BY hostname, DATE(data_hora) order by DATE(data_hora) desc;')
        # cur.execute(f'SELECT * FROM tb_airquality order by ID desc')
        row_list = []
        for data in cur:
            row_list.append(data)

        conn.commit()
        conn.close()
        return row_list

    def min_max_med_hora_DB(self, horas=1.0):
        timedelta = dt.timedelta(hours=horas)
        data = dt.datetime.now() - timedelta
        tempo = data.strftime("%Y-%m-%d %H:%M:%S")
        conn = self.connect
        cur = conn.cursor()
        cur.execute(
            f'SELECT hostname,DATE(data_hora) AS data_referencia, TIME_FORMAT(data_hora, "%H") AS hora, MIN(temperatura_ar) AS min_temperatura, MAX(temperatura_ar) AS max_temperatura, AVG(temperatura_ar) AS med_temperatura, MIN(temperatura_orvalho) AS min_temperatura_orvalho, MAX(temperatura_orvalho) AS max_temperatura_orvalho, AVG(temperatura_orvalho) AS med_temperatura_orvalho,  MIN(umidade) AS min_umidade, MAX(umidade) AS max_umidade, AVG(umidade) AS med_umidade, MIN(pressao_local) AS min_pressao_local, MAX(pressao_local) AS max_pressao_local, AVG(pressao_local) AS med_pressao_local, MIN(corrente_fase_A) AS min_corrente_fase_A, MAX(corrente_fase_A) AS max_corrente_fase_A, AVG(corrente_fase_A) AS med_corrente_fase_A,MIN(corrente_fase_B) AS min_corrente_fase_B, MAX(corrente_fase_B) AS max_corrente_fase_B, AVG(corrente_fase_B) AS med_corrente_fase_B, MIN(corrente_fase_C) AS min_corrente_fase_C, MAX(corrente_fase_C) AS max_corrente_fase_C, AVG(corrente_fase_C) AS med_corrente_fase_C,MIN(corrente_Neutro) AS min_corrente_Neutro, MAX(corrente_Neutro) AS max_corrente_Neutro, AVG(corrente_Neutro) AS med_corrente_Neutro,MIN(status_energia) AS min_status_energia, MAX(status_energia) AS max_status_energia, AVG(status_energia) AS med_status_energiaFROM gerador_dados_tbl WHERE data_hora >= "{tempo}"  GROUP BY 1,2,3; ')
        # cur.execute(f'SELECT * FROM tb_airquality order by ID desc')
        row_list = []
        for data in cur:
            row_list.append(data)

        conn.commit()
        conn.close()
        row_list.reverse()
        return row_list


""" for item in DATABASE().min_max_med_hora_DB(2):
    print(item) """
