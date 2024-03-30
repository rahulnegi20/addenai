from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from dependency import get_db
from core import schemas
import crud as DB

from typing_extensions import Annotated
from sqlalchemy.orm import Session

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/getAdsets")
async def getAdsets(db: db_dependency, skip: int = 0, limit: int = 10):
    try:
        res = DB.getAdsetsDB(db, skip=skip, limit=limit)
        return JSONResponse(content={"adsets": res}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")   

@router.get("/getAdsetsByCampaginId/{campaignId}")
async def getAdsetsbyCampaignId(db: db_dependency, campaignId: str, skip: int = 0, limit: int = 10):
    try:
        res = DB.getAdsetsByCampaginIdDB(db, int(campaignId), skip=skip, limit=limit)
        return JSONResponse(content={"adsets": res}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")   

@router.get("/getAdsetsByGroupId/{groupId}")
async def getAdsetsbyGroupId(db: db_dependency, groupId: str, skip: int = 0, limit: int = 10):
    try:
        res = DB.getAdsetsByGroupIdDB(db, int(groupId), skip=skip, limit=limit)
        return JSONResponse(content={"adsets": res}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")  
     
@router.get("/getCampaigns")
async def getCampaigns(db: db_dependency, skip: int = 0, limit: int = 10):
    try:
        res = DB.getCampaignsDB(db, skip=skip, limit=limit)
        return JSONResponse(content={"campaigns": res}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")   


@router.get("/getGroups")
async def getGroups(db: db_dependency, skip: int = 0, limit: int = 10):
    try:
        res = DB.getGroupsDB(db, skip=skip, limit=limit)
        return JSONResponse(content={"groups": res}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")   

@router.post("/createAdset", status_code=status.HTTP_201_CREATED)
async def createAdset(db:db_dependency, adset: schemas.Adset):
    try:
        print(adset)
        ans = DB.createAdsetDB(db=db, adset=adset)

        return JSONResponse(content={"response":"Created Sucessfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")


@router.post("/createCampaign")
async def createCampaign(db:db_dependency, campaign: schemas.Campaign):
    try:
        ans = DB.createCampaignDB(db=db, campaign=campaign)

        return JSONResponse(content={"response": "Created Sucessfull"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")   


@router.post("/createGroup", status_code=status.HTTP_201_CREATED)
async def createCampaign(db:db_dependency, group: schemas.Group):
    try:
        ans = DB.createGroupDB(db=db, group=group)

        return JSONResponse(content={"response": "Created Sucessfull"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed with error: {e}")   