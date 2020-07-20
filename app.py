from flask import Flask ,render_template

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    #return 'Hello World!!'

    print("Success")
    #return "test"
    return render_template('home.html', hello="Garykim")

@app.route('/about')
def aubout():
    #return 'Hello World!!'

    print("Success")
    #return "test"
    return render_template('about.html', hello="Garykim")

@app.route('/articles')

def articles():
    #return 'Hello World!!'

    print("Success")
    #return "test"
    return render_template('articles.html', hello="Garykim")



if __name__== '__main__':
    # app.run(host= '0.0.0.0', port = '8080')
    app.run()
















