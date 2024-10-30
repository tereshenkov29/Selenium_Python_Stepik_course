import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Операция "Минное поле"
Привет, будущие автоматизаторы! Сегодня у нас не просто задача, а настоящий тайм-триал, испытание на скорость и 
точность! Мы переносимся в мир, где каждое неверное движение может стать последним... ну, или по крайней мере, 
приведёт к неудачному выполнению задания. Задача симулирует реальную рабочую ситуацию, в которой на скорость 
выполнения операций поставлен жесткий лимит.   
Задачи
Стартовая Позиция: Используя Selenium, откройте заданный веб-сайт. Убедитесь, что ваша машина готова к операции.
Секунды на Счетчике: У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те, 
которые доступны для редактирования. 
Проверка: Нажмите на кнопку "Проверить" на странице.
Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.
Для проверки доступности текстового поля, используйте проверку атрибута disabled у соответствующих текстовых полей:
.get_attribute('disabled')"""

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/2/1.html')

    text_fields = driver.find_elements(By.XPATH, "//*[@id=\"textfields-container\"]/input")

    for field in text_fields:
        if field.get_attribute('disabled'):
            continue
        else:
            field.clear()

    submit_button = driver.find_element(By.ID, "checkButton")
    submit_button.click()

    alert = driver.switch_to.alert.text
    print(alert)
