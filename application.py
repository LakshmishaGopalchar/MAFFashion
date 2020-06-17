import pyodbc
import pandas as pd
import pyodbc
from flask import Flask
from flask import Flask, jsonify
#import spacy
from flask import request

server = 'MAFVAZEBISQL01'
database = 'TX_MAFFashionDW'
#username = 'aateam'
#password = 'uKPdyRRNEK7qQ9xS'
#driver= '{ODBC Driver 17 for SQL Server}'
drivers = [item for item in pyodbc.drivers()]
driver = drivers[-1]
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';'Trusted_Connection=yes')
cursor = cnxn.cursor()


cursor.execute("select *  from TempRetailProduct where [Brand Code] = 'LEGO'")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()

app = Flask(__name__)

app.debug = True

#app.run(debug=False)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/jsonResrNew")
def helloNew():
    
    return (("succesfully inserted")) 
