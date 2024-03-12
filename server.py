from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://username:password@localhost/db_name')
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    data = session.execute('SELECT title, image FROM ads LIMIT 500')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
