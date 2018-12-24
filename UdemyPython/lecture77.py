# for i in range(1,10):
#     print(1,2,3,4)
#     print(1,2,3,4,sep = ';')

import webbrowser

my_url = 'https://www.python.org/'
# webbrowser.open(my_url,new = 1)

firefox = webbrowser.get(using='firefox')
firefox.open_new(my_url)