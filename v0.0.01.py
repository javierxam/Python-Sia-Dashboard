from io import BytesIO
import json
import pycurl
import pprint

print("|-----SIA Dashboard for multinode farm-----|")
print("|             Author Javierxam             |")
print("|                 v0.0.01                  |")
print("|------------------------------------------|")
print("\n\n")
#make curl to the sia api
c = pycurl.Curl()
data = BytesIO()
c.setopt(c.URL, 'localhost:20010/host')
c.setopt(pycurl.USERAGENT, 'Sia-Agent')
c.setopt(c.WRITEFUNCTION, data.write)
c.perform()


#convert to json & load in to a dictionary
reply json.loads(data.getvalue())

#nested query anidada & get the remaining storage capacity in gigabytes
anidadaRespuesta=(reply.get("externalsettings"))
storageRemaining=(nestedReply.get("remainingstorage"))
storageRemaining=int(storageRemaining/1000000000)

#make a nested query & get the total storage capacity in gigabytes
storageTotal=(nestedReply.get("totalstorage"))
storageTotal=int(storageTotal/1000000000)

#used storage
storageUsed=storage-storageRemaining

stringNode1=('Available '+str(storageRemaining)+'GB | Stored '+str(storageUsed)+'GB | Total '+str(storageTotal)+'GB')

print(stringNode1)

#save the query reply as json file
with open('sample.json', 'a') as outfile:
    json.dump(stringNode1, outfile)
    outfile.write('\n')



