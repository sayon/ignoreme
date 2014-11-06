import os
import sys

remote_repo = "https://github.com/github/gitignore.git"
local_repo = os.path.expandvars("$HOME/.ignoreme")
current_path = os.getcwd();

def init():
    if os.path.exists(local_repo + "/.git"):
        pull()
    else:
        clone()

def clone():
    os.system("git clone -q %s %s" % (remote_repo, local_repo))

def pull():
    os.chdir(local_repo)
    os.system("git pull -q origin master")
    os.chdir(current_path)

def dump(langs):
    init()
    with open(".gitignore", 'w+') as output:
        for lang in langs:
            path = "%s/%s.gitignore" % (local_repo, lang)
            if os.path.exists(path):
                with open(path, 'r') as f:
                    output.write(f.read())

            path = "%s/Global/%s.gitignore" % (local_repo, lang)
            if os.path.exists(path):
                with open(path, 'r') as f:
                    output.write(f.read())

# usage:
dump(['java', 'haskell', 'agda'])