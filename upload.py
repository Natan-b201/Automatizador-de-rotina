from login import Login
from time import sleep
import os
from os import walk
from scrapping_boxs import scan_items_in_sys
from utils import element_is_load, reading_folders

from file_monitoration import folder_is_change
from utils import  create_json, reading_json, file_is_exists, convert_url


# input_file = log.driver.find_element_by_xpath(f'//mat-table/mat-row[{row_temp}]/mat-cell[5]/label/input')
#input_file.send_keys(location)
# location = f'{os.getcwd()}/G.01.00.00004/G.01.00.00004.1/{fil["file_name"]}'

# Verifica se teve mundaça

def conf_file_upload():

    change, location = folder_is_change()

    upes = reading_json(convert_url('./config/boxs'))

    list_t = list()

    for uep in upes:

        for local in location:

            if uep['index'] == local['index']:

                for bx in uep['boxs']:

                    if bx['index'] == local['box']:

                        list_t.append({
                            "index": uep['index'],
                            "index_box": bx['index'],
                            "id": (bx['link'].split("/")[(len(bx['link'].split("/"))-1)]),
                            "link": bx['link']
                        })


    create_json(convert_url('./config/upload'), list_t)





def up_files(instance):
    upload = reading_json(convert_url('./config/upload'))

    for upl in upload:
    
        control_items = reading_json(convert_url(f'./config/folders/{upl["id"]}'))

        instance.driver.get(f'{instance.get_urlBase()}{upl["link"]}')
        element_is_load(instance,"//mat-card/div/div[3]/mat-form-field[1]/div/div[1]/div/input", time_in=60)
        element_is_load(instance,"//mat-table/mat-row[1]/mat-cell[5]/label/input", time_in=60)

        row = 1  
        
        for control in control_items[upl["link"]]:
            
            if control['upload'] == "none":
                location = convert_url(f'{os.getcwd()}/{upl["index"]}/{upl["index_box"]}/{control["name"]}.pdf')
                if not file_is_exists(location):
                    location = convert_url(f'{os.getcwd()}/{upl["index"]}/{upl["index_box"]}/{control["name"]}.PDF')

                

                input_file = instance.driver.find_element_by_xpath(f'//mat-table/mat-row[{row}]/mat-cell[5]/label/input')

                input_file.send_keys(location)

            row +=1  

        instance.driver.get(f'{instance.get_urlBase()}#/modules/home')
        sleep(1)
        instance.driver.get(f'{instance.get_urlBase()}{upl["link"]}')
        element_is_load(instance,"//mat-card/div/div[3]/mat-form-field[1]/div/div[1]/div/input", time_in=7200)
        sleep(3)
        dt = scan_items_in_sys(instance)
        
        reading_folders(upl["link"], dt )
        instance.driver.get(f'{instance.get_urlBase()}#/modules/home')
        sleep(5)  