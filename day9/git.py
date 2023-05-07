# Git is a version-control system

# Importance of Git are; It helps in team collaboration and version
# control of a projects

# On installing git to the system, we can use it's CLI (Command Line Interface)

# We upload all the codes somewhere in the cloud and that place in most cases is
# GitHub

# We have different GitHub like cloud systems like GitLab and Bitbucket

# We have local repository and remote repository in VCS.
# (Version Control System)



# Git Commands

# git init  # It initializes a local repository
# git config --global user.name "<username>"
# git config --global user.email "<email>"


# Steps to Push the code to github repo
# git status  # shows the current status of files
# 1. git add . (git add --all)
# 2. git commit -m "<commit-message>"   # -m is flag for message
# 3. git push -u origin <branch_name>

# 4. git branch   # Gives all the branches and highlights the current branch

# 5. git remote add <remote_name> <host-alias>:<ssh-link>   # Adds a new origin to local. This is done
# to establish connection between local and remote repos.

# 6. git remote -v   # To check your remote names
# 7. git remote remove <remote_name>   # removes the remote alias name (origin)
# 8. ssh-keygen -t rsa -b 4096 -C "your_email@example.com"  # Generates an SSH key
# 9. git diff  # shows recent changes



############# Git Branch ##########################


# 1. git branch  # Lists all the branches and highlights the current branch
# 2. git branch <branch_name> # Creates a new branch
# 3. git checkout <branch_name>  # jumps (checkout) to new branch

# 2 and 3 can be obtained from single command from the below command:
# 4. git checkout -b <branch_name>

# 6. git merge <branch_name>  # This merges the code from <branch_name> to
# the current branch.
# git branch -D <branch_name>
