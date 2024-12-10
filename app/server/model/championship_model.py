from pydantic import BaseModel, Field, constr, conint, create_model


class ChampionshipModel(BaseModel):
    championship: constr(strict=True) = Field(...)
    code_name: constr(strict=True) = Field(...)
    country: constr(strict=True) = Field(...)
    image: constr(strict=True) = Field(...)
    total_teams: conint(strict=True) = Field(...)
    date_start: constr(strict=True) = Field(...)
    date_end: constr(strict=True) = Field(...)
    status: constr(strict=True) = Field(...)

    class config:
        championship = "championship"
        code_name = "code_name"
        country = "country"
        image = "image"
        total_teams = "total_teams"
        date_start = "date_start"
        date_end = "date_end"
        status = "status"

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        OptionalModel = create_model(
            f"Optional{cls.__name__}",
            __base__=ChampionshipModel,
            **{
                k: (v.annotation, None) for k, v in ChampionshipModel.model_fields.items()
            })
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
    def data_helper(championship) -> dict:
        return {
            "_id": str(championship['_id']),
            "championship": str(championship["championship"]),
            "code_name":  str(championship["code_name"]),
            "country": str(championship["country"]),
            "image": str(championship["image"]),
            "total_teams": str(championship["total_teams"]),
            "date_start": str(championship["date_start"]),
            "date_end": str(championship["date_end"]),
            "status": str(championship["status"]),
        }
