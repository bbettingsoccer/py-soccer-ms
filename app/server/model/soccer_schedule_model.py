from pydantic import BaseModel, Field, constr, create_model


class SoccerScheduleModel(BaseModel):
    team_a: constr(strict=True) = Field(...)
    team_b: constr(strict=True) = Field(...)
    local_match: constr(strict=True) = Field(...)
    date_match: constr(strict=True) = Field(...)
    time_match: constr(strict=True) = Field(...)
    status: constr(strict=True) = Field(...)

    class config:

        team_a = "team_a"
        team_b = "team_b"
        local_match = "local_match"
        date_match = "date_match"
        time_match = "time_match"
        status = "status"

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        OptionalModel = create_model(
            f"Optional{cls.__name__}",
            __base__=SoccerScheduleModel,
            **{
                k: (v.annotation, None) for k, v in SoccerScheduleModel.model_fields.items()
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
    def data_helper(soccer_schedule) -> dict:
        return {
            "_id": str(soccer_schedule['_id']),
            "team_a": str(soccer_schedule["team_a"]),
            "team_b": str(soccer_schedule["team_b"]),
            "local_match": str(soccer_schedule["local_match"]),
            "date_match": str(soccer_schedule["date_match"]),
            "time_match": str(soccer_schedule["time_match"]),
            "status": str(soccer_schedule["status"]),
        }
