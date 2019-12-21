from flask import Flask
from flask import request, render_template
import sys
sys.path.insert(0, 'C:/Users/Garry/Desktop/EzComm Web Project/templates/')
from templates import texttosp
from templates import texttosign
from templates import set_hand
from templates import reco
from templates import reco2
app = Flask(__name__, static_url_path='/static')
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    return (render_template('softproj main page.html'))

@app.route('/foo1', methods=['GET', 'POST'])
def foo1():
    return (render_template('softproj product page.html'))

@app.route('/foo', methods=['GET', 'POST'])
def foo():
    return (render_template('softproj main page.html'))

@app.route('/foo2', methods=['POST'])
def foo2():
    text = request.form['ttosp']
    texttosp.exec2(text)
    return (render_template('softproj product page.html'))

@app.route('/foo3', methods=['POST'])
def foo3():
    text = request.form['ttosign']
    texttosign.exec3(text) 
    return (render_template('softproj product page.html'))

@app.route('/foo4', methods=['POST'])
def foo4():
    text = request.form['sptosign']
    texttosign.exec3(text) 
    return (render_template('softproj product page.html'))

@app.route('/foo5', methods=['GET', 'POST'])
def foo5():
    return (render_template('softproj profile page.html'))

@app.route('/foo6/', methods=['GET', 'POST'])
def foo6():
    set_hand.exec()
    return (render_template('softproj project page.html'))

@app.route('/foo7', methods=['GET','POST'])
def foo7():
    reco2.exec()
    return (render_template('softproj project page.html'))

@app.route('/foo8', methods=['GET','POST'])
def foo8():
    reco.exec()
    return (render_template('softproj project page.html'))

@app.route('/foo9', methods=['GET', 'POST'])
def foo9():
    return (render_template('softproj project page.html'))

@app.route('/foo10', methods=['GET', 'POST'])
def foo10():
    return (render_template('softproj about.html')) 
if __name__ == '__main__':
    app.run(debug=True,port=8080)

