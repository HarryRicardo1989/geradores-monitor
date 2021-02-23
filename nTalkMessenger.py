import os


class NTALK:
    def envia(self, message):
        try:
            os.system(
                f'curl -X POST -k -H "Accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -i "https://ntalk.grupocriar.com.br/api/sysop/mensagem/enviar" --data "secretKey=6e9cd586573e557d70d7711eb4f659c3d9068c1e&mensagem="{message}"&grupos[]=1351569867669357"')  # sysalert
            os.system(
                f'curl -X POST -k -H "Accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -i "https://ntalk.grupocriar.com.br/api/sysop/mensagem/enviar" --data "secretKey=6e9cd586573e557d70d7711eb4f659c3d9068c1e&mensagem="{message}"&grupos[]=81606837986651"')  # vigias

        except Exception as ex:
            os.system(f'echo "erro Ntalk"{ex}')


class EMAIL:
    def enviaEmail(self, message):
        try:
            os.system(f'sudo /usr/local/sbin/sysalert/getalert {message} &')
        except Exception as ex:
            os.system(f'echo "erro Email" {ex}')
