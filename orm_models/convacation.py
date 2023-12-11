from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Boolean
from sqlalchemy.orm import relationship

from . import Base


class Tribe(Base):
    __tablename__ = 'tribe'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    school_name = Column(String, nullable=False)


class Election(Base):
    __tablename__ = 'election'

    id = Column(Integer, primary_key=True)
    tribe_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    time_start_collection = Column(DateTime, nullable=False, comment="Время начала выдвижения кандидатов")
    time_finish_collection = Column(DateTime, nullable=False, comment="Время окончания выдвижения кандидатов")
    time_start_voting = Column(DateTime, nullable=False, comment="Время начала голосования")
    time_finish_voting = Column(DateTime, nullable=False, comment="Время окончания голосования")
    is_finished = Column(Boolean, default=False)

    tribe = relationship("Tribe", backref="election")


class Candidate(Base):
    __tablename__ = 'candidate'

    id = Column(Integer, primary_key=True)
    election_id = Column(Integer, ForeignKey("election.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("capybara.id"), nullable=False)
    is_approved = Column(Boolean, default=False)
    about = Column(String, nullable=False)

    election = relationship("Election", backref="candidate")
    user = relationship("Capybara", backref="candidate")


class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    election_id = Column(Integer, ForeignKey("election.id"), nullable=False)
    voter_id = Column(Integer, ForeignKey("capybara.id"), nullable=False)
    candidate_id = Column(Integer, ForeignKey("candidate.id"), nullable=False)

    election = relationship("Election", backref="vote")
    voter = relationship("Capybara", backref="vote")
    candidate = relationship("Candidate", backref="vote")
