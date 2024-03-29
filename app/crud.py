from sqlalchemy.orm import Session

from core import models
from sqlalchemy.orm import Session

from core import models
from core import schemas


def getCampaignsDB(db: Session, skip: int = 0, limit: int = 10):
    """Get a list of campaigns
    Args:
        db (Session): The database session
        skip (int, optional): The number of campaigns to skip. Defaults to 0.
        limit (int, optional): The maximum number of campaigns to return. Defaults to 10.

    Returns:
        [models.Item]: A list of campaigns
    """
    return db.query(models.Campaign).offset(skip).limit(limit).all()

def getAdsetsDB(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Adset).offset(skip).limit(limit).all()


def getAdsetsByCampaginIdDB(db: Session, campaignId: int, skip: int = 0, limit: int = 10):
    return db.query(models.Adset).filter(models.Adset.campaign_id == campaignId).all()

def getAdsetsByGroupIdDB(db: Session, groupId: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Adset).join(models.AdsetGroupAssociation).filter(models.AdsetGroupAssociation.group_id == groupId).all()
    )

def getGroupsDB(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Group).offset(skip).limit(limit).all()


def createAdsetDB(db: Session, adset: schemas.Adset):
    db_adset = models.Adset(**adset.model_dump())
    db.add(db_adset)
    db.commit()
    db.refresh(db_adset)

    return db_adset

def createCampaignDB(db: Session, campaign: schemas.Campaign):
    db_campaign = models.Campaign(**campaign.model_dump())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)

    return db_campaign

def createGroupDB(db: Session, group: schemas.Group):
    db_group = models.Group(**group.model_dump())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group


