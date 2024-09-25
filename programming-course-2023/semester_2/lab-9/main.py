from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visited_cities.db'
db = SQLAlchemy(app)


class VisitedCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.String(100), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'clear' in request.form:
            db.session.query(VisitedCity).delete()
            db.session.commit()
        else:
            town = request.form['town']
            # Конвертация даты в нужный формат чтобы сохранить в базе данных
            visit_date = datetime.strptime(
                request.form['visit_date'], '%Y-%m-%d').date()
            new_city = VisitedCity(town=town, visit_date=visit_date)
            db.session.add(new_city)
            db.session.commit()
        return redirect(url_for('index'))

    cities = VisitedCity.query.order_by(VisitedCity.visit_date.desc()).all()
    return render_template('index.html', cities=cities)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
