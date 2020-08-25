# Idea-Vault
This project was made because I have a lot of great ideas when I'm away from my computer, and I tend to forget them if I don't write them down. So instead of just using a notes app, I created this script that I run from my phone (*via SSH on raspberry pi*), to be able to insert my new idea right into my project planning workflow, with the option of making a git repository for it as well.

# Installation
```
git clone "https://github.com/EzraKatzman/Idea-vault.git"
cd Idea-Vault
pip install -r requirements.txt
touch .env
add your username, password, and github auth token to the .env file
```

# Env File format
```
NOTIONUSER="username"
NOTIONPASS="password"
TOKEN="token"
```
