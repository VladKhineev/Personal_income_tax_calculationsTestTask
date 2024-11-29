import uvicorn
from fastapi import FastAPI

# from report.routers import router as router_report

app = FastAPI(title='PITC')

# app.include_router(router_report)

@app.get('/')
def top():
    return 'Hello'