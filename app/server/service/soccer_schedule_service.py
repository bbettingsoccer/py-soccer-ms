from app.server.common.match_constants import MatchConstants
from app.server.dao.operationimpl_dao import OperationImplDAO
from app.server.model.soccer_schedule_model import SoccerScheduleModel
from fastapi.encoders import jsonable_encoder
from typing import List


class SoccerScheduleService:

    def __init__(self, championship: str):
        collection = championship + MatchConstants.DOMAIN_SOCCER_OPERATION_SCHEDULE
        print("collection >>> ", collection)
        self.collection = OperationImplDAO(collection)

    async def getSoccerScheduleForAll(self):
        print("getSoccerScheduleForAll ")
        objectL = []
        try:
            objects = await self.collection.find_condition(None)
            print("getSoccerScheduleForAll - objects", objects)

            if objects:
                for objected in objects:
                    objectL.append(SoccerScheduleModel.data_helper(objected))
            return objectL
        except Exception as e:
            print("[Error :: Service] - FindAll")
            return None

    async def getSoccerScheduleForCondiction(self, search: str, values: []):
        objectL = []
        filter = []
        match search:
            case MatchConstants.GET_SEARCH_DATE:
                filter = {SoccerScheduleModel.config.date_match: values[0]}
            case MatchConstants.GET_SEARCH_TEAM:
                filter = {"$or": [{SoccerScheduleModel.config.team_a: {"$eq": values[0]}},
                                  {SoccerScheduleModel.config.team_b: {"$eq": values[0]}}]}
            case MatchConstants.GET_SEARCH_TEAM_DATE_MATCH:
                filter = {"$and": [{SoccerScheduleModel.config.date_match: {"$eq": values[0]}},
                                   {"$or": [
                                       {SoccerScheduleModel.config.team_a: {"$eq": values[1]}},
                                       {SoccerScheduleModel.config.team_b: {"$eq": values[1]}}]
                                   }]
                          }
            case MatchConstants.GET_SEARCH_TEAMS_DATE_MATCH:
                filter = {"$and": [{SoccerScheduleModel.config.date_match: {"$eq": values[0]}},
                                   {"$or": [
                                       {SoccerScheduleModel.config.team_a: {"$eq": values[1]}},
                                       {SoccerScheduleModel.config.team_b: {"$eq": values[2]}}]
                                   }]
                          }

        try:
            objects = None
            objects = await self.collection.find_condition(filter)
            if objects:
                for objected in objects:
                    objectL.append(SoccerScheduleModel.data_helper(objected))
                return objectL
        except Exception as e:
            print("[Error :: Service] - FindCondition > Filter :", filter)
            return None

    async def updateSoccerSchedule(self, id: str, data: dict):
        if len(data) < 1:
            return False
        try:
            objFind = await self.collection.find_one(id)
            if objFind:
                await self.collection.update_one(id, data)
                return True
            return False
        except Exception as e:
            print('Error :: Service] - Update >', data)
            return False

    async def saveSoccerSchedule(self, data: List[SoccerScheduleModel]):
        result = False
        try:
            for json_obj in data:
                values = [json_obj.date_match, json_obj.team_a, json_obj.team_a]
                objUpdateOrSave = await self.getSoccerScheduleForCondiction(
                    MatchConstants.GET_SEARCH_TEAMS_DATE_MATCH, values)

                if objUpdateOrSave is None:  # SAVE - Transaction
                    result = True
                    currentMatchSave = jsonable_encoder(json_obj)
                    await self.collection.save(currentMatchSave)
            return result
        except Exception as e:
            print("[Error :: Service] - Save")
