from io import BytesIO
import json
from urllib import response
import pycurl
import pprint

c = pycurl.Curl()
data = BytesIO()

c.setopt(c.URL, 'localhost:20010/host/storage')
c.setopt(pycurl.USERAGENT, 'Sia-Agent')
c.setopt(c.WRITEFUNCTION, data.write)

c.perform()

#convertimos a json y damos mejor formato
respuesta= json.loads(data.getvalue())
nuevaRespuesta=pprint.pprint(respuesta)

print (nuevaRespuesta)
#guardamos la respuesta como un archivo json

with open('sample.json', 'w') as outfile:
    json.dump(respuesta, outfile, ensure_ascii=False, indent=4)