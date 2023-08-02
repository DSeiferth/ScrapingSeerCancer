import numpy as np
import pandas as pd

mapping = pd.read_csv('MappingCancerNumber.csv')

### incidence ###
frames = []
for i in range(len(mapping.Incidence_ID)):
    print(i, mapping.Incidence_Site[i])
    try:
        df = pd.read_csv('Incidence_'+str(i)+'_'+mapping.Incidence_Site[i]+'.csv')
        df['cancer_id'] = (np.ones(len(df))*i).astype(int)
        frames.append(df)
    except:
        print('ERROR: could not find', 'Incidence_'+str(i)+'_'+mapping.Incidence_Site[i]+'.csv')

result = pd.concat(frames)
result.to_csv('Incidence_all_cancer_ids.csv', index=False)

###  survival probability ###
frames = []
for i in range(len(mapping.Survival_Site.dropna())):
    print(i, mapping.Survival_Site[i])
    if i>9:
        break
    try:
        df = pd.read_csv('Survival_'+str(i)+'_'+mapping.Survival_Site[i]+'.csv')
        df['cancer_id'] = (np.ones(len(df))*i).astype(int)
        frames.append(df)
    except:
        print('ERROR: could not find', 'Incidence_'+str(i)+'_'+mapping.Survival_Site[i]+'.csv')
result = pd.concat(frames)
result.to_csv('Survival_all_cancer_ids.csv', index=False)`
