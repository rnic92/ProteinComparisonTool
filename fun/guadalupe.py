import html2text
from urllib.request import urlopen
from bs4 import BeautifulSoup
outfile = open("results.txt", "w")



url = "https://www.ncbi.nlm.nih.gov/nuccore/CP017581"
page = urlopen(url).read()
html = page.decode("utf-8")
outfile.write(html)

"""

html1 = urllib.request.urlopen("https://www.ncbi.nlm.nih.gov/nuccore/CP031649.1").read()

soup = BeautifulSoup(html1, 'html.parser')
searchtag = "leucine-responsive transcriptional regulator"
outfile.write("HEADER\n")
outfile.write(str(soup))
if "complement" in soup:
    print("hello")



# print(type(soup))
"""
outfile.close()
