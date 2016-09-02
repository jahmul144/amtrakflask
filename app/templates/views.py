'''
Created on Aug 11, 2016

@author: ehummel
'''
from app import app
from flask import render_template
import psycopg2
import sys
from flask.globals import request

@app.route('/')
@app.route('/index')

def index():
   
    return render_template('index1.html',
                           title='Amtrak')
    
@app.route('/results', methods =['POST','GET'])
def results():

    conn = None

    try:
        
        depart = request.form['depart']
        print(type(depart))
        date = request.form['date']   
        
        conn = psycopg2.connect("dbname = 'scrape'  user = 'jah' host = 'localhost' password = 'jah14'") 
        
        cur = conn.cursor()
        
        cur.execute("SELECT trainnumber, departdate, departure, value, flexible FROM scrapeamtrakv2 WHERE departure = '{}' AND departdate = '{}';".format(depart,date))    
        rows = cur.fetchmany(100)
        
       
            
    
    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback()
            
        print ('Error{}'.format(e))    
        sys.exit(1)
    
    
    finally:
    
        if conn:
            
            # Close communication with the database
            
            cur.close()
            conn.close()    
    
    return render_template('list1.html',
                           rows=rows)  
    
