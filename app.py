from flask import Flask ,render_template
from data import Articles



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

@app.route('/articles', methods =['GET', 'POST'])

def articles():
    #return 'Hello World!!'

    print("Success")
    #return "test"
    articles = Articles()
    print(articles)
    return render_template('articles.html', articles=articles)


@app.route('/test')
def show_image():
    return render_template('image.html')

@app.route('/article/<int:id>')
def article(id):
    print(type(id))
    articles = Articles()
    return render_template('article.html', data = [articles, id])



if __name__== '__main__':
    # app.run(host= '0.0.0.0', port = '8080')
    app.run()
