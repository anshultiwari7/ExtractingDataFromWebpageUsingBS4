import requests
import bs4

def get_petrolpump(url):
      html = requests.get(url)
      soup=bs4.BeautifulSoup(html.text,'html.parser')
      
      data = soup.select('table.new tr td')

      name = ""
      totaldata = 0
      for i in data:
        name = name + str(i.text.encode('ascii','ignore'))
        name = name + '$'
        totaldata = totaldata + 1
    
      name = name.replace('\n','') 
      name = name.replace('\n','')
      name = name.replace('\b','')
      name = name.replace('\t','')
      name = name.replace('\r','')

      petrol = name.split('$')
      if totaldata>5:
       petrol.pop(0)
       petrol.pop(0)
       petrol.pop(0)
       petrol.pop(0)
       petrol.pop(0)
       totaldata = totaldata - 5
      else:
       totaldata = 0
      for i in range(totaldata):
        if i%5 == 0:
         print ('{\"State\": \"'+petrol[i]+'\",')
        if i%5 == 1:
         print ('\"City\": \"'+petrol[i]+'\",')
        if i%5 == 2:
         print ('\"Name\": \"'+petrol[i]+'\",')
        if i%5 == 3:
         print ('\"Address\": \"'+petrol[i]+'\",')
        if i%5 == 4:
         print ('\"CompanyName\": \"'+petrol[i]+'\"')
         print ('},')
      return totaldata

def get_city(url):
      html = requests.get(url)
      soup=bs4.BeautifulSoup(html.text,'html.parser')
      
      data = soup.select('td.table_blk a')

      name = ""
      totaldata = 0
      for i in data:
        name = name + str(i.text.encode('ascii','ignore'))
        name = name + '$'
        totaldata = totaldata + 1
    
      name = name.replace('\n','') 
      name = name.replace('\n','')
      name = name.replace('\b','')
      name = name.replace('\t','')
      name = name.replace('\r','')
      name = name.replace('Where is ','')
      name = name.lower()

      city = name.split('$')

#      for i in range(totaldata):
 #       print city[i]
      return city

def get_state(url):
      html = requests.get(url)
      soup=bs4.BeautifulSoup(html.text,'html.parser')
      
      data = soup.select('table.tableizer-table tr td a')

      name = ""
      totaldata = 0
      for i in data:
        name = name + str(i.text.encode('ascii','ignore'))
        name = name + '$'
        totaldata = totaldata + 1
    
      name = name.replace('\n','') 
      name = name.replace('\n','')
      name = name.replace('\b','')
      name = name.replace('\t','')
      name = name.replace('\r','')
      name = name.replace('Where is ','')
      name = name.lower()

      state = name.split('$')

#      for i in range(totaldata):
 #       print city[i]
      return state

a = 0
c = 0
state = get_state('http://www.mapsofindia.com/states/')
#state.remove('puducherry')
#state.remove('lakshadweep')
#state.remove('daman and diu')
#state.remove('dadar and nagar haveli')
#state.remove('andaman and nicobarislands')
#state.remove('')
a = a+1
for i in state:
   state_base_url = 'http://www.mapsofindia.com/maps/'
   state_url = state_base_url + i + '/' + i +'location.htm'
   city = get_city(state_url)
   for i in city:
     base_url = 'http://automobiles.mapsofindia.com/petrol-stations/'
     url = base_url + i + '.htm'
     c = c + get_petrolpump(url) 

print (c)
