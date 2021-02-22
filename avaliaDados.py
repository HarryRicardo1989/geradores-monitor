import os
from nTalkMessenger import NTALK, EMAIL
from time import sleep, time


class AVALIADOR:
    def __init__(self):
        self.flagHighTempPredio = False
        self.flagLowTempPredio = False
        self.flagHighHumidityPredio = False
        self.flagCriticalDewPointPredio = False
        self.flagHighTempCasa = False
        self.flagLowTempCasa = False
        self.flagHighHumidityCasa = False
        self.flagCriticalDewPointCasa = False
        self.avaliatempoPredio = time()
        self.avaliatempoCasa = time()

    def should_update(self, last_update, rate):
        if(time() - last_update) > rate:
            self.avaliatempoPredio = self.avaliatempoCasa = time()
            return True
        return False

    def avalia(self, hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local):
        if hostname == "dcpredio":
            hostname = "DATA CENTER PREDIO"
            if not self.should_update(self.avaliatempoCasa, 300):
                return
            self.atitudePredio(hostname, data_hora, temperatura_ar,
                               temperatura_orvalho, umidade, pressao_local)
            self.avaliatempoCasa = time()

        if hostname == "dccasa":
            hostname = "DATA CENTER CASA"
            if not self.should_update(self.avaliatempoPredio, 300):
                return
            self.atitudeCasa(hostname, data_hora, temperatura_ar,
                             temperatura_orvalho, umidade, pressao_local)
            self.avaliatempoPredio = time()

    def atitudeCasa(self, hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local):

        if temperatura_ar > 25:
            self.flagHighTempCasa = True
            mensagem = f'"Problem: High Temperature on {hostname} at {data_hora}  <br> Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return

        else:
            if self.flagHighTempCasa == True:
                self.flagHighTempCasa = False
                mensagem = f'" Resolved: Normal Temperature on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

        if temperatura_ar < 18:
            self.flagLowTempCasa = True
            mensagem = f'" Problem Low Temperature on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagLowTempCasa == True:
                self.flagLowTempCasa = False
                mensagem = f'" Resolved: Normal Temperature on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

        if umidade > 75:
            self.flagHighHumidityCasa = True
            mensagem = f'" Problem: High Humidity on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagHighHumidityCasa == True:
                self.flagHighHumidityCasa = False
                mensagem = f'" Resolved: Normal Humidity on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

        if temperatura_orvalho >= (temperatura_ar - 2):
            self.flagCriticalDewPointCasa = True
            mensagem = f'" Problem: Critical Dew Point on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagCriticalDewPointCasa == True:
                self.flagCriticalDewPointCasa = False
                mensagem = f'" Resolved: Normal Dew Point on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

    def atitudePredio(self, hostname, data_hora, temperatura_ar, temperatura_orvalho, umidade, pressao_local):

        if temperatura_ar > 25:
            self.flagHighTempPredio = True
            mensagem = f'"Problem: High Temperature on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagHighTempPredio == True:
                self.flagHighTempPredio = False
                mensagem = f'"Resolved: High Temperature on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

        if temperatura_ar < 18:
            self.flagLowTempPredio = True
            mensagem = f'" Problem: Low Temperature on {hostname} at {data_hora}  <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagLowTempPredio == True:
                self.flagLowTempPredio = False
                mensagem = f'" Resolved: Low Temperature on {hostname} at {data_hora} <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

        if umidade > 75:
            self.flagHighHumidityPredio = True
            mensagem = f'" Problem: High Humidity on {hostname} at {data_hora} <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagHighHumidityPredio == True:
                self.flagHighHumidityPredio = False
                mensagem = f'" Resolved: Normal Humidity on {hostname} at {data_hora} <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

        if temperatura_orvalho >= (temperatura_ar - 2):
            self.flagCriticalDewPointPredio = True
            mensagem = f'" Problem: Critical Dew Point on {hostname} at {data_hora} <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
            NTALK().envia(mensagem)
            try:
                EMAIL().enviaEmail(mensagem)
            except Exception as ex:
                self.salva_log(ex, mensagem)
                return
        else:
            if self.flagCriticalDewPointPredio == True:
                self.flagCriticalDewPointPredio = False
                mensagem = f'" Resolved: Normal Dew Point on {hostname} at {data_hora} <br>Temperature: {temperatura_ar:3.2f}º <br>Humidity: {umidade:3.2f}% <br>Dew Point: {temperatura_orvalho:3.2f}º"'
                NTALK().envia(mensagem)
                try:
                    EMAIL().enviaEmail(mensagem)
                except Exception as ex:
                    self.salva_log(ex, mensagem)
                    return

    def salva_log(self, exeption, mensagem):
        with open("/var/log/LogDataCenter.log", 'a') as logDatacenter:
            logDatacenter.write(f'{mensagem}\n')
            logDatacenter.write(f'{exeption}\n')
            logDatacenter.write("__________________________________ \n")
