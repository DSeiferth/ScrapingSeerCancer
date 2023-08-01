from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

def scrape(id_int, out=0, del_nan=True):
    cancer_id = str(id_int)
    URL = 
"https://canques.seer.cancer.gov/cgi-bin/cq_submit?dir=seer2020&db=1&rpt=DATA&sel=1^0^0^"+cancer_id+"^23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51^1^1^6,8,13,17,20,23,25&dec=1,1,1&template=null&y=Year%20of%20diagnosis^23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51^Age%20at%20diagnosis^6,8,13,17,20,23,25"
    print(URL)
    # r = requests.get(URL)
    # Error reaching host
    # Failed to create connection to host host='canques.seer.cancer.gov', port=443. This could be from the device being 
busy or an error in name resolution. Please retry
    
    #URL = "https://www.geeksforgeeks.org/data-structures/"
    #r = requests.get(URL)
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    # Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given 
link.
    r = requests.get(url=URL, headers=headers, timeout=10)
    # Connection timeout
 
    if out:
        print(r.content)
        print()
 
    soup = BeautifulSoup(r.content, 'html.parser')
 
    if out: print(soup.prettify())
    
    bla = soup.get_text()
    s1 = bla.split('Report Results: \n',1)[1]
    s2 = s1.split('\n\nNotes:\n')[0]
    
    string = s2
    string = string.replace(u'\xa0', u' ')
    string = string.replace(u'\n', u' ')
    if out: print(string )


    year_diagnosis = []
    age_at_diagnosis = []
    incidence = []
    lines = string.split(';')
    if out: print(lines)
    for l in lines:
        a = l.split(',')
        if out: print(a)
        if len(a)==3:
            if del_nan:
                try:
                    inc = float(a[2])
                    year_diagnosis.append(int(a[0]))
                    age_at_diagnosis.append(int(a[1]))
                    incidence.append(inc)
                except:
                    inc = np.nan
            else:
                try:
                    inc = float(a[2])
                except:
                    inc = np.nan
                year_diagnosis.append(int(a[0]))
                age_at_diagnosis.append(int(a[1]))
                incidence.append(inc)

    d = {'year': year_diagnosis, 'age': age_at_diagnosis, 'incidence':incidence}
    df = pd.DataFrame(data=d)
    
    return df

mapping = pd.read_csv('MappingCancerNumber.csv')
Incidence_Site = mapping.Incidence_Site
for i in range(len(Incidence_Site)):
    print(i, Incidence_Site[i])
    try:
        df = scrape(id_int=i, del_nan=False)
        df.to_csv('Incidence_'+str(i)+'_'+Incidence_Site[i]+'.csv', index=False)
    except:
        print('ERROR with', i, Incidence_Site[i] )
        print()
