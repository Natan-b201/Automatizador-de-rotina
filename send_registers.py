from time import sleep
from utils import reading_folders
from forms import add_files
from add_values_the_items import mapping_it
from scrapping_boxs import  scan_items_in_sys

def send_rg_in_base(instance, location, app=False):

    for loc in location:
        try:
            dta, link = mapping_it(loc)
            names = list()
        except Exception as error:
            app.situation(f'Send_regis \n {error} \nError 14: {error.__context__} \n Error 14: {error.__cause__}') if app else print(f'Error 67: {error.__context__} \n Error 67: {error.__annotations__}') 
            instance.driver.close()
            app.buttonExit() if app else print(f'Error: {error.__cause__}')
            sleep(15)
        else:
            if len(dta):
                app.situation(f'Organizando arquivos..')  if app else print(f'Organizando arquivos..')
                for data in dta:
                    names.append(data['name'])

                names.sort()
                
                instance.driver.get(f'{instance.get_urlBase()}{link}')

                sleep(2)
                for name in names:
                    for data2 in dta:
                        app.situation(f'Enviando: {name}')  if app else print(f'Enviando: {name}')
                        if data2['name'] == name:
                            add_files(instance,data2)
                
                app.situation(f'Registrando as mudanças ...')  if app else print(f'Registrando as mudanças ...') 
                reading_folders(link,  scan_items_in_sys(instance))
                sleep(5)
