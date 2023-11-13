from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from orm_models.user import User, UserAccess
