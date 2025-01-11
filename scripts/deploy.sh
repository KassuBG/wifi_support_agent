#!/bin/bash
# Deploy the agent to Heroku

# Login to Heroku
heroku login

# Create a new Heroku app
heroku create

# Set environment variables
heroku config:set DEBUG=True

# Deploy the app
git push heroku main

# Open the app in the browser
heroku open