# ===== load_thecode =====#
import webbrowser
import random
import time

# webbrowser,time,random module is present by default, no need to pip install
# set preferred browser as default, usually Microsoft Edge(Windows)


address = ['google.com', 'youtube.com', 'wikipedia.com', 'amazon.in', 'python.org']
for i in range(0, a):  # where a = no of tabs you want to open, i don't recommend >10
    no = random.randrange(0, len(address))
    webbrowser.open_new_tab(address[no])
    time.sleep(2)

