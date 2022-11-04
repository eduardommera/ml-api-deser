# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:17:10 2022

@author: Eduardo
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
    
)


class model_input(BaseModel):
    d_asignatura :int
    estado :int
    e_calificacion :int
    nota :int
    genero :int
    edad :int
    financiamiento :int
    trabaja :int
    region :int
    nacionalidad :int
    nepadre :int
    nemadre :int
    nem :int
    rprocedencia :int
    recidencia :int
    aextra :int
    rreprobados :int
    hijos :int
    ecivil :int
    apoderado :int
    hermanos :int
    horario :int



#carga del modelo guardado
deser_model = pickle.load(open('modelo_desercion.sav','rb'))

@app.post('/prediccion_desercion')
def deser_pred(input_parameters :model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    asig = input_dictionary['d_asignatura']
    est = input_dictionary['estado']
    califi = input_dictionary['e_calificacion']
    grade = input_dictionary['nota']
    gend = input_dictionary['genero']
    age = input_dictionary['edad']
    finan = input_dictionary['financiamiento']
    work = input_dictionary['trabaja']
    reg = input_dictionary['region']
    nacio = input_dictionary['nacionalidad']
    nepa = input_dictionary['nepadre']
    nema = input_dictionary['nemadre']
    nemscore = input_dictionary['nem']
    rproce = input_dictionary['rprocedencia']
    reci = input_dictionary['recidencia']
    actextra = input_dictionary['aextra']
    rreprob = input_dictionary['rreprobados']
    hijo = input_dictionary['hijos']
    ecivi = input_dictionary['ecivil']
    apode = input_dictionary['apoderado']
    herma = input_dictionary['hermanos']
    hora = input_dictionary['horario']


    input_list =[asig, est, califi, grade, gend, age, finan, work, reg, nacio, nepa, nema, nemscore, 
                 rproce, reci, actextra, rreprob, hijo, ecivi, apode, herma, hora]
    
    
    prediccion = deser_model.predict([input_list])
    
    if prediccion[0] ==0:
        return 'el alumno no se titula'
    else:
        return 'el alumno se titula'
