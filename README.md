# scraping from SEER for cancer survivors

### environment set-up
conda create --name scraping requests beautifulsoup4 numpy pandas matplotlib jupyter
 
conda activate scraping

### incidence
URL = 
"https://canques.seer.cancer.gov/cgi-bin/cq_submit?dir=surv2020&db=100&rpt=DATA&sel=1^"+cancer_id+"^^1^1^3,4,6,7^&dec=3,0,3&template=null&y=Year%20of%20diagnosis^0,1,2,3,4,5,6,7,8,9,10,11,12^Age%20at%20diagnosis^3,4,6,8,9^Survival%20interval^0,1,2,3,4,5,6,7,8,9,10"
where x is the cancer site id

### survival probability
URL = 
"https://canques.seer.cancer.gov/cgi-bin/cq_submit?dir=surv2020&db=100&rpt=DATA&sel=1^"+cancer_id+"^^1^1^3,4,6,7^&dec=3,0,3&template=null&y=Year%20of%20diagnosis^0,1,2,3,4,5,6,7,8,9,10,11,12^Age%20at%20diagnosis^3,4,6,8,9^Survival%20interval^0,1,2,3,4,5,6,7,8,9,10"
where x is the cancer site id

### problems
for cancer site ids > 10, the survival probability times out or has a ChunkEncodingError (still WIP)
