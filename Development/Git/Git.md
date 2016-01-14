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

## Basic Git Commands

Here is a list of some basic Git commands to get you going with Git.
For more detail, check out the  [Atlassian Git Tutorials](https://www.atlassian.com/git/?utm_source=basic-git-commands&utm_medium=link&utm_campaign=git-microsite)  for a visual introduction to Git commands and workflows, including examples.

- Tell Git who you are
* Configure the author name and email address to be used with your commits.Note that Git strips some characters (for example trailing periods) from user.name.
```
git config --global user.name "Sam Smith"
git config --global user.email sam@example.com
```
- Create a new local repository
```
git init
```
- Check out a repository
Create a working copy of a local repository
```
git clone /path/to/repository
```
For a remote server, use
```
git clone username@host:/path/to/repository
```
- Add files
Add one or more files to staging (index)
```
git add <file_name>
git add -A
```
- Status
List the files you've changed and those you still need to add or commit
```
git status
```
- Commit
Commit changes to head (but not yet to the remote repository)
```
git commit -m "#<task_number> - Commit message"
```
Commit any files you've added with git add, and also commit any files you've changed since then
```
git commit -a
```
- Push
Send changes to the feature branch of your remote repository
```
git push origin <branch_name>
```
- Connect to a remote repository
If you haven't connected your local repository to a remote server, add the server to be able to push to it
```
git remote add origin <server>
```
List all currently configured remote repositories
```
git remote -v
```
- Stash
Temporarily save the changes not committed on a stack, usually occured before fetching latest changes on the remote server
```
git stash
```
Bring back the saved changes onto the working directory, and remove them from the stack at the same time
```
git stash pop
```
- Branches
Create a new branch and switch to it
```
git checkout -b <branch_name>
```
Switch from one branch to another
```
git checkout <branch_name>
```
List all the branches in your repo, and also tell you what branch you're currently in
```
git branch
```
Delete the feature branch
```
git branch -d <branch_name>
```
Push the branch to your remote repository, so others can use it
```
git push origin <branch_name>
```
Push all branches to your remote repository
```
git push -all origin
```
Delete a branch on your remote repository
```
git push origin :<branch_name>
```
- Update from the remote repository
Fetch and merge changes on the remote server to your working directory
```
git pull
```
To merge a different branch into your active branch
```
git merge <branch_name>
```
View all the merge conflicts
```
git diff
```
View the conflicts against the base file
```
git diff --base <file_name>
```
Preview changes, before merging
```
git diff <source_branch> <target_branch>
```
After you have manually resolved any conflicts, you mark the changed file
```
git add <file_name>
```
- Tags
You can use tagging to mark a significant changeset, such as a release
```
git tag 1.0.0 <commit_id>
```
CommitId is the leading characters of the changeset ID, up to 10, but must be unique. Get the ID using
```
git log
```
Push all tags to remote repository
```
git push --tags origin
```
- Undo local changes
If you mess up, you can replace the changes in your working tree with the last content in head. Changes already added to the index, as well as new files, will be kept
```
git checkout -- <file_name>
```
Instead, to drop all your local changes and commits, fetch the latest history from the server and point your local master branch at it, do this
```
git fetch origin
git reset --hard oringin/master
```
- Search
Search the working directory for foo()
```
git grep "foo()"
```