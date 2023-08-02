import numpy as np
import pandas as pd

mapping = pd.read_csv('MappingCancerNumber.csv')

### copy and paste SEER data that does not load ###

def scrape_by_hand(name):
    with open('scrape_by_hand/'+name+'.txt') as f:
        lines = f.readlines()
    read = False

    year_diagnosis = []
    age_at_diagnosis = []
    survival_interval = []
    survival_prob = []

    for line in lines:
        if 'Report Results:' in line:
            read = True
        if 'Notes:' in line:
            read = False
        if read:
            if 'Report Results:' not in line:
                s = line.split(',')
                #print(s)
                try:
                    prob = float(s[3].split(';')[0])
                except:
                    prob = np.nan
                year_diagnosis.append(int(s[0]))
                age_at_diagnosis.append(int(s[1]))
                survival_interval.append(int(s[2]))
                survival_prob.append(prob)

    d = {'year': year_diagnosis, 'age': age_at_diagnosis, 
             'surv_interval':survival_interval, 'surv_prob':survival_prob}
    df = pd.DataFrame(data=d)
    return df

Survival_Site = mapping.Survival_Site.dropna()
for i in range(len(Survival_Site)):
    print(i, Survival_Site[i])
    try:
        df = scrape_by_hand(name=str(i)+'_'+Survival_Site[i])
        df.to_csv('Survival_'+str(i)+'_'+Survival_Site[i]+'.csv', index=False)
    except:
        print('ERROR with', i, Survival_Site[i] )
        print()
