import json
from urllib.request import urlopen

with urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo") as response:
    data=json.load(response)
    print(json.dumps(data,indent=2))
    count=0
    total=0
    for item in data['Time Series (Daily)']:    
        count+=1
        total+=float(data['Time Series (Daily)'][item]['4. close'])
    avarage=total/count
    print("Total {}, count of '4. close' {} and avaraege is {}".format(total,count,avarage))
        