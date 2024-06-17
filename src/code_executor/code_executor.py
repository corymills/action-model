from fastapi import FastAPI, Request
import uvicorn
import uuid
from io import StringIO
import sys

app = FastAPI()

environments = {}

@app.post("/setup")
async def setup_environment():
    env_id = str(uuid.uuid4())
    environments[env_id] = {
        "globals": {},
        "locals": {},
        "code_history": []
    }
    return {"env_id": env_id}

@app.post("/execute")
async def execute_code(request: Request):
    payload = await request.json()
    env_id = payload["env_id"]
    code = payload["code"]

    if env_id not in environments:
        return {"error": "Environment not found"}

    env = environments[env_id]
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code, env["globals"], env["locals"])
        sys.stdout = old_stdout
        env["code_history"].append(code)
        locals = env["locals"]
        globals = env["locals"]
        output = redirected_output.getvalue()
    
        return {"output": output, "locals": locals, "globals": globals}
    except Exception as e:
        return {"error": str(e)}

@app.post("/shutdown")
async def shutdown_environment(request: Request):
    payload = await request.json()
    env_id = payload["env_id"]

    if env_id not in environments:
        return {"error": "Environment not found"}

    del environments[env_id]
    return {"message": "Environment shutdown"}

@app.get("/code_history/{env_id}")
async def get_code_history(env_id: str):
    if env_id not in environments:
        return {"error": "Environment not found"}

    env = environments[env_id]
    code_history = env["code_history"]
    return {"code_history": code_history}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)