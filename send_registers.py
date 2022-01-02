from time import sleep
from utils import reading_json, reading_folders
from login import Login
from forms import add_files
from add_values_the_items import mapping_it
from file_monitoration import folder_is_change
from scrapping_boxs import  scan_items_in_sys

def send_rg_in_base(instance, location):

    for loc in location:
        
        dta, link = mapping_it(loc)
        names = list()
        if len(dta):
            for data in dta:
                names.append(data['name'])

            names.sort()
           
            instance.driver.get(f'{instance.get_urlBase()}{link}')

            sleep(2)
            for name in names:
                for data2 in dta:
                    if data2['name'] == name:
                        add_files(instance,data2)
            
            reading_folders(link,  scan_items_in_sys(instance))
            sleep(5)
