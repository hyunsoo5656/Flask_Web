from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import pymysql
from data import Articles
app = Flask(__name__)
app.debug = True

db = pymysql.connect(host='localhost',
                port=3306,
                user='root',
                passwd='1234',
                db='myflaskapp')




@ app.route('/')
def index():
# print('Success')
    return render_template('home.html', hello='Sean')

@ app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register',methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':

        # data = request.body.get('author')
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')

        if (password == re_password):
            print([name, email, password, username, re_password])
            cursor = db.cursor()

            # name = 'SONG'
            # email = '5@naver.com' 
            # username = 'SONG'
            # password = '1234'

            # sql_3=  '''
            #         INSERT INTO users(name, email , username, password) 
            #         VALUES (%s, %s, %s,%s);
            #         '''

            sql = '''
                INSERT INTO users (name, email, username, password) 
                VALUES (%s, %s, %s, %s)
            
            '''

            cursor.execute(sql, (name, email, username, password))
                        
            db.commit()
            db.close()

            # cursor = db.cursor()
            # cursor.execute('SELECT * FROM users;')
            # users = cursor.fetchall()
            
            return "register Success"





            return "POST Success"
            
        else:    
        # name = form.name.data
            return "Invalid Password"
    else:
        return "GET Success"

@ app.route('/articles', methods=['GET', 'POST'])
def articles():
    print('success')
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', articles=articles)

@ app.route('/test')
def show_image():
    return render_template('image.html')

@ app.route('/article/<int:id>')
def article(id):
    articles = Articles()[id-1]
    print(articles)
    return render_template('article.html', data=articles)
if __name__ == "__main__":
    app.run()