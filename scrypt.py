import json, requests

ano = "2023"

rtta = requests.get('https://nolaborables.com.ar/api/v2/feriados/'+ano)
#print(type(rtta))

#rtta = json.dumps(rtta).replace("\\n","</br>")

no_laborables_payload = rtta.json()

#print(len(no_laborables_payload))
#print(no_laborables_payload)

file_name = "feriados"+ano+".json"
cont = 0
with open(file_name, 'w') as f:
    f.write("[")
    for i in no_laborables_payload:
        cont += 1
        linea = str("\n" + r"{" + f"\"mtv\":\"{i['motivo']}\",\"ms\":{i['mes']},\"d\":{i['dia']},\"nf\":\"{i['info']}\"" + r"}")
        if cont != len(no_laborables_payload):
            linea += ","
        linea = linea.replace("https://es.wikipedia.org/wiki/","")
        linea = linea.replace("ñ","&ntilde")
        linea = linea.replace("á","a")
        linea = linea.replace("é","e")
        linea = linea.replace("í","&iacute")
        linea = linea.replace("ó","o")
        linea = linea.replace("ú","u")
        linea = linea.replace("ü","u")
        f.write(linea)
    f.write("]")
    f.close()