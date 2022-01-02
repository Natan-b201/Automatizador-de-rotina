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

conf = GlobalConfig()

if not conf.is_error():
    root = Tk()
    app = SituationView(root)

    try:
        boxs = file_is_exists(convert_url("./config/boxs.json"))
    except:
        boxs = False

    try:    
        change, foldrs = folder_is_change()
    except:
        change = False

    if not boxs or plan_is_change(conf) or change:

        app.situation("Esperando página carregar ...")
        try:
            lg = Login(conf.getUrlBase(),conf.getUser(),conf.getPassword(), conf.getClient(), True, app)

            if lg.is_logout():
                app.situation("Login feito com sucesso")
            
            app.situation("Esperando página carregar ...")

            if lg.authentication_validation():
                app.situation("Página carregada")

            if not boxs:
                app.situation("Começando a criação dos arquivos de configuração!!")
                conf.mapping_boxs(lg, app)


            if plan_is_change(conf):
                app.situation("Lendo arquivos de configuração ...")
                dt = reading_json(convert_url('./config/boxs'))
                
                if len(dt):
                    dt = dt[(len(dt))-1]
                    dt['boxs'] = dt['boxs'][(len(dt['boxs']))-1]
                else:
                    dt =  {}

                app.situation("Preparando tudo para o envio ...")
                upl = update_xlsx(dt)
                
                app.situation(f'Preparando para enviar {len(upl)} items')
                for up in upl:
                    
                    app.situation(f'Inserindo a caixa: {up["index"]}')
                    add_item(lg, up, app)
                    
                        
                app.situation(f'Mapiando as informações ...')    
                conf.mapping_boxs(lg, app)
                app.situation(f'Finalizado')   



            if change:
                app.situation(f'Preparando para adicionar registros no sistema ...')   
                send_rg_in_base(lg, foldrs, app)
                while True:
                    app.situation(f'Configurando arquivo para upload...')   
                    conf_file_upload()
                    app.situation(f'Verificando velocidade da internet ... ')
                    st = speedtest.Speedtest() 
                    st.get_best_server()
                    bytes_val = st.upload()
                    Megabits = bytes_val/1048576
                    MegaBytes = Megabits/8
                    app.situation(f'Velocidade da internet {MegaBytes:.2f}... ')
                    app.situation(f'Começando upload..')   
                    if up_files(lg, MegaBytes, app):
                        break

            lg.driver.close()
            app.situation("Conexão fechada")
            sleep(2)
            app.ext()
        except Exception as error:
            try:
                lg.driver.close()
            except:
                pass
            finally:
                
                app.situation(f'Error: {error.__cause__} \n Error: {error.__context__} \nOcorreu um erro que não soube lidar, \nprocure o desenvolvedor para encontar o problema')
                app.buttonExit()

    else:
        app.situation("Nenhuma mudança encontrada!!!")
        sleep(2)
        app.ext()

    root.mainloop()