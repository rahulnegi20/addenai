from pydantic import BaseModel

class AdsetBase(BaseModel):
    name:str
    optimization_goal:str
    campaign_id:int

class AdsetCreate(AdsetBase):
    pass

class Adset(AdsetBase):

    class Config:
        orm_mode = True

class CampaignBase(BaseModel):
    name: str
    objective: str

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):

    class Config:
        orm_mode = True
