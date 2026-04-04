# ML Backend - Krushi Mitra

This module handles plant disease prediction using a deep learning model.

## Endpoint

POST /predict

Returns:
- prediction
- confidence score

## Run locally

pip install -r requirements.txt  
uvicorn main:app --reload
