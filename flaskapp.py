from storm_prototype import load, run
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__, template_folder='template')
model_ = load()

def format_output( label, prob ):
    output = ''
    if label == 0:
        output+='<p>It is <b>a politics</b> corpus</p>'
    else:
        output+='<p>It is <b>not a politics</b> corpus</p>'

    output+=f'<p>The probablity is about <b>{prob}</b></p>' 

    return output

@app.route('/')
def index():
    return render_template('index.html')
    #return redirect(url_for('print_info'))

@app.route('/server_info')
def server_info():
    return render_template('server_information.html')

@app.route('/prototype1', methods=['POST', 'GET'])
def get_text():
    input_ = ''
    if request.method == 'POST':
        input_ = request.form['input']
        a, b = run(input_, model_)
        
        return render_template('prototype1.html', word=format_output(a, b), text=input_)
    return render_template('prototype1.html', text='Input something here')

if __name__ == '__main__':
    app.run(debug=True)
