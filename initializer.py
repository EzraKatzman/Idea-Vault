from github import Github
import sys, os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("GITUSER")
password = os.getenv("GITPASS")

args = sys.argv
args.pop(0)
reponame = ' '.join(args)

def create():
    user = Github(username, password).get_user()
    user.create_repo(reponame)
    print(f"Successfully created repository {reponame}")

if __name__ == "__main__":
    create()
    