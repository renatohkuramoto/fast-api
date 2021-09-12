#!/bin/bash

cd /app

eval uvicorn app.app:app --reload --host 0.0.0.0 --port 5000
