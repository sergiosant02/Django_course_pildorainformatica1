from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

class Person(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

def saludo(resquest):
    p1 = Person('Sergio', 'Santiago')
    themes = ["vistas", "plantillas", "despliegues"]
    doc_external = open("video1/templates/saludo.html")
    plt = Template(doc_external.read())
    doc_external.close()
    ctx = Context({'date': datetime.datetime.now(), 'person':p1, 'themes': themes})

    res = plt.render(ctx)
    return HttpResponse(res)

def saludo2(resquest):
    p1 = Person('Sergio', 'Santiago')
    themes = ["vistas", "plantillas", "despliegues"]
    doc_external = loader.get_template("saludo.html")
    ctx = {'date': datetime.datetime.now(), 'person':p1, 'themes': themes}

    res = doc_external.render(ctx)
    return HttpResponse(res)

def saludo2(resquest):
    p1 = Person('Sergio', 'Santiago')
    themes = ["vistas", "plantillas", "despliegues"]
    doc_external = loader.get_template("saludo.html")
    ctx = {'date': datetime.datetime.now(), 'person':p1, 'themes': themes}

    res = doc_external.render(ctx)
    return HttpResponse(res)

def give_date(resquest):
    current_date = datetime.datetime.now()

    doc = """
    <html>
        <body>
            <h1>
                Fecha y hora actuales %s
            </h1>
        </body>
    </html>
    """%current_date
    return HttpResponse(doc)

def calculate_age(resquest, year):
    current_age = 18
    period = current_age + year

    doc = """
    <html>
        <body>
            <h2>
                Tendrás %s años
            </h2>
        </body>
    </html>
    """%period
    return HttpResponse(doc)
