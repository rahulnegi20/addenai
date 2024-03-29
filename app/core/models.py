from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Adset(Base):
    __tablename__ = 'adsets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    optimization_goal  = Column(String)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    campaign = relationship("Campaign", back_populates="adsets")
    groups = relationship("Group", secondary="adset_group_association")


class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    objective = Column(String, nullable=False)
    adsets = relationship("Adset", back_populates="campaign")


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    adsets = relationship("Adset", secondary="adset_group_association")


class AdsetGroupAssociation(Base):
    __tablename__ = 'adset_group_association'
    
    adset_id = Column(Integer,ForeignKey("adsets.id"), primary_key=True) 
    group_id = Column(Integer,ForeignKey("groups.id"), primary_key=True) 

