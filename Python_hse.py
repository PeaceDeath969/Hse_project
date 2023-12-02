from flask import Flask, render_template
import pandas as pd
import streamlit as st

df = pd.read_csv("mn.csv")
hd = df[:20].values.tolist()
col_names = df.columns
col_names = list(col_names)

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
posts = [

]
@app.route('/')
def index5():
    return render_template('meme.html', head=col_names, rows=hd)

@app.route('/meme')
def index():
    return render_template('main.html', head=col_names, rows=hd)

@app.route('/Anal')
def index2():
    return render_template('main_anal.html', head=col_names, rows=hd)

@app.route('/str')
def index3():
    return render_template('stream.html', head=col_names, rows=hd)

@app.route('/git')
def index4():
    return render_template('git.html', head=col_names, rows=hd)

app.run(debug = True)