from database import engine, Base  # import your engine and Base
from models import User            # import your User model

# This will create the table in the database
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
