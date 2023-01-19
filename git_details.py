# File that gives the active status, recent commits of the git, recents commits of git by previous week and commit was authored by Rufus.

from git import Repo
from datetime import datetime

def printGitDetails(localDir:str):

  #Repository
  local_repo = Repo(localDir)

  #Active Branch
  active_branch = local_repo.active_branch
  print("active branch: "+str(active_branch))

  #Local Changes
  changed = local_repo.index.diff(None)
  ischanged = False
  if len(changed) == 0:
    ischanged = False
  else:
    ischanged = True

  print("local changes: ",ischanged)

  #Recent Commit
  recentCommit = local_repo.commit(str(active_branch))
  commitedTime = datetime.fromtimestamp(recentCommit.committed_date)
  currentTime = datetime.now()
  diffTime = currentTime - commitedTime
  isRecentCommit = True
  if diffTime.days > 7:
    isRecentCommit = False

  print("recent commit: ",isRecentCommit)

  #Author Rufus
  blameRufus = False
  if recentCommit.author.name == "Rufus":
    blameRufus = True

  print("blame Rufus: ",blameRufus)

#input the github repository
git_directory_path = input("Enter git hub directory path....")

printGitDetails(git_directory_path)