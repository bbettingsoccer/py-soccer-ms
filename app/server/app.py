from fastapi import FastAPI
from .routes import soccer_schedule_router as SoccerScheduleRouter
from .routes import soccer_match_router as SoccerMatchRouter
from .routes import soccer_championship_router as ChampionshipRouter

app = FastAPI()
app.include_router(SoccerScheduleRouter.router, tags=["SoccerSchedule"], prefix="/soccer/schedule")
app.include_router(SoccerMatchRouter.router, tags=["SoccerMatch"], prefix="/soccer/match")
app.include_router(ChampionshipRouter.router, tags=["Championship"], prefix="/soccer/championship")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this SheduleMatch domain !"}

