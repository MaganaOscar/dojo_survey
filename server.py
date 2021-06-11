from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def survey():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if 'radio_os' in request.form:
        os = request.form['radio_os']
    else:
        os = ''
    toppings = ', '.join(request.form.getlist('toppings'))
    return render_template('results.html', name=name, location=location, language=language, comment=comment, os=os, toppings=toppings)

if __name__ == '__main__':
    app.run(debug=True)