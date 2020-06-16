## From SQL to DataFrame Pandas
import pandas as pd
import pyodbc
from flask import Flask
from flask import Flask, jsonify
#import spacy
from flask import request


sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=MAFVDCBISQL03;DATABASE=MAFVCUSTDW;Trusted_Connection=yes') 

query="select B.DataAreaID as company,B.GlobalNumber,B.TransDate,D.[Item ID],D.[Subgroup Code],D.Division,D.[Category Name],D.Subgroup,Sum(B.NetAmountAED) as NetAmount,Sum(B.Qty) as Qty from FactFashionTransLine B join DimFashionStores C on B.Store = C.StoreNumber join (select DimFashionRetailProduct.Company,DimFashionRetailProduct.[Item ID],DimFashionRetailProduct.Division,DimFashionRetailProduct.[Category Name],DimFashionRetailProduct.[Subgroup Code],DimFashionRetailProduct.Subgroup from DimFashionRetailProduct group by DimFashionRetailProduct.Company, DimFashionRetailProduct.[Item ID], DimFashionRetailProduct.Division, DimFashionRetailProduct.[Category Name], DimFashionRetailProduct.[Subgroup Code], DimFashionRetailProduct.Subgroup) as D on B.ItemID = D.[Item ID] and B.DataAreaID = D.Company left join stgFashionExclusionList as E on B.GlobalNumber = E.GlobalNumber where B.GlobalNumber is not NULL and C.StoreBrandCode = 'CnB' and B.CustAccount not Like 'R%' and B.NetAmountAED > 0 and E.GlobalNumber is NULL group by B.DataAreaID, B.GlobalNumber, B.TransDate, D.[Item ID], D.[Subgroup Code], D.Division, D.[Category Name], D.Subgroup"

df = pd.read_sql(query, sql_conn)
NewDf=df.head(4)

app = Flask(__name__)

app.debug = True

#app.run(debug=False)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/jsonResrNew")
def helloNew():
    r=NewDf['GlobalNumber'][1]
    return (str(r),"succesfully inserted") 
