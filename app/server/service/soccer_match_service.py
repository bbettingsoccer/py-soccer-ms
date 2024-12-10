from app.server.common.match_constants import MatchConstants
from app.server.dao.operationimpl_dao import OperationImplDAO
from app.server.model.soccer_match_model import SoccerMatchModel


class SoccerMatchService:

    def __init__(self, championship: str):
        collection = championship + MatchConstants.DOMAIN_SOCCER_OPERATION_MATCH
        self.collection = OperationImplDAO(collection)

    async def getSoccerMatchForAll(self):
        currentsL = []
        try:
            currents = await self.collection.find_condition(None)
            if currents:
                for currented in currents:
                    print(currents)
                    currentsL.append(SoccerMatchModel.data_helper(currented))
                return currentsL
        except Exception as e:
            print("[Error :: Service] - Find")
        return None

    async def getSoccerMatchForCondiction(self, search: str, values: []):
        currentsL = []
        filter = []
        match search:
            case MatchConstants.GET_SEARCH_STATUS:
                filter = {SoccerMatchModel.config.status: values[0]}
            case MatchConstants.GET_SEARCH_DATE_MATCH:
                filter = {SoccerMatchModel.config.date_match: {"$eq": values[0]}}
            case MatchConstants.GET_SEARCH_TEAM:
                filter = {"$or": [{SoccerMatchModel.config.team_a: {"$eq": values[0]}},
                                  {SoccerMatchModel.config.team_b: {"$eq": values[0]}}]}
        try:
            currents = await self.collection.find_condition(filter)

            if currents:
                for currented in currents:
                    currentsL.append(SoccerMatchModel.data_helper(currented))
                return currentsL
        except Exception as e:
            print("[Error :: Service] - Find_Condition > Filter :", filter)
        return None
