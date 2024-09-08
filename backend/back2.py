from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from db1 import get_transactions, get_user_settings, update_user_settings

app = FastAPI()

# Добавляем поддержку CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5047","http://194.87.239.209"],  # Можно указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserSettings(BaseModel):
    telegram_id: str
    settings: dict

@app.get("/get_user_settings")
async def get_user_settings_api(telegram_id: str):
    if not telegram_id:
        raise HTTPException(status_code=400, detail="telegram_id is required")
    
    settings = get_user_settings(telegram_id)
    if settings:
        return settings
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/get_transactions")
async def get_transactions_api():
    transactions = get_transactions()
    print(111)
    return transactions

@app.post("/api/update_user_settings")
async def update_user_settings_api(user_settings: UserSettings):
    telegram_id = user_settings.telegram_id
    settings = user_settings.settings
    
    if not telegram_id or not settings:
        raise HTTPException(status_code=400, detail="telegram_id and settings are required")
    
    update_user_settings(telegram_id, settings)
    return {"message": "User settings updated successfully"}

if __name__ == '__main__':
   
    uvicorn.run(app, host="0.0.0.0", port=8000)
