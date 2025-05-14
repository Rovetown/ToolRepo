#!/usr/bin/env bash
# Start Go backend
(cd backend && go run .) &
sleep 1
# Start Python frontend
(cd frontend && ../.venv/bin/python app.py)
