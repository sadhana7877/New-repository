from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace "admin" and "simplepass" with your PostgreSQL username and password if different
DATABASE_URL = "postgresql://admin:simplepass@localhost:5432/audit_db"

# This creates the connection to the database
engine = create_engine(DATABASE_URL)

# This creates a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the base class for all our database models
Base = declarative_base()
