# Git

## Project Management Flow

### Create a new branch for a concret task, this is recommanded when a member charges a task

1. Check out a repository
    ```
    git clone /path/to/repository
    ```
2. Locate in the local root directory of the repository
    ```
    cd <path_to_local_root_directory>
    ```
3. List all the branches in your repo, and also tell you what branch you're currently in
    ```
    git branch
    ```
4. Create a a new branch and switch to it for a concret task
    ```
    git checkout -b <branch_name>
    ```
5. Make some changes for this task
6. List the files you've changed and those you still need to add or commit
    ```
    git status
    ```
7. Add the files changed
    ```
    git add -A
    ```
8. Commit changes to head
    ```
    git commit -m "#<task_number> - Commit message"
    ```
9. Push commited changes to the new branch of your remote repository
    ```
    git push origin <branch_name>
    ```
10. Send pull request on GitHub repository web site from the new branch to master branch
11. Project code reviewer merges the new branch into master branch once receving the pull request
    ```
    git merge <branch_name>
    ```

### Modify a branch for a task which needs multiple members

1. Check out a repository
    ```
    git clone /path/to/repository
    ```
2. Locate in the local root directory of the repository
    ```
    cd <path_to_local_root_directory>
    ```
3. List all the branches in your repo, and also tell you what branch you're currently in
    ```
    git branch
    ```
4. Switch to the branch on which you work
    ```
    git checkout <branch_name>
    ```
5. Pull the latest changes from the branch
    ```
    git pull origin <branch_name>
    ```
6. Make some changes for your task
7. List the files you've changed and those you still need to add or commit
    ```
    git status
    ```
8. Temporarily save the changes not committed on a stack
    ```
    git stash
    ```
9. Pull the latest changes from remote server for this branch
    ```
    git pull origin <branch_name>
    ```
10. Bring back the saved changes onto the working directory, and remove them from the stack at the same time
    ```
    git stash pop
    ```
11. List the files you've changed and those you still need to add or commit
    ```
    git status
    ```
12. Add the files changed
    ```
    git add -A
    ```
13. Commit changes to head
    ```
    git commit -m "#<task_number> - Commit message"
    ```
14. Push commited changes to the new branch of your remote repository
    ```
    git push origin <branch_name>
    ```

## Git Articles
- [Basic Git commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html) - Atlassian Stash
- [Git Reference](http://gitref.org) - Git
- [How To Use Git Effectively](https://www.digitalocean.com/community/tutorials/how-to-use-git-effectively) - Jason Kurtz