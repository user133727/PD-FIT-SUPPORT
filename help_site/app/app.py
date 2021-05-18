from flask import Flask, render_template

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/doc1')
def doc1():
    title = 'Техподдержка FIT'
    return render_template('doc1.html', title=title)

@app.route('/templates/doc2')
def doc2():
    title = 'Техподдержка FIT'
    return render_template('doc2.html', title=title)

@app.route('/templates/doc3')
def doc3():
    title = 'Техподдержка FIT'
    return render_template('doc3.html', title=title)

@app.route('/templates/doc4')
def doc4():
    title = 'Техподдержка FIT'
    return render_template('doc4.html', title=title)

@app.route('/templates/doc5')
def doc5():
    title = 'Техподдержка FIT'
    return render_template('doc5.html', title=title)

@app.route('/templates/doc6')
def doc6():
    title = 'Техподдержка FIT'
    return render_template('doc6.html', title=title)

@app.route('/templates/doc7')
def doc7():
    title = 'Техподдержка FIT'
    return render_template('doc7.html', title=title)

@app.route('/templates/doc8')
def doc8():
    title = 'Техподдержка FIT'
    return render_template('doc8.html', title=title)

@app.route('/templates/doc9')
def doc9():
    title = 'Техподдержка FIT'
    return render_template('doc9.html', title=title)