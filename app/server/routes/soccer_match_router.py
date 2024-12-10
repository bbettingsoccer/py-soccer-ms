from fastapi import APIRouter
from app.server.common.match_constants import MatchConstants
from app.server.service.soccer_match_service import SoccerMatchService
from app.server.model.soccer_match_model import SoccerMatchModel

router = APIRouter()


@router.get("/championship/{championship}", response_description="Match retrieved")
async def getSoccerMatchByAll(championship: str):
    service = SoccerMatchService(championship)
    try:
        currentsL = await service.getSoccerMatchForAll()
        if currentsL:
            return SoccerMatchModel.ResponseModel(currentsL, "Soccer Match data retrieved successfully")
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 404, "Soccer Match doesn't exist.")
    except Exception:
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/championship/{championship}/status/{status}")
async def getSoccerMatchByStatus(championship: str, status: str):
    service = SoccerMatchService(championship)
    values = [status]
    try:
        matchL = await service.getSoccerMatchForCondiction(MatchConstants.GET_SEARCH_STATUS, values)
        if matchL:
            return SoccerMatchModel.ResponseModel(matchL, "Soccer Match data retrieved successfully")
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 404, "Soccer Match doesn't exist.")
    except Exception:
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/championship/{championship}/date_match/{date_match}", response_description="Match retrieved")
async def getSoccerMatchByDateMatch(championship: str, date_match: str):
    service = SoccerMatchService(championship)
    values = [date_match]
    try:
        matchL = await service.getSoccerMatchForCondiction(MatchConstants.GET_SEARCH_DATE_MATCH, values)
        if matchL:
            return SoccerMatchModel.ResponseModel(matchL, "Soccer Match data retrieved successfully")
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 404, "Soccer Match doesn't exist.")
    except Exception:
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/championship/{championship}/team/{team}", response_description="Match retrieved")
async def getSoccerMatchByTeam(championship: str, team: str):
    service = SoccerMatchService(championship)
    values = [team]
    try:
        matchL = await service.getSoccerMatchForCondiction(MatchConstants.GET_SEARCH_TEAM, values)
        if matchL:
            return SoccerMatchModel.ResponseModel(matchL, "Match data retrieved successfully")
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 404, "Soccer Match doesn't exist.")
    except Exception:
        return SoccerMatchModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")
