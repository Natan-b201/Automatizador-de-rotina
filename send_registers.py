from time import sleep
from utils import reading_json, reading_folders
from login import Login
from forms import add_files
from add_values_the_items import mapping_it
from file_monitoration import folder_is_change
from scrapping_boxs import  scan_items_in_sys

def send_rg_in_base(instance, location, app=False):

    for loc in location:
        
        dta, link = mapping_it(loc)
        names = list()
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
