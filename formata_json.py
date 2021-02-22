from database import DATABASE
from datetime import datetime
from collections import defaultdict


class JsonFy:
    def __init__(self):
        self.__read = DATABASE()

    def json_data(self, tempo_coleta):
        pcdData = []
        data = self.__read.select_DB(horas_de_coleta=tempo_coleta)
        host_DC = defaultdict(list)
        for row_db in data:
            hostname_db, data_hora_db, temperatura_ar_db, temperatura_orvalho_db, umidade_db, pressao_local_db = row_db

            host_DC[hostname_db].append({
                "timestamp": datetime.timestamp(data_hora_db),
                "hostname": hostname_db,
                "temperatura_ar": temperatura_ar_db,
                "temperatura_orvalho": temperatura_orvalho_db,
                "umidade": umidade_db,
                "pressao_local": pressao_local_db
            })

        return host_DC

    def json_minMaxMed_data(self, dias):
        pcdData = []
        data = self.__read.min_max_med_DB(dias)
        host_DC2 = defaultdict(list)
        for row_db in data:
            hostname, data_hora_db, min_temperatura, max_temperatura, med_temperatura, min_temperatura_orvalho, max_temperatura_orvalho, med_temperatura_orvalho, min_umidade, max_umidade, med_umidade, min_pressao_local, max_pressao_local, med_pressao_local = row_db

            host_DC2[hostname].append({
                "timestamp": datetime.timestamp(data_hora_db),
                "hostname": hostname,
                "temperatura_ar": float(med_temperatura),
                "temperatura_ar_min": float(min_temperatura),
                "temperatura_ar_max": float(max_temperatura),
                "temperatura_orvalho": float(med_temperatura_orvalho),
                "temperatura_orvalho_min": float(min_temperatura_orvalho),
                "temperatura_orvalho_max": float(max_temperatura_orvalho),
                "umidade": float(med_umidade),
                "umidade_min": float(min_umidade),
                "umidade_max": float(max_umidade),
                "pressao_local": float(med_pressao_local),
                "pressao_local_min": float(min_pressao_local),
                "pressao_local_max": float(max_pressao_local)
            })
        return host_DC2

    def json_minMaxMedHora_data(self, horas):
        pcdData = []
        data = self.__read.min_max_med_hora_DB(horas)
        host_DC3 = defaultdict(list)

        for row_db in data:
            hostname, datadia, hora, min_temperatura, max_temperatura, med_temperatura, min_temperatura_orvalho, max_temperatura_orvalho, med_temperatura_orvalho, min_umidade, max_umidade, med_umidade, min_pressao_local, max_pressao_local, med_pressao_local = row_db
            data_hora = f'{datadia} {hora}:00:00'

            host_DC3[hostname].append({
                "timestamp": datetime.timestamp(datetime. strptime(data_hora, '%Y-%m-%d %H:%M:%S')),
                "hostname": hostname,
                "temperatura_ar": float(med_temperatura),
                "temperatura_ar_min": float(min_temperatura),
                "temperatura_ar_max": float(max_temperatura),
                "temperatura_orvalho": float(med_temperatura_orvalho),
                "temperatura_orvalho_min": float(min_temperatura_orvalho),
                "temperatura_orvalho_max": float(max_temperatura_orvalho),
                "umidade": float(med_umidade),
                "umidade_min": float(min_umidade),
                "umidade_max": float(max_umidade),
                "pressao_local": float(med_pressao_local),
                "pressao_local_min": float(min_pressao_local),
                "pressao_local_max": float(max_pressao_local)
            })
        return host_DC3