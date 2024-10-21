from flask import Flask, render_template, request
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
@app.route('/', methods = ["GET","POST"])
def index():
    # Fetch all fish from the database
    fish_list = Fish.query.all()

    fish_description = None

    if request.method == 'POST':
        selected_fish_id = request.form.get('fishPicker')
        if selected_fish_id:
            selected_fish = Fish.query.get(int(selected_fish_id))

            if selected_fish:
                fish_description = selected_fish.description
        if selected_fish_id == 1:
            print()
                        
    return render_template('index.html', fish=fish_list, description=fish_description)
@app.route('/AddFish', methods=["GET", "POST"])
def AddFish():
    if request.method == 'POST':
        fish_name = request.form.get('fish_name')  # Get the fish name
        fish_description = request.form.get('fish_description')  # Get the fish description
        print(f"Fish Name: {fish_name}")  # Separate data handling for fish name
        print(f"Fish Description: {fish_description}")  # Separate data handling for fish description
        
        if fish_name and fish_description:  # Check if both fields are filled
            # Create a new Fish object
            new_fish = Fish(name=fish_name, description=fish_description)
            db.session.add(new_fish)  # Add the new fish object to the session
            db.session.commit()  # Commit the session to save changes
            print("New item added to the database.")
            return render_template('AddFish.html', success=True)  # Render success response

    return render_template('AddFish.html')  # Render the form for adding fish

    


if __name__ == '__main__':
    app.run(debug=True)