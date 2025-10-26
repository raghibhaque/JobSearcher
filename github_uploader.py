from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_github(file_path, commit_message="AutoJobTracker update"):
    """Uploads local file to GitHub repo."""
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPO")

    g = Github(token)
    repo = g.get_repo(repo_name)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        existing = repo.get_contents(file_path)
        repo.update_file(existing.path, commit_message, content, existing.sha)
        print("✅ File updated on GitHub.")
    except:
        repo.create_file(file_path, commit_message, content)
        print("✅ File created on GitHub.")
