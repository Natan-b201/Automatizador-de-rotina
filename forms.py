from time import sleep

def add_files(instance,data):
    if len(data['name']):
        name_input = instance.driver.find_element_by_xpath("//app-pack-file-itens/mat-card/div/div[1]/mat-form-field[1]/div/div[1]/div/input")
        name_input.clear()
        name_input.send_keys(data['name'])

        subject_input = instance.driver.find_element_by_xpath("//app-pack-file-itens/mat-card/div/div[1]/mat-form-field[2]/div/div[1]/div/input")
        subject_input.clear()
        subject_input.send_keys(data['subject'])

        describe_input = instance.driver.find_element_by_xpath("//app-pack-file-itens/mat-card/div/div[1]/mat-form-field[3]/div/div[1]/div/input")
        describe_input.clear()
        describe_input.send_keys(data['describe'])

        if len(name_input.get_attribute("value")):
            button = instance.driver.find_element_by_xpath("//app-pack-file-itens/mat-card/div/div[1]/div/button")
            button.click()
            sleep(1)
