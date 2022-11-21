from io import BytesIO
import json
import pycurl
import pprint
from datetime import datetime


print("\n")
print(" /-----SIA Dashboard for multinode farm-----\ ")
print(" \             Author Javierxam             /")
print("  \________________v0.0.05_________________/")
print("\n")

nodes = 18
portRange = nodes+2000
bigNodePort=20010
storageRemaining=0
storageTotal=0
storageTotal=0
grandStorageRemaining=0
grandStorageUsed=0
grandStorageTotal=0
grandDownloadTotal=0
grandUploadTotal=0
bigNodeStorageRemaining=0
bigNodeStorageTotal=0
bigNodeStorageUsed=0

#make a iteration for each node in the farm for storage metrics
for i in range(2002, portRange):
    port=i*10
    #curl to the sia nodes api 
    c = pycurl.Curl()
    data = BytesIO()
    c.setopt(c.URL, 'localhost:'+str(port)+'/host')
    c.setopt(pycurl.USERAGENT, 'Sia-Agent')
    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()

    #convert to json and load it into a disctionary
    reply= json.loads(data.getvalue())

    #make a nested query and get the remaining storage in gigabytes
    nestedReply=(reply.get("externalsettings"))
    storageRemaining=(nestedReply.get("remainingstorage"))
    storageRemaining=int(storageRemaining/1000000000)
    
    #make a nested query and get the total storage in gigabytes
    storageTotal=(nestedReply.get("totalstorage"))
    storageTotal=int(storageTotal/1000000000)
    
    #get the used storage
    storageUsed=storageTotal-storageRemaining
    
    #summation of the storage values
    grandStorageRemaining+=storageRemaining
    grandStorageUsed+=storageUsed
    grandStorageTotal+=storageTotal


#make a iteration for each node in the farm for bandwidth metrics
for i in range(2002, portRange):
    port=i*10
    #curl to the sia nodes api 
    c = pycurl.Curl()
    data = BytesIO()
    c.setopt(c.URL, 'localhost:'+str(port)+'/host/bandwidth')
    c.setopt(pycurl.USERAGENT, 'Sia-Agent')
    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()

    #convert to json and load it into a disctionary
    reply= json.loads(data.getvalue())

    #query for get the time at nodes start
    startTime=(reply.get("starttime"))
        
    #query for get the download in gigabytes
    download=reply.get("download")
    downloadTotal=download/1000000000
    
    #query for get the upload in gigabytes
    upload=reply.get("upload")
    uploadTotal=upload/1000000000
    
    #summation of download values
    grandDownloadTotal+=downloadTotal
    grandUploadTotal+=uploadTotal

#curl for BIGNODE STORAGE

c = pycurl.Curl()
data = BytesIO()
c.setopt(c.URL, 'localhost:'+str(bigNodePort)+'/host')
c.setopt(pycurl.USERAGENT, 'Sia-Agent')
c.setopt(c.WRITEFUNCTION, data.write)
c.perform()
#convert to json and load it into a disctionary
bigNodeReply= json.loads(data.getvalue())
#make a nested query and get the remaining storage in gigabytes
nestedReply=(bigNodeReply.get("externalsettings"))
bigNodeStorageRemaining=(nestedReply.get("remainingstorage"))
bigNodeStorageRemaining=int(bigNodeStorageRemaining/1000000000)
#make a nested query and get the total storage in gigabytes
bigNodeStorageTotal=(nestedReply.get("totalstorage"))
bigNodeStorageTotal=int(bigNodeStorageTotal/1000000000)
#get the used storage
bigNodeStorageUsed=bigNodeStorageTotal-bigNodeStorageRemaining

#curl for BIGNODE BANDWIDTH
c = pycurl.Curl()
data = BytesIO()
c.setopt(c.URL, 'localhost:'+str(bigNodePort)+'/host/bandwidth')
c.setopt(pycurl.USERAGENT, 'Sia-Agent')
c.setopt(c.WRITEFUNCTION, data.write)
c.perform()
#convert to json and load it into a disctionary
bigNodeReply= json.loads(data.getvalue())
#query for get the time at nodes start
startTime=(bigNodeReply.get("starttime"))
#query for get the download in gigabytes
bigNodeDownload=bigNodeReply.get("download")
bigNodeDownloadTotal=bigNodeDownload/1000000000
#query for get the upload in gigabytes
bigNodeUpload=bigNodeReply.get("upload")
bigNodeUploadTotal=bigNodeUpload/1000000000


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dateString=("Timestamp =", dt_string)	

#Pretty print for BIG NODE
bigNodeStringStorage=('BIG NODE STATS\nSTORAGE -> Available '+str(bigNodeStorageRemaining)+'GB | Stored '+str(bigNodeStorageUsed)+'GB | Total '+ str(bigNodeStorageTotal)+'GB')
bigNodeStringBandwith=('BANDWIDTH -> Download '+ str(round(bigNodeDownloadTotal))+'GB | Uploaded '+str(round(bigNodeUploadTotal))+'GB')

#Pretty print for regular nodes
stringStorage=('REGULAR NODES STATS\nSTORAGE -> Available '+str(grandStorageRemaining)+'GB | Stored '+str(grandStorageUsed)+'GB | Total '+str(grandStorageTotal)+'GB')
stringBandwith=('BANDWITH -> Downloaded '+ str(round(grandDownloadTotal))+'GB | Uploaded '+str(round(grandUploadTotal))+'GB')

stringFarm='\n'+str(dateString)+'\n'+stringStorage+'\n'+stringBandwith+'\n'+bigNodeStringStorage+'\n'+bigNodeStringBandwith+'\n'

#print stats
print(stringFarm)

#save and write stats
myfile=open('database.txt', 'a') 
myfile.write(stringFarm)
myfile.close()
