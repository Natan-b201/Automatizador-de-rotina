from time import sleep
import utils


class Seach_Box():
    def __init__(self, selin, cod):

        self.cods = selin.driver.find_element_by_xpath("//mat-form-field[1]/div/div/div[@class='mat-form-field-infix']/input")
        self.cods.send_keys(cod)

        self.type_button = selin.driver.find_element_by_xpath("//mat-form-field[3]/div/div/div[@class='mat-form-field-infix']/mat-select")
        self.type_button.click()

        if utils.is_load_select(selin):
            utils.option_select(selin, "Caixa").click()

        self.client = selin.driver.find_element_by_xpath("//mat-form-field[4]/div/div/div[@class='mat-form-field-infix']/mat-select")
        self.client.click()
        
        if utils.is_load_select(selin):
            utils.option_select(selin, selin.getClient()).click()

        self.seach = selin.driver.find_element_by_xpath("//div[@class='button-seach']/button")
        self.seach.click()









        
        
        





