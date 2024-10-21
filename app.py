from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite database using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fish.db'
db = SQLAlchemy(app)

# Database model for Fish
class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Fish {self.name}>"

# Route to serve the web page with the fish picker control
@app.route('/')
def index():
    # Fetch all fish from the database
    fish_list = Fish.query.all()
    return render_template('index.html', fish=fish_list)

# Route to fetch fish description using FishID
@app.route('/get_description/<int:fish_id>')
def get_description(fish_id):
    # Fetch the fish by its ID from the database
    fish = Fish.query.get(fish_id)
    if fish:
        return jsonify({'description': fish.description})
    return jsonify({'error': 'Fish not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)