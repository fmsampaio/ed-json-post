from fastapi import FastAPI, Depends, HTTPException, status, Response

from .database import SessionLocal, get_db, Base, engine
from . import schemas, models

from fastapi.middleware.cors import CORSMiddleware

import json

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def index(): 
    return {
        'info' : 'API for practicing JSON manipulation'
    }

@app.get("/data")
def list_all(db: SessionLocal = Depends(get_db)):
    data = db.query(models.JsonData).all()
    return data

@app.post('/data')
def create(request: schemas.StudentData, db: SessionLocal = Depends(get_db)):
    new_json_data = models.JsonData(json_data = json.dumps(request.getJson()))
    db.add(new_json_data)
    db.commit()
    db.refresh(new_json_data)
    return new_json_data

@app.delete('/data/{id}')
def destroy(id: int, db: SessionLocal = Depends(get_db)):
    query = checkDataById(id, db)
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def checkDataById(id, db):
    query = db.query(models.JsonData).filter(models.JsonData.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student data with id equals to {id} was not found')
    return query