import streamlit as st
import sqlite3
import google.generativeai as genai

# Provide your Genai api Key
genai.configure(api_key="AIzaSyCQ03hBTujkos-cADeKyc-4ZowTTKz-lEQ")

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name Naresh_it_umapathi and has the following columns - employee_name, 
    employee_role, employee_salary \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM Naresh_it_umapathi ;
    \nExample 2 - Tell me all the employees working in Data Science role?, 
    the SQL command will be something like this SELECT * FROM Naresh_it_umapathi 
    where employee_role="Data Science"; 
    also the sql code should not have ``` and ; and : and ": in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"Naresh_it_umapathi.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
