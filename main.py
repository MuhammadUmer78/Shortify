from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pyshorteners

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shortify.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Shortify(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    shortify_url = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.url}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        shortify = Shortify(url = url, shortify_url = short_url)
        db.session.add(shortify)
        db.session.commit()

    allData = Shortify.query.all()
    return render_template('index.html', allData=allData)

@app.route('/delete/<int:sno>')
def delete(sno):
    remove = Shortify.query.filter_by(sno=sno).first()
    db.session.delete(remove)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)