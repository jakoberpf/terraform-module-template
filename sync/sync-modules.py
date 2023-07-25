# https://digitalvarys.com/git-operations-with-python-scripting/
import os
import shutil
from os import path
from time import strftime, localtime

from git import Repo
from github import Auth, Github

repo_names = [
  "terraform-erpf-gateway-ingress",
  # ## kubernetes
  # "terraform-kubernetes-longhorn-deployment",
  # "terraform-kubernetes-external-secrets-deployment",
  # "terraform-kubernetes-prometheus-stack-deployment",
  # "terraform-kubernetes-prometheus-adapter-deployment",
  # "terraform-kubernetes-certmanager-deployment",
  # "terraform-kubernetes-certificate-manager-deployment",
  # "terraform-kubernetes-secrets-manager-deployment",
  # "terraform-kubernetes-traefik-deployment",
  # "terraform-kubernetes-flux-deployment",
  # "terraform-kubernetes-argo-deployment",
  # "terraform-kubernetes-metallb-deployment",
  # ## proxmox
  # "terraform-proxmox-kubernetes-cluster",
  # "terraform-proxmox-kubernetes-node",
  # ## oracle
  # "terraform-oracle-kubernetes-node",
  # "terraform-oracle-base-vpc",
  # "terraform-oracle-peering-local",
  # ## zerotier
  # "terraform-zerotier-base-network",
  # "terraform-zerotier-base-member",
  # "terraform-zerotier-cluster-network",
]

github_files = [
  ".github/PULL_REQUEST_TEMPLATE.md",
  ".github/auto-release.yml",
  ".github/renovate.json",
  ".github/ISSUE_TEMPLATE/bug_report.md",
  ".github/ISSUE_TEMPLATE/feature_request.md",
  ".github/ISSUE_TEMPLATE/question.md",
  ".github/workflows/auto-release.yml",
  ".github/workflows/pull-request.yaml",
]

sync_branch_name = "terraform-module-template-sync"


def main():
  for repo_name in repo_names:
    git_url = "https://github.com/jakoberpf/" + repo_name
    repo_dir = path.join("repos/", repo_name)

    if path.isdir(repo_dir):
      print("repo already present")
      repo = Repo(repo_dir)
    else:
      print("repo is not present")
      repo = Repo.clone_from(git_url, repo_dir)

    repo.config_writer().set_value("name", "email", "Jakob Boghdady").release()
    repo.config_writer().set_value("name", "email", "github@jakoberpf.de").release()

    os.system("git config --global user.name \"Jakob Boghdady\"")
    os.system("git config --global user.email \"github@jakoberpf.de\"")

    print(repo.remote().refs)

    if sync_branch_name in repo.remote().refs:
      print("branch already exists")
      current = repo.git.checkout(sync_branch_name)
    else:
      print("branch does not exists")
      current = repo.create_head(sync_branch_name).checkout()

    # update .GitHub files

    if path.isdir(path.join(repo_dir, ".github")):
      shutil.rmtree(path.join(repo_dir, ".github"))
      print("files removed")

    shutil.copytree(path.join('.github'), path.join(repo_dir, ".github"))
    print('files updates')

    if repo.index.diff(None) or repo.untracked_files:
      repo.git.add(A=True)
      dtime = strftime('%d-%m-%Y %H:%M:%S', localtime())
      repo.git.commit(m='Updated on' + dtime)
      # repo.git.push('--set-upstream', 'origin', current)
      # print('git push')

    else:
      print('no changes')

    # using an access token
    auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

    # Public Web Github
    github = Github(auth=auth)


if __name__ == '__main__':
  main()
