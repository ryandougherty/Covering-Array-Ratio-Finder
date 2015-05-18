from urllib.request import urlopen
from bs4 import BeautifulSoup

class CAElement:
    def __init__(self, N, t, k, v):
        self.N = N
        self.t = t
        self.k = k
        self.v = v
    def set_ratio(self, ratio):
        self.ratio = ratio
    def __str__(self):
        return "CA(%d; %d, %d, %d) -> %f" % (self.N, self.t, self.k, self.v, self.ratio)

CAArray = []

for v in range(2, 26):
    for t in range(2, 7):
        url = "http://www.public.asu.edu/~ccolbou/src/tabby/%d-%d-ca.html" % (t, v)
        if v == 2 and t == 2:
            response = urlopen(url)
            soup = BeautifulSoup(response)
            tables = soup.findChildren('table')
            table = tables[0]
            rows = table.findChildren('tr')
            for row in rows:
                cells = row.findChildren('td')
                elements = []
                for cell in cells:
                    value = cell.string
                    if value is not None and value != "k" and value != "N":
                        elements.append(value)
                if len(elements) == 2:
                    kParsed = int(elements[0])
                    NParsed = int(elements[1])
                    CAArray.append(CAElement(NParsed, t, kParsed, v))
        else:
            response = urlopen(url)
            soup = BeautifulSoup(response)
            tables = soup.findChildren('table')
            table = tables[0]
            rows = table.findChildren('tr')
            for row in rows:
                cells = row.findChildren('td')
                elements = []
                for cell in cells:
                    value = cell.string
                    if value is not None and value != "k" and value != "N" and value != "Source":
                        elements.append(value)
                if len(elements) == 3:
                    kParsed = int(elements[0])
                    NParsed = int(elements[1])
                    CAArray.append(CAElement(NParsed, t, kParsed, v))

for element in CAArray:
    ratio = element.N / pow(element.v, element.t)
    element.set_ratio(ratio)

CAArray.sort(key=lambda x: (x.ratio, x.N, x.v, x.t, x.k), reverse=True)

for element in CAArray:
    print(element)
