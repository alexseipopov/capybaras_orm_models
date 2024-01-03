from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, CheckConstraint
from sqlalchemy.orm import relationship

from . import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    school_user_id = Column(String)
    capy_uuid = Column(String, nullable=False)
    user_access = relationship("UserAccess", backref="user")
    user_avatar = relationship("UserAvatar", backref="user")


class UserAccess(Base):
    __tablename__ = 'user_access'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_in = Column(Integer, nullable=False)
    session_state = Column(String, nullable=False)
    time_create = Column(DateTime, nullable=False, server_default=func.now())


class UserAvatar(Base):
    __tablename__ = 'user_avatar'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    avatar = Column(String)


class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)
    peer_1 = Column(Integer, ForeignKey('user.id'))
    peer_2 = Column(Integer, ForeignKey('user.id'))

    __table_args__ = (
        CheckConstraint('peer_1 != peer_2', name='check_peer_ids_different'),
    )