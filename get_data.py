from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from utils import option_select, trim, is_load_select
from utils import get_table
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Get_data:
    def __init__(self, selin, client, type=""):
        self.instance = selin
        self.instance.driver.get(f'{self.instance.get_urlBase()}#/modules/pack')

        if not self.is_load():
            return False

        if len(type):
            self.type_button = self.instance.driver.find_element_by_xpath("//mat-form-field[3]/div/div/div[@class='mat-form-field-infix']/mat-select")
            self.type_button.click()

            if is_load_select(self.instance):
                option_select(self.instance, type).click()

        self.client = self.instance.driver.find_element_by_xpath("//mat-form-field[4]/div/div/div[@class='mat-form-field-infix']/mat-select")
        self.client.click()

        if is_load_select(self.instance):
            option_select(self.instance, client).click()

        self.seach = self.instance.driver.find_element_by_xpath("//div[@class='button-seach']/button")
        self.seach.click()

        sleep(2)

        self.datas = {}
        self.table_cont = self.instance.driver.find_element_by_xpath("//div[@class='table-container']/mat-table")
        self.table_s = get_table(self.table_cont)
        self.datas = self.add_values(self.datas, self.table_s)
        self.next_button = self.instance.driver.find_element_by_xpath("//mat-paginator/div/div[2]/button[2]")

        while True:
            self.next_button.click()

            sleep(1)
            
            self.table_s = get_table(self.table_cont)
            self.datas = self.add_values(self.datas, self.table_s)
            self.next_button = self.instance.driver.find_element_by_xpath("//mat-paginator/div/div[2]/button[2]")

            if self.next_button.get_attribute("disabled"):
                break

    
    def is_load(self):
        try:
            WebDriverWait(self.instance.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, "//app-root/app-main/div/mat-sidenav-container/mat-sidenav-content/main/app-pack-list/div[2]/form"))
            )
            
            return True
        except:
            
            return False


    def get_datas(self):
        return self.datas

    def add_values(self,datas, table):
        for tab in table:
            rows = tab.find_all("mat-cell")
            datas[trim(rows[0].text)] = {
                "link": trim(rows[0].a['href']),
                "type": trim(rows[1].text),
                "subject": trim(rows[2].text),
                "client": trim(rows[3].text),
                "place": trim(rows[4].text),
                "shelf": trim(rows[5].text)
            }
        return datas








        
        
        





