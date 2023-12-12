from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from orm_models.user import User, UserAccess
from orm_models.capybaras import Capybara
from orm_models.election import Election, Vote, Candidate
