from io import BytesIO
import json
import pycurl
import pprint

print("|-----SIA Dashboard for multinode farm-----|")
print("|             Author Javierxam             |")
print("|                 v0.0.02                  |")
print("|------------------------------------------|")
print("\n\n")

nodes = 18
portRange = nodes+2000
storageRemaining=0
storageTotal=0
storageTotal=0

#make a iteration for each node in the farm    
for i in range(2001, rango):
    puerto=i*10
    #curl to the sia nodes api 
    c = pycurl.Curl()
    data = BytesIO()
    c.setopt(c.URL, 'localhost:'+str(puerto)+'/host')
    c.setopt(pycurl.USERAGENT, 'Sia-Agent')
    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()

    #convert to json and load it into a disctionary
    reply= json.loads(data.getvalue())

    #make a nested query and get the remaining storage in gigabytes
    nestedReply=(reply.get("externalsettings"))
    storageRemining=(nestedReply.get("remainingstorage"))
    storageRemaining=int(storageRemaining/1000000000)
    
    #make a nested query and get the total storage in gigabytes
    storageTotal=(nestedReply.get("totalstorage"))
    storageTotal=int(storageTotal/1000000000)
    
    #get the used storage
    storageUsed=storageTotal-storageRemaining
    
    #summation of the storage values
    storageRemaining+=storageRemaining
    storageTotal+=storageUsed
    storageTotal+=storageTotal

    

#format and save the values in a json file
stringFarm=('TOTALS -> Available '+str(storageRemaining)+'GB | Stored '+str(storageTotal)+'GB | Total '+str(storageTotal)+'GB\n')
print(stringFarm)
myfile=open('database.txt', 'w') 
myfile.write(stringFarm)
myfile.close()
