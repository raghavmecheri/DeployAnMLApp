from fastapi import FastAPI, Request, HTTPException, Path, Body

from app.models import (
    Input,
    Output
)

from app.services import Predictor

predictor = Predictor()

app = FastAPI(
    title="Sample ML Microservice!",
    version="1.0.0",
    description="An example scikit learn deployment :)",
)

OPEN_ROUTES = ['/docs', '/openapi.json']

@app.post("/api/predict/spamfilter", response_model=Output, tags=["PRED"])
def label_images(body: Input):
	output = predictor.predict(body.message)
	return { "output": output }