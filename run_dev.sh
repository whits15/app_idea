#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Start the Flask backend
echo "Starting Flask backend..."
python app/__init__.py &
BACKEND_PID=$!

# Start the React frontend
echo "Starting React frontend..."
cd app/static && npm start &
FRONTEND_PID=$!

# Function to handle script termination
cleanup() {
    echo "Shutting down servers..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit
}

# Set up trap to catch termination signal
trap cleanup SIGINT SIGTERM

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID 