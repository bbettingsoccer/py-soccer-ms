from typing import List

from fastapi import APIRouter, Body
from app.server.common.match_constants import MatchConstants
from app.server.model.championship_model import ChampionshipModel
from app.server.service.soccer_championship_service import ChampionshipService

router = APIRouter()


@router.get("/", response_description="Match retrieved")
async def getChampionshipByAll():
    service = ChampionshipService()
    try:
        objectL = await service.getChampionshipsForAll()
        if objectL:
            return ChampionshipModel.ResponseModel(objectL, "Championship data retrieved successfully")
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 404, "Championship doesn't exist.")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/code/{code}")
async def getChampionshipByCode(code: str):
    service = ChampionshipService()
    values = [code]
    try:
        objectL = await service.getChampionshipForCondition(MatchConstants.GET_SEARCH_CHAMPIONSHIP_CODE, values)
        if objectL:
            return ChampionshipModel.ResponseModel(objectL, "Data retrieved successfully")
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 404, "Championship doesn't exist.")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")

@router.get("/name/{name}")
async def getChampionshipByName(name: str):
    service = ChampionshipService()
    values = [name]
    objectL = await service.getChampionshipForCondition(MatchConstants.GET_SEARCH_CHAMPIONSHIP_NAME, values)
    try:
        if objectL:
            return ChampionshipModel.ResponseModel(objectL, "Match data retrieved successfully")
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 404, "Championship doesn't exist.")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.get("/country/{country}", response_description="Data retrieved")
async def getChampionshipByCountry(country: str):
    service = ChampionshipService()
    values = [country]
    try:
        objectL = await service.getChampionshipForCondition(MatchConstants.GET_SEARCH_COUNTRY, values)
        if objectL:
            return ChampionshipModel.ResponseModel(objectL, "Data retrieved successfully")
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 404, "Championship doesn't exist.")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.post("/", response_description="Data saved successfully")
async def postChampionship(data: List[ChampionshipModel] = Body(...)):
    service = ChampionshipService()
    try:
        jsonObj = await service.saveChampionship(data)
        if jsonObj:
            return ChampionshipModel.ResponseModel(None, "Championship data save successfully")
        return ChampionshipModel.ErrorResponseModel("Conflict", 409, "You have same registers in database")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.put("/id/{id}", response_description="Data update the database")
async def putChampionship(id: str, data: ChampionshipModel = Body(...)):
    data = {k: v for k, v in data.dict().items() if v is not None}
    service = ChampionshipService()
    try:
        json_obj = await service.updateChampionship(id, data)
        if json_obj:
            return ChampionshipModel.ResponseModel("Update".format(id), "Success")
        return ChampionshipModel.ErrorResponseModel("Update", 404, "Error update transaction")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")


@router.delete("/{championship}", response_description="Data deleted from the database")
async def deleteChampionship(championship: str):
    service = ChampionshipService()
    try:
        object_id = await service.deleteChampionshipForCondition(MatchConstants.DELETE_CHAMPIONSHIP_NAME, championship)
        if object_id:
            return ChampionshipModel.ResponseModel("Delete", "delete for date successfully")
        return ChampionshipModel.ErrorResponseModel("Delete", 404, "Champions doesn't exist.")
    except Exception:
        return ChampionshipModel.ErrorResponseModel("An error occurred.", 500, "HTTP 500 Internal Server Error")
