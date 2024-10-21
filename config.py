from app_2 import db, Fish
# Create the database tables if they don't exist
#db.create_all()

# Add some fish data to the database
NewItem = Fish(name="Salmonj", description="Salmon iks a popular food fish.")


# Add fish data to the database session and commit
db.session.add_all([NewItem])
db.session.commit()

print("Fish data has been added to the database.")