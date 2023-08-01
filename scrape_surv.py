from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

mapping = pd.read_csv('MappingCancerNumber.csv')

def scrape_surv_prob(id_int, out=0, timeout=None, del_nan=True):    
    '''
    timpout None wait forever
    timeout tuple: connect and read timeouts
    timeout single float: both connect and read timeouts
    '''
    cancer_id = str(id_int)
    URL = 
"https://canques.seer.cancer.gov/cgi-bin/cq_submit?dir=surv2020&db=100&rpt=DATA&sel=1^"+cancer_id+"^^1^1^3,4,6,7^&dec=3,0,3&template=null&y=Year%20of%20diagnosis^0,1,2,3,4,5,6,7,8,9,10,11,12^Age%20at%20diagnosis^3,4,6,8,9^Survival%20interval^0,1,2,3,4,5,6,7,8,9,10"
    print(URL)
    # r = requests.get(URL)
    # Error reaching host
    # Failed to create connection to host host='canques.seer.cancer.gov', port=443. This could be from the device being 
busy or an error in name resolution. Please retry
    
    #URL = "https://www.geeksforgeeks.org/data-structures/"
    #r = requests.get(URL)
    #headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                'AppleWebKit/537.11 (KHTML, like Gecko) '
                'Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'
    }
    
    
#https://stackoverflow.com/questions/70189517/requests-chunkedencodingerror-with-requests-get-but-not-when-using-postman
    r = requests.get(url=URL, headers=headers, timeout=timeout, verify=True, stream=True)
    print('status_code',r.status_code)
    print('r.content', type(r.content))
 
    if out: 
        print(r.content)
        print()
 
    soup = BeautifulSoup(r.content, 'html.parser')
 
    if out: 
        print(soup.prettify())
    
    bla = soup.get_text()
    s1 = bla.split('Report Results: \n',1)[1]
    s2 = s1.split('\n\nNotes:\n')[0]
    
    string = s2
    string = string.replace(u'\xa0', u' ')
    string = string.replace(u'\n', u' ')
    if out: print(string )

    year_diagnosis = []
    age_at_diagnosis = []
    survival_interval = []
    survival_prob = []
    lines = string.split(';')
    if out: print(lines)
    for l in lines:
        a = l.split(',')
        if out: print(a)
        if len(a)==4:
            if del_nan:
                try:
                    prob = float(a[3])
                    year_diagnosis.append(int(a[0]))
                    age_at_diagnosis.append(int(a[1]))
                    survival_interval.append(int(a[2]))
                    survival_prob.append(prob)
                except:
                    prob = np.nan
            else:
                try:
                    prob = float(a[3])
                except:
                    prob = np.nan
                year_diagnosis.append(int(a[0]))
                age_at_diagnosis.append(int(a[1]))
                survival_interval.append(int(a[2]))
                survival_prob.append(prob)
    d = {'year': year_diagnosis, 'age': age_at_diagnosis, 
         'surv_interval':survival_interval, 'surv_prob':survival_prob}
    df = pd.DataFrame(data=d)
    return df

Survival_Site = mapping.Survival_Site.dropna()
for i in range(len(Survival_Site)):
    print(i, Survival_Site[i])
    try:
        df = scrape_surv_prob(id_int=i, out=0, timeout=(0.1, 10), del_nan=False)
        df.to_csv('Survival_'+str(i)+'_'+Survival_Site[i]+'.csv', index=False)
    except:
        print('ERROR with', i, Survival_Site[i] )
        print()
