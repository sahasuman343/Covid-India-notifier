# do all the imports
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading


# get html data of website
def get_html_data(url):
    data = requests.get(url)
    return data


# parsing html and extracting data
def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div1 = bs.find("div", class_="site-stats-count").find("li",class_="bg-blue").find("strong",class_=None).get_text()
    info_div1_text = bs.find("div", class_="site-stats-count").find("li",class_="bg-blue").find("span",class_=None).get_text()

    info_div2 = bs.find("div", class_="site-stats-count").find("li",class_="bg-green").find("strong",class_=None).get_text()
    info_div2_text = bs.find("div", class_="site-stats-count").find("li",class_="bg-green").find("span",class_="mob-hide").get_text()

    info_div3 = bs.find("div", class_="site-stats-count").find("li",class_="bg-red").find("strong",class_=None).get_text()
    info_div3_text = bs.find("div", class_="site-stats-count").find("li",class_="bg-red").find("span",class_=None).get_text()

   
    all_details = info_div1_text + " : " + info_div1+"\n"+info_div2_text + " : " + info_div2 + "\n" +info_div3_text + " : " +info_div3
   # print(all_details)
    return(all_details)
    
get_corona_detail_of_india()  




# function use to  reload the data from website
def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing..")
    mainLabel['text'] = newdata


# function for notifying...
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=1800,
            app_icon='icon.ico'
        )
        time.sleep(900)

'''
# creating gui:
root = tk.Tk()
root.geometry("900x800")
root.iconbitmap("icon.ico")
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background='white')
f = ("poppins", 25, "bold")
banner = tk.PhotoImage(file="index.png")
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f, bg='white')
mainLabel.pack()

reBtn = tk.Button(root, text="REFRESH", font=f, relief='solid', command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()'''
notify_me()