#!/bin/bash
echo "🚀 Setting up TheraBot..."

# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../frontend
pip install -r requirements.txt

echo "✅ Setup complete!"
