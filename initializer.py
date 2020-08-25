from github import Github
import sys, os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

args = sys.argv
args.pop(0)
reponame = ' '.join(args)

def create():
    user = Github(token).get_user()
    user.create_repo(reponame)
    print(f"Successfully created repository {reponame}")

if __name__ == "__main__":
    create()
    