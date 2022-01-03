from tkinter import *
from GlobalConfig import GlobalConfig
from login import Login
from send_registers import send_rg_in_base
from utils import convert_url, file_is_exists, create_json, reading_json
from reading_xml import update_xlsx
from file_monitoration import plan_is_change
from create_boxs import add_item
from time import sleep
from file_monitoration import folder_is_change
from upload import conf_file_upload, up_files
from SituationView import SituationView
import speedtest


# Code ..

class App:

    def start(self, application=False):
        
        self.conf = GlobalConfig()
        
        self.app = application
        
        self.app.situation("Lendo configurações ...") if self.app else print("Lendo configurações ...")

        if not self.conf.is_error():
            try:
                self.boxs = file_is_exists(convert_url("./config/boxs.json"))
            except:
                self.boxs = False
                
            try:    
                self.change, self.foldrs = folder_is_change()
            except:
                self.change = False

            if not self.boxs or plan_is_change(self.conf) or self.change:

                self.app.situation("Esperando página carregar ...") if self.app else print("Esperando página carregar ...")

                try:
                    self.lg = Login(self.conf.getUrlBase(),self.conf.getUser(),self.conf.getPassword(), self.conf.getClient(), True, self.app)
                except Exception as erro:
                    
                    self.app.situation(f'Error: {erro.__cause__}') if self.app else print(f'Error 46: {erro.__cause__}')
                    self.app.buttonExit() if self.app else print(f'Não exite app')

                else:
                    if self.lg.is_logout():
                        self.app.situation("Login feito com sucesso") if self.app else print("Login feito com sucesso")
                        
                self.app.situation("Esperando página carregar ...") if self.app else print("Esperando página carregar ...")

                try:
                    if self.lg.authentication_validation():
                        self.app.situation("Página carregada") if self.app else print("Página carregada")
                    
                    if not self.boxs:
                        self.box_change()

                    if plan_is_change(self.conf):
                        self.plan_change(self)

                    try:
                        if self.change:
                            self.send_rg()
                    except Exception as erro:
                        self.app.situation(f'Error 70: {erro} \n Error 70: {erro.__cause__}') if self.app else print(f'Error 67: {erro.__context__} \n Error 67: {erro.__annotations__}') 
                        self.lg.driver.close()
                        self.app.buttonExit() if self.app else print(f'Error: {erro.__cause__}')
                        sleep(10)
                
                except Exception as erro:
                    self.app.situation(f'Error 67: {erro.__context__}') if self.app else print(f'Error 67: {erro.__context__} \n Error 67: {erro.__annotations__}') 
                    self.lg.driver.close()
                    self.app.buttonExit() if self.app else print(f'Error: {erro.__cause__}')
                else:
                    self.lg.driver.close()
                    self.app.situation("Conexão fechada") if self.app else print("Conexão fechada")
                    sleep(2)
                    self.app.ext() if self.app else print("Conexão fechada")
            else:
                self.app.situation("Nenhuma mudança encontrada!!!") if self.app else print("Nenhuma mudança encontrada!!!")
                sleep(2)
                self.app.ext() if self.app else print("Nenhuma mudança encontrada!!!")
            

    def box_change(self):
        self.app.situation("Começando a criação dos arquivos de configuração!!") if self.app else print("Começando a criação dos arquivos de configuração!!")
        self.conf.mapping_boxs(self.lg, self.app)
        

    def plan_change(self):
        self.app.situation("Lendo arquivos de configuração ...") if self.app else print("Lendo arquivos de configuração ...") 
        dt = reading_json(convert_url('./config/boxs'))
        
        if len(dt):
            dt = dt[(len(dt))-1]
            dt['boxs'] = dt['boxs'][(len(dt['boxs']))-1]
        else:
            dt =  {}

        self.app.situation("Preparando tudo para o envio ...") if self.app else print("Preparando tudo para o envio ...")
        upl = update_xlsx(dt)
        
        self.app.situation(f'Preparando para enviar {len(upl)} items') if self.app else print(f'Preparando para enviar {len(upl)} items')
        for up in self.upl:
            
            self.app.situation(f'Inserindo a caixa: {up["index"]}') if self.app else print(f'Inserindo a caixa: {up["index"]}')
            add_item(self.lg, up, self.app)
            
                
        self.app.situation(f'Mapiando as informações ...') if self.app else print(f'Mapiando as informações ...')
        self.conf.mapping_boxs(self.lg, self.app)
        self.app.situation(f'Finalizado') if self.app else print(f'Finalizado') 

    def send_rg(self):
        self.app.situation(f'Preparando para adicionar registros no sistema ...')  if self.app else print(f'Preparando para adicionar registros no sistema ...') 
        
        try:
            send_rg_in_base(self.lg, self.foldrs, self.app)
        except Exception as erro:
            self.app.situation(f'Error 125: {erro.__context__} \n Error 125: {erro.__cause__}') if self.app else print(f'Error 67: {erro.__context__} \n Error 67: {erro.__annotations__}') 
            self.lg.driver.close()
            self.app.buttonExit() if self.app else print(f'Error: {erro.__cause__}')
            sleep(15)
        else:
            while True:
                self.app.situation(f'Configurando arquivo para upload...') if self.app else print(f'Configurando arquivo para upload...')  
                conf_file_upload()
                self.app.situation(f'Verificando velocidade da internet ... ') if self.app else print(f'Verificando velocidade da internet ... ')
                st = speedtest.Speedtest() 
                st.get_best_server()
                bytes_val = st.upload()
                Megabits = bytes_val/1048576
                MegaBytes = Megabits/8
                self.app.situation(f'Velocidade da internet {MegaBytes:.2f}... ') if self.app else print(f'Velocidade da internet {MegaBytes:.2f}... ') 
                self.app.situation(f'Começando upload..') if self.app else print(f'Começando upload..')
                if up_files(self.lg, MegaBytes, self.app):
                    break
    
init = App()
app = SituationView()
init.start(app)
app.start()

