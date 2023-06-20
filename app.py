import time

from flask import Flask, render_template, request, g

from src.codevecdb.parse_text import parse_text_and_insert
from src.codevecdb.search_text import search_question
from src.codevecdb.split.split_dispatch import split_file_to_chunks

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True


@app.before_request
def before_request():
    g.start = time.time()


@app.after_request
def after_request(response):
    diff = time.time() - g.start
    print(str(diff) + ":" + str(response))
    return response


@app.route('/code', methods=['GET', 'POST'])
def post_code():
    if request.method == 'POST':
        code_str = request.form['code']
        results = parse_text_and_insert(code_str)
        print("code success")
        return render_template('code.html', results=results)
    return render_template('code.html')


@app.route('/query', methods=['GET', 'POST'])
def query_code():
    if request.method == 'POST':
        query = request.form['query']
        results = search_question(query)
        print("query success")
        return render_template('query.html', results=[results])
    return render_template('query.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        split_file_to_chunks(file)
        print("upload success")
        return render_template('upload_file.html')
    return render_template('upload_file.html')


@app.route('/')
def hello_world():
    results = []
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run()
