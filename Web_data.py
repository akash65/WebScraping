
# coding: utf-8

# In[156]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://housing.com/in/buy/search?f=eyJiYXNlIjpbeyJ0eXBlIjoiUE9MWSIsInV1aWQiOiJjOTZkZWFiZGU2NzQzZjZmNjc3YyIsImxhYmVsIjoiSyBSIFB1cmFtIn1dLCJub25CYXNlQ291bnQiOjAsInYiOjIsInMiOiJkIn0%3D")
value = r.content

soup = BeautifulSoup(value, "html.parser")

all = soup.find_all("div", {"class":"list-item-container"})

all[0].find("span", {"class":"lst-price"}).text

base_url = "https://housing.com/in/buy/search?s=number&f=eyJiYXNlIjpbeyJ0eXBlIjoiUE9MWSIsInV1aWQiOiJjOTZkZWFiZGU2NzQzZjZmNjc3YyIsImxhYmVsIjoiSyBSIFB1cmFtIn1dLCJub25CYXNlQ291bnQiOjAsInYiOjIsInMiOiJkIn0%3D"
for number in range(0,100): 
    print(base_url+str(number))
    r = requests.get(base_url+str(number))
    value = r.content
    soup = BeautifulSoup(value, "html.parser")
    all = soup.find_all("div", {"class":"list-item-container"})
    #print(all)
    l=[]
    for item in all:
        d={}
        try:
            #print(item.find("div", {"class":"lst-prjct-by text-ellipsis"}).text.replace("by","").replace("Search",""))
            d["Builders"]=item.find("div", {"class":"lst-prjct-by text-ellipsis"}).text.replace("by","").replace("Search","")
        except:
            d["Builders"]=None
        try:
            #print(item.find("div", {"class":"lst-loct text-ellipsis"}).text)
            d["Locality"]=item.find("div", {"class":"lst-loct text-ellipsis"}).text
        except:
            d["Locality"]=None
        try:
            #print(item.find("span",{"class":"lst-price"}).text)
            d["LPrice"]=item.find("span",{"class":"lst-price"}).text
        except:
            d["LPrice"]=None
        try:
            #print(item.find("div", {"class":"stub emiWidget"}).text.replace("EMI starts at",""))
            d["Monthly_Installment"]=item.find("div", {"class":"stub emiWidget"}).text.replace("EMI starts at","")
        except:
            d["Monthly_Installment"]=None
        try:
            #print(item.find("div", {"class":"lst-sub-value lst-config-title text-ellipsis"}).text.replace("BHK Apartment",""))
            d["Villa_BHK"]=item.find("div", {"class":"lst-sub-value lst-config-title text-ellipsis"}).text.replace("BHK Apartment","")
        except:
            d["Villa_BHK"]=None
        try:
            #print(item.find("div", {"class":"lst-sub-value text-ellipsis"}).text.replace("per sqft.",""))
            d["sqft"]=item.find("div", {"class":"lst-sub-value text-ellipsis"}).text.replace("per sqft.","")
        except:
            d["sqft"]=None

        print("")
        l.append(d)


    import pandas
    df = pandas.DataFrame(l)

    df.to_csv("ouptu.csv")

