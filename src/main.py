from fastapi import FastAPI

from src.report.routers import router as router_report


app = FastAPI(title='PITC')

app.include_router(router_report)