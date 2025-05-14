#!/usr/bin/env bash
# Start Go backend
(cd backend && go run .) &
sleep 1
# Start Python frontend
(cd frontend && ../.venv/bin/python app.py)
EOF
chmod +x scripts/run.sh
git add scripts/run.sh
git commit -m "feat: add run script to launch backend and frontend"
