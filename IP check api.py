import http.client

#Utilizamos la API de la pagina https://ip-api.com/docs/api:json
#Variable de conexion HTTP
conn = http.client.HTTPConnection("ip-api.com", "80")
#Enviamos la IP por medio del metodo GET
conn.request("GET", "/json/191.95.56.25")

#Leemos la respuesta
res = conn.getresponse()
data = res.read()
#decodificamos la informacion en formato utf-8
print(data.decode("utf-8"))