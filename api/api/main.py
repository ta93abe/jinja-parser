from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from jinja2 import Template

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

class TemplateRequest(BaseModel):
    template: str
    variables: dict

@app.post("/parse")
async def parse_template(request: TemplateRequest):
    template = Template(request.template)
    result = template.render(**request.variables)
    return {"result": result}