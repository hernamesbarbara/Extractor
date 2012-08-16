from BeautifulSoup import BeautifulSoup
import re


path = "./pdfs/test/"
f = 'bank_statement5.html'
page = open(path+f, 'rb')

soup = BeautifulSoup(page.read())
divs = soup.findAll("div")


rgx_date = "[0-9]{2}[/-][0-9]{2}$"
rgx_date2 = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec [0-9]{1,2}"
rgx_amnt = "[0-9]+?[,]?[0-9]*[.][0-9]{2}"

amnts = 0
dts = 0

dates = []
amounts = []

for div in divs:
    spans = div.findAll("span")

    for span in spans:
        span_text = span.getText('\n')
        span_text = span_text.strip()
        
        for text in span_text.split('\n'):
            if re.match(rgx_date, text):
                dates.append(text)
                dts+=1

            if re.match(rgx_date2, text):
                dates.append(text)
                dts+=1

            if re.match(rgx_amnt, text):
                amounts.append(text)          
                amnts+=1

for d, a in zip(dates, amounts):
    print d, a
