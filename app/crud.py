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
    """Get a list of adsets
    Args:
        db (Session): The database session
        skip (int, optional): The number of adsets to skip. Defaults to 0.
        limit (int, optional): The maximum number of adsets to return. Defaults to 10.

    Returns:
        [models.Item]: A list of adsets
    """
    return db.query(models.Adset).offset(skip).limit(limit).all()


def getAdsetsByCampaginIdDB(db: Session, campaignId: int, skip: int = 0, limit: int = 10):
    """Get a list of adsets by campaign id
    Args:
        db (Session): The database session
        campaignId (int): The campaign id
        skip (int, optional): The number of adsets to skip. Defaults to 0.
        limit (int, optional): The maximum number of adsets to return. Defaults to 10.

    Returns:
        [models.Item]: A list of adsets
    """
    return db.query(models.Adset).filter(models.Adset.campaign_id == campaignId).offset(skip).limit(limit).all()

def getAdsetsByGroupIdDB(db: Session, groupId: int, skip: int = 0, limit: int = 10):
    """Get a list of adsets by group id
    Args:
        db (Session): The database session
        groupId (int): The group id
        skip (int, optional): The number of adsets to skip. Defaults to 0.
        limit (int, optional): The maximum number of adsets to return. Defaults to 10.

    Returns:
        [models.Item]: A list of adsets
    """
    return (
        db.query(models.Adset).join(models.AdsetGroupAssociation).filter(models.AdsetGroupAssociation.group_id == groupId).offset(skip).limit(limit).all()
    )

def getGroupsDB(db: Session, skip: int = 0, limit: int = 10):
    """Get a list of groups
    Args:
        db (Session): The database session
        skip (int, optional): The number of groups to skip. Defaults to 0.
        limit (int, optional): The maximum number of groups to return. Defaults to 10.

    Returns:
        [models.Item]: A list of groups
    """
    return db.query(models.Group).offset(skip).limit(limit).all()


def createAdsetDB(db: Session, adset: schemas.Adset):
    """Create an adset
    Args:
        db (Session): The database session
        adset (schemas.Adset): The adset to create

    Returns:
        models.Adset: The created adset
    """
    db_adset = models.Adset(**adset.model_dump())
    db.add(db_adset)
    db.commit()
    db.refresh(db_adset)

    return db_adset

def createCampaignDB(db: Session, campaign: schemas.Campaign):
    """Create a campaign
    Args:
        db (Session): The database session
        campaign (schemas.Campaign): The campaign to create

    Returns:
        models.Campaign: The created campaign
    """
    db_campaign = models.Campaign(**campaign.model_dump())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)

    return db_campaign

def createGroupDB(db: Session, group: schemas.Group):
    """Create a group
    Args:
        db (Session): The database session
        group (schemas.Group): The group to create

    Returns:
        models.Group: The created group
    """
    db_group = models.Group(**group.model_dump())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group
