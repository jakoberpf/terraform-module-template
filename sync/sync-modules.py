# https://digitalvarys.com/git-operations-with-python-scripting/
import contextlib
import os
import shutil
from os import path
from time import strftime, localtime

from git import Repo
from github import Auth, Github

sync_branch_name = "terraform-module-template-sync"

repo_owner = os.getenv("REPO").split("/")[0]
repo_name = os.getenv("REPO").split("/")[1]

github_token = os.getenv("REPO_WORKFLOWS_TOKEN")


def clone_or_fetch_repository(token, owner, repo):
  git_url = f"https://{owner}:{token}@github.com/{owner}/{repo}.git"
  print(f"{git_url}")
  repo_dir = path.join("repos/", repo)
  print(f"{repo_dir}")

  if path.isdir(repo_dir):
    print("repo already present, not cloning")
    repo = Repo(repo_dir)
  else:
    print("repo is not present, cloning repo")
    repo = Repo.clone_from(git_url, repo_dir)
    print("repo cloned")

  return repo


# def checkout_branch_or_create():


def create_pull_request(github, owner, repo, base_branch, head_branch, title, body):
  repo = github.get_repo(f"{owner}/{repo}")

  pull_exists: bool = False
  for pull in repo.get_pulls():
    if pull.title == title:
      pull_exists = True

  if not pull_exists:
    # Create the pull request
    pull_request = repo.create_pull(
      title=title,
      body=body,
      base=base_branch,
      head=head_branch
    )

    print(f"Pull request created: {pull_request.html_url}")
    return pull_request
  else:
    print("Pull request already exists")
    return None


def main():
  repo = clone_or_fetch_repository(github_token, repo_owner, repo_name)

  repo.config_writer().set_value("name", "email", "Jakob Boghdady").release()
  repo.config_writer().set_value("name", "email", "58260820+jakoberpf@users.noreply.github.com").release()

  os.system("git config --global user.name \"Jakob Boghdady\"")
  os.system("git config --global user.email \"58260820+jakoberpf@users.noreply.github.com\"")

  if sync_branch_name in repo.remote().refs:
    print("branch already exists")
    repo.git.checkout(sync_branch_name)
  else:
    print("branch does not exists")
    repo.create_head(sync_branch_name).checkout()

  # update .GitHub files

  if path.isdir(path.join(path.join("repos/", repo_name), ".github")):
    shutil.rmtree(path.join(path.join("repos/", repo_name), ".github"))
    print("files removed")

  shutil.copytree(path.join('.github'), path.join(path.join("repos/", repo_name), ".github"))

  with contextlib.suppress(FileNotFoundError):
    os.remove(path.join("repos/", repo_name) + '/.github/workflows/sync-modules.yaml')

  print('files updates')

  if repo.index.diff(None) or repo.untracked_files:
    repo.git.add(A=True)
    dtime = strftime('%d-%m-%Y %H:%M:%S', localtime())
    repo.git.commit(m='Updated on ' + dtime)
    repo.git.push('--set-upstream', 'origin', sync_branch_name)
    print('git push')

  else:
    print('no changes')

  auth = Auth.Token(github_token)
  github = Github(auth=auth)

  title = "Sync from template module"
  body = "This pull request syncs this module with the template module."
  base_branch = "main"

  create_pull_request(github, repo_owner, repo_name, base_branch, sync_branch_name, title, body)


if __name__ == '__main__':
  main()
