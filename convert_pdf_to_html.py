from utils import formatpdfs
from BeautifulSoup import BeautifulSoup
import re, os, fnmatch



rgx_date = "([0-9]{1}|1[0-2])[/-][1-3]?[0-9]$"
rgx_date2 = "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{1,2}$"
rgx_amnt = "[0-9]+?[,]?[0-9]+[.][0-9]{2}"
fdir = "./pdfs"

formatpdfs.split_pdf(fdir)


for root, dirnames, filenames in os.walk(fdir):
    print "#"*80
    print "#"*80
    print "#"*80
    print root

    for filename in fnmatch.filter(filenames, '*.html'):
        print "*"*80
        print filename
        page = open(root+"/"+filename, 'rb')

        soup = BeautifulSoup(page.read())
        divs = soup.findAll("div")
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
            print d,"|", a
