from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import file_controller

app = FastAPI(
    title="WxO File Upload API",
    description="The wxo file upload API takes the input as file and stores in IBM COS.",
    version="0.1.0",
)

app.include_router(router=file_controller.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs")