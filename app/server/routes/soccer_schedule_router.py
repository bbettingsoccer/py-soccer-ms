from fastapi import APIRouter, Body
from app.server.common.match_constants import MatchConstants
from app.server.model.soccer_schedule_model import SoccerScheduleModel
from app.server.service.soccer_schedule_service import SoccerScheduleService
from typing import List

router = APIRouter()


@router.get("/championship/{championship}", response_description="Match retrieved")
async def getSoccerScheduleByAll(championship: str):
    service = SoccerScheduleService(championship)
    try:
        objectL = await service.getSoccerScheduleForAll()
        if objectL:
            return SoccerScheduleModel.ResponseModel(objectL, "Soccer Schedule data retrieved successfully")
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 404, "SoccerSchedule doesn't exist.")
    except Exception:
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/championship/{championship}/dateMatch/{dateMatch}")
async def getSoccerScheduleByDateMatch(championship: str, dateMatch: str):
    service = SoccerScheduleService(championship)
    values = [dateMatch]
    try:
        objectL = await service.getSoccerScheduleForCondiction(MatchConstants.GET_SEARCH_DATE, values)
        if objectL:
            return SoccerScheduleModel.ResponseModel(objectL, "Soccer Schedule data retrieved successfully")
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 404, "SoccerSchedule doesn't exist.")
    except Exception:
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/championship/{championship}/team/{team}", response_description="Match retrieved")
async def getSoccerScheduleByTeam(championship: str, team: str):
    service = SoccerScheduleService(championship)
    values = [team]
    try:
        objectL = await service.getSoccerScheduleForCondiction(MatchConstants.GET_SEARCH_TEAM, values)
        if objectL:
            return SoccerScheduleModel.ResponseModel(objectL, "Soccer Schedule data retrieved successfully")
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 404, "SoccerSchedule doesn't exist.")
    except Exception:
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/championship/{championship}/team/{team}/dateMatch/{dateMatch}", response_description="Match retrieved")
async def getSoccerScheduleByDateMatchAndTeam(championship: str, team: str, dateMatch: str):
    service = SoccerScheduleService(championship)
    values = [dateMatch, team]
    try:
        objectL = await service.getSoccerScheduleForCondiction(MatchConstants.GET_SEARCH_TEAM_DATE_MATCH, values)
        if objectL:
            return SoccerScheduleModel.ResponseModel(objectL, "Soccer Schedule data retrieved successfully")
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 404, "Soccer Schedule doesn't exist.")
    except Exception:
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.post("/championship/{championship}", response_description="Data saved successfully")
async def postSoccerSchedule(championship: str, data: List[SoccerScheduleModel] = Body(...)):
    service = SoccerScheduleService(championship)
    try:
        json_obj = await service.saveSoccerSchedule(data)
        if json_obj:
            return SoccerScheduleModel.ResponseModel(None, "Soccer Schedule data save  successfully")
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 421, "SoccerSchedule Already registered")
    except Exception:
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.put("/championship/{championship}/id/{id}", response_description="Data update the database")
async def putSoccerSchedule(championship: str, id: str, req: SoccerScheduleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    service = SoccerScheduleService(championship)
    try:
        object_id = await service.updateSoccerSchedule(id, req)
        if object_id:
            return SoccerScheduleModel.ResponseModel(None, "Soccer Schedule update successfully".format(id))
        return SoccerScheduleModel.ErrorResponseModel("An error occurred.", 404, "Soccer Schedule doesn't exist.")
    except Exception:
        return SoccerScheduleModel.ErrorResponseModel("Error", 404, "Error update transaction")
