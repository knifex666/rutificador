from bs4 import BeautifulSoup
import requests

#Funcion permite extraer la tabla html y convertirla en una lista JSON
def api2_conversor(nombre):

    respuesta = requests.get('https://ws.rutificador.app/call-rutificador-v2/?opcion=nombre&nombre=%s' % nombre)

    html_data = respuesta.text

    s = BeautifulSoup(html_data, 'html.parser').table
    h, [_, *d] = [i.text for i in s.tr.find_all('th')], [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]
    json = [dict(zip(h, i)) for i in d]

    return json

def api1_conversor(nombre):

    URL = 'https://www.nombrerutyfirma.com/buscar'
    params = {'term': nombre}

    peticion = requests.post(URL, data = params)

    if peticion.status_code == 200:
        html_code = peticion.text

    s = BeautifulSoup(html_code, 'html.parser').table
    h, [_, *d] = [i.text for i in s.tr.find_all('th')], [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]
    json = [dict(zip(h, i)) for i in d]

    return json

def normalizar(s):
    remplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in remplazos:
        s = s.replace(a, b)
    s = s.upper()
    return s