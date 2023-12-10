from flask import Flask, render_template, request
import pandas as pd

import streamlit as st

df = pd.read_csv("mn.csv")
hd = df[:20].values.tolist()
col_names = df.columns
col_names = list(col_names)
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])
df['trip_duration_timestamp'] = df.ended_at - df.started_at
df['trip_duration_minutes'] = (df.trip_duration_timestamp.dt.total_seconds()/60)

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


@app.route('/str2', methods=['POST'])
def submit():
    global df
    data = request.form['inputDate']
    print(data)
    selected_data = df[df['started_at'].dt.date == pd.to_datetime(data).date()]
    print(selected_data)
    print(df.shape)
    a = [
        "Trip_Duration",
        f"  Mean: {selected_data['trip_duration_minutes'].mean()}",
        f"  Median: {(selected_data['trip_duration_minutes'].max() + selected_data['trip_duration_minutes'].min()) / 2}",
        f"  Standart deviation: {selected_data['trip_duration_minutes'].std()}",
        ]
    return render_template('post.html', head=col_names, rows = a)

@app.route('/str')
def index3():
    return render_template('stream.html', head=col_names, rows=hd)

@app.route('/git')
def index4():
    return render_template('streamlit.html', head=col_names, rows=hd)

if __name__ == '__main__':
    app.run(debug=True)