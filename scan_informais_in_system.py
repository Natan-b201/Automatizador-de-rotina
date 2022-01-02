from scrapping_boxs import scrapping_folders_inf, scan_items_in_sys
from utils import element_is_load, reading_folders
from time import sleep

def scan(instance, datas, app=False):

    try:
      
        app.situation("Contando elementos ...") if app else print("Contando elementos ...")
        
        cont = 0
        for dt in datas:
            cont += len(dt['boxs'])
        ct = 1

        app.situation(f'Comecando o scrapping de {cont}') if app else print(f'Comecando o scrapping de {cont}')

        for dt in datas:
            lis_temp = list()
            for bx in dt['boxs']:

                instance.driver.get(f'{instance.get_urlBase()}{bx["link"]}')

                element_is_load(instance, "//mat-card/div/div[4]/mat-form-field[1]/div/div[1]/div/input")
           
                infos = scrapping_folders_inf(instance, bx["link"])

                lis_temp.append(infos)

                reading_folders(bx["link"],  scan_items_in_sys(instance))

                instance.driver.get(f'{instance.get_urlBase()}#/modules/home')
                sleep(2)
                app.situation(f'Processo em {((ct*100)/cont):.2f}%') if app else print(f'Processo em {((ct*100)/cont):.2f}%')
       
                ct += 1
            dt['boxs'] = lis_temp
        
        return datas
    except:
        return False