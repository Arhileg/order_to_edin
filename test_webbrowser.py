import webbrowser
from selenium import webdriver



# https://chromedriver.storage.googleapis.com/index.html

# try:
#     browser = webdriver.Firefox()
#     print('Firefox')
#     # browser.get('url')
# except (Exception):
#     print(Exception)

# print(webbrowser.browser())
# browser = webbrowser()
WinDef = webbrowser.get(using=webbrowser.Chrome('chrome'))
print(help(WinDef))
print(dir(WinDef))
print(WinDef.__dict__)
print(WinDef.__str__())
print(WinDef.__weakref__)
# print(webbrowser.register())


# browserName