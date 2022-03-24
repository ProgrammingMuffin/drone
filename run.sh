#!/bin/bash 
cd client/drone/
npm install
npm run dev >> /dev/null &
cd ../../server/
python3 main.py &
