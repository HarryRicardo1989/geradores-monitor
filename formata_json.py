from database import DATABASE
from datetime import datetime
from collections import defaultdict


class JsonFy:
    def __init__(self):
        self.__read = DATABASE()

    def json_data(self, tempo_coleta):
        pcdData = []
        data = self.__read.select_DB(horas_de_coleta=tempo_coleta)
        host_geradores = defaultdict(list)
        for row_db in data:
            hostname_db, data_hora_db, temperatura_ar_db, temperatura_orvalho_db, umidade_db, pressao_local_db,correnteFaseA_db,correnteFaseB_db, correnteFaseC_db, correnteNeutro_db, statusEnergia_db = row_db

            host_geradores[hostname_db].append({
                "timestamp": datetime.timestamp(data_hora_db),
                "hostname": hostname_db,
                "temperatura_ar": temperatura_ar_db,
                "temperatura_orvalho": temperatura_orvalho_db,
                "umidade": umidade_db,
                "pressao_local": pressao_local_db,
                "corrente_Fase_A": correnteFaseA_db,
                "corrente_Fase_B": correnteFaseB_db,
                "corrente_Fase_C": correnteFaseC_db,
                "corrente_Neutro": correnteNeutro_db,
                "status_Energia" : statusEnergia_db
                 })

        return host_geradores

    def json_minMaxMed_data(self, dias):
        pcdData = []
        data = self.__read.min_max_med_DB(dias)
        host_geradores2 = defaultdict(list)
        for row_db in data:
            hostname, data_hora_db, min_temperatura,max_temperatura, med_temperatura, min_temperatura_orvalho, max_temperatura_orvalho, med_temperatura_orvalho, min_umidade, max_umidade, med_umidade, min_pressao_local, max_pressao_local, med_pressao_local,min_corrente_fase_A, max_corrente_fase_A, med_corrente_fase_A,min_corrente_fase_B, max_corrente_fase_B, med_corrente_fase_B,min_corrente_fase_C, max_corrente_fase_C, med_corrente_fase_C,min_corrente_fase_Neutro, max_corrente_fase_Neutro, med_corrente_fase_Neutro,min_status_energia, max_status_energia, med_status_energia = row_db

            host_geradores2[hostname].append({
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
                "pressao_local_max": float(max_pressao_local),
                "max_corrente_fase_A":float(max_corrente_fase_A),
                "med_corrente_fase_A":float(med_corrente_fase_A),
                "min_corrente_fase_B":float(min_corrente_fase_B),
                "max_corrente_fase_B":float(max_corrente_fase_B),
                "med_corrente_fase_B":float(med_corrente_fase_B),
                "min_corrente_fase_C":float(min_corrente_fase_C),
                "max_corrente_fase_C":float(max_corrente_fase_C),
                "med_corrente_fase_C":float(med_corrente_fase_C),
                "min_corrente_fase_Neutro":float(min_corrente_fase_Neutro),
                "max_corrente_fase_Neutro":float(max_corrente_fase_Neutro),
                "med_corrente_fase_Neutro":float(med_corrente_fase_Neutro),
                "min_status_energia":float(min_status_energia),
                "max_status_energia":float(max_status_energia),
                "med_status_energia":float(med_status_energia),

            })
        return host_geradores2

    def json_minMaxMedHora_data(self, horas):
        pcdData = []
        data = self.__read.min_max_med_hora_DB(horas)
        host_geradores3 = defaultdict(list)

        for row_db in data:
            hostname, datadia, hora, min_temperatura,max_temperatura, med_temperatura, min_temperatura_orvalho, max_temperatura_orvalho, med_temperatura_orvalho, min_umidade, max_umidade, med_umidade, min_pressao_local, max_pressao_local, med_pressao_local,min_corrente_fase_A, max_corrente_fase_A, med_corrente_fase_A,min_corrente_fase_B, max_corrente_fase_B, med_corrente_fase_B,min_corrente_fase_C, max_corrente_fase_C, med_corrente_fase_C,min_corrente_fase_Neutro, max_corrente_fase_Neutro, med_corrente_fase_Neutro,min_status_energia, max_status_energia, med_status_energia = row_db
            data_hora = f'{datadia} {hora}:00:00'

            host_geradores3[hostname].append({
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
                "min_corrente_fase_A":float(min_corrente_fase_A),
                "pressao_local_max":float(max_pressao_local),
                "max_corrente_fase_A":float(max_corrente_fase_A),
                "med_corrente_fase_A":float(med_corrente_fase_A),
                "min_corrente_fase_B":float(min_corrente_fase_B),
                "max_corrente_fase_B":float(max_corrente_fase_B),
                "med_corrente_fase_B":float(med_corrente_fase_B),
                "min_corrente_fase_C":float(min_corrente_fase_C),
                "max_corrente_fase_C":float(max_corrente_fase_C),
                "med_corrente_fase_C":float(med_corrente_fase_C),
                "min_corrente_fase_Neutro":float(min_corrente_fase_Neutro),
                "max_corrente_fase_Neutro":float(max_corrente_fase_Neutro),
                "med_corrente_fase_Neutro":float(med_corrente_fase_Neutro),
                "min_status_energia":float(min_status_energia),
                "max_status_energia":float(max_status_energia),
                "med_status_energia":float(med_status_energia),
            })
        return host_geradores3
