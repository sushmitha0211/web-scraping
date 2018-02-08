import requests
from bs4 import BeautifulSoup
r= requests.get("https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off")
soup = BeautifulSoup(r.content, 'html.parser')

d = soup.findAll("div",{"class":"col _2-gKeQ"})
#print len(d)
#for item in soup.findAll("div",{"class":"col _2-gKeQ"}):
    #print item
k = d[0]

print k
price = k.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print (price[0].text)
ratings = k.findAll("div",{"class":"niH0FQ"})
#print (ratings[0].text)
filename = "sush.csv"
f = open(filename,"w")
headers="price,ratings\n"
f.write(headers)

for k in d:
    price_value =  k.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    p= price_value[0].text
    rating_value= k.findAll("div",{"class":"niH0FQ"})
    r=  rating_value[0].text

    print p
    print r


split_pricing = p.split(",")
final_pricing = split_pricing[0]
split_rating = r.split(" ")
final_rating = split_rating[0]

print(final_pricing + "," + final_rating + "\n")
f.write(final_pricing + "," + final_rating + "\n")

f.close()




print trim_price
print trim_rating











#for link in soup.find_all("article"):
    #print link
