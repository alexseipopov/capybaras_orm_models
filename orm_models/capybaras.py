from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Boolean
from sqlalchemy.orm import relationship

from . import Base


class Capybara(Base):
    __tablename__ = 'capybara'

    id = Column(Integer, primary_key=True)
    school_user_id = Column(String, nullable=False)
    login = Column(String, nullable=False)
    is_subscribe = Column(Boolean, default=True)
    telegram_id = Column(Integer)
    key = Column(String, nullable=False)
    is_student = Column(Boolean, default=True)

