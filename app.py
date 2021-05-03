from selenium.webdriver import Chrome
# from tkinter import Widget, Button, Label, Frame

driver = Chrome(executable_path='./chromedriver-lin64')
driver.get("https://hometax.go.kr")
driver.execute_script('fn_topMenuOpen("menuAtag_0601200000")')


def get_move_script(tag:str=menuAtag_0000000000) -> str:
    return f"fn_topMenuOpen('{tag}')"
