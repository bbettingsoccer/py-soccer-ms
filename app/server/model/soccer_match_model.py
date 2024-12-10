from pydantic import BaseModel, Field, constr, create_model



class SoccerMatchModel(BaseModel):
    team_a: constr(strict=True) = Field(default=None, title="team_a")
    team_b: constr(strict=True) = Field(default=None, title="team_b")
    date_match: constr(strict=True) = Field(default=None, title="date_match")
    score_a: constr(strict=True) = Field(default=None, title="score_a")
    score_b: constr(strict=True) = Field(default=None, title="score_b")
    status: constr(strict=True) = Field(default=None, title="status")

    class config:
        team_a = "team_a"
        team_b = "team_b"
        date_match = "date_match"
        score_a = "score_a"
        score_b = "score_b"
        status = "status"

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        OptionalModel = create_model(
            f"Optional{cls.__name__}",
            __base__=SoccerMatchModel,
            **{
                k: (v.annotation, None) for k, v in SoccerMatchModel.model_fields.items()
            })

        #        fields = {
        #           attribute: (Optional[data_type.type_], None)
        #          for attribute, data_type in annonations.items()
        #     }
        # OptionalModel = create_model(f"Optional{cls.__name__}", **fields)
        return OptionalModel

    def ResponseModel(data, message):
        return {
            "data": [data],
            "code": 200,
            "message": message,
        }

    def ErrorResponseModel(error, code, message):
        return {"error": error, "code": code, "message": message}

    @staticmethod
    def data_helper(soccer_match) -> dict:
        return {
            "_id": str(soccer_match['_id']),
            "team_a": str(soccer_match["team_a"]),
            "team_b": str(soccer_match["team_b"]),
            "date_match": str(soccer_match["date_match"]),
            "score_a": str(soccer_match["score_a"]),
            "score_b": str(soccer_match["score_b"]),
            "status": str(soccer_match["status"]),
        }
