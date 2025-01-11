# Description: FastAPI application that will serve as the API for the support agent.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.support_agent import InternetSupportAgent

app = FastAPI()
agent = InternetSupportAgent()

class UserInput(BaseModel):
    message: str

@app.post("/support")
async def support(user_input: UserInput):
    if not user_input.message:
        raise HTTPException(status_code=400, detail="Message is required")
    response = agent.handle_request(user_input.message)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    