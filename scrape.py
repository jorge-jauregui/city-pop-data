import requests 
import lxml.html as lx
import pandas as pd

url = 'https://worldpopulationreview.com/world-cities/'

page = requests.get(url) #handle for page content
doc = lx.fromstring(page.content) #doc for page content
tr_elements = doc.xpath('//tr') #parse <tr>..</tr> data
[len(T) for T in tr_elements[:20]] #check length of rows (first 10)
        

#parsing table header
tr_elements = doc.xpath('//tr')
col = [ ]
i = 0

for t in tr_elements[0]:
    i += 1
    name = t.text_content( )
    print('%d:"%s"'%(i,name)) #first row
    col.append((name,[ ]))

for j in range (1,len(tr_elements)):
    T = tr_elements[j] 
    
    if len(T) != 5:
        break
    i = 0
    
    for t in T.iterchildren( ):
        data = t.text_content( )
        if i>0:
            try:
                data = int(data)
            except:
                pass
        col[i][1].append(data)
        i += 1
        
#print([len(C) for (title, C) in col])
dict = {title:column for (title,column) in col} 
city_pop = pd.DataFrame(dict)


pd.set_option('display.max_rows', None) #none = unlimited/ display all rows
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None) 


city_pop.loc[:] #display # of rows
