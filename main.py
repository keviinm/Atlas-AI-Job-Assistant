from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from mangum import Mangum  # ✅ Required for AWS Lambda

app = FastAPI(title="Atlas AI Job Assistant API")

# CORS settings (needed for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

# ✅ AWS Lambda Handler
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
