<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introduction](#introduction)
- [Basics](#basics)
  - [Create project](#create-project)
  - [Branch operations](#branch-operations)
  - [Commit Process](#commit-process)
  - [Revoke change](#revoke-change)
- [Development process for features/bugs](#development-process-for-featuresbugs)
  - [Step1: development](#step1-development)
  - [Step2: send pull request to project owner/leader/manager](#step2-send-pull-request-to-project-ownerleadermanager)
  - [Step3: owner/leader/manager merge to master and delete the created branch](#step3-ownerleadermanager-merge-to-master-and-delete-the-created-branch)
- [How to commit code when cooperate with others](#how-to-commit-code-when-cooperate-with-others)
- [Issues & Solutions](#issues-&-solutions)
- [References:](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

This document introduces the usage of git.

Our team use Git for collaborative development. Git offers GUI tool and command line. In the develop process, we can also use tools like DiffMerge to compare codes before pushing codes to remote repository, this can help prevent wrong commit not wanted.

## Basics
### Create project

- Clone remote project

    ```
    git clone <path_to_repository>
    ```
- Create local project
	
    ```
    cd <path_to_local_root_directory>
    ```
	
    ```
    git init
    ```

### Branch operations

- Fetch all latest branches

    ```
    git fetch
    ```

- List branches

    ```
    git branch
    ```
- Switch branch

    ```
    git checkout <branch_name>
    ```
- Create new branch

    ```
    git checkout -b <branch_name>
    ```
- Delete branch(local/remote)

    ```
    git branch -D <branchName> #Delete local branch
    ```
		
    ```
    git push origin --delete <branchName> #Delete remote branch
    ```
	    
### Configure Host

- TODO

### Commit Process

- Add the files need to be committed

    ```
    git add -A
    ```
- Commit changes

    ```
    git commit -m "#<task_number> - Commit message"
    ```
    
- Push to the remote repository


    ```
    git push origin <branch_name> #	Push commited changes to the new branch of your remote repository.
    ```

### Revoke change

- To restore to the latest submission record：

		git checkout 
		git reset —hard origin/master
    
### Compare changes

- Command line

    ```
    git diff
    ```
- The Third-party tool(GUI): DiffMerge

## Development process for features/bugs

### Step1: development 

1. Create a new branch and switch to it for a concrete task
    
    ```
    git checkout -b <branch_name>
    ```
2. Make changes for your task

3. List the files you've changed and those you still need to add or commit
    
    ```
    git status
    ```
4. Add the files changed(**this command would add all files new or changed, please make sure all that is what you want commit**)
    
    ```
    git add -A
    ```
5. Commit changes to head
    
    ```
    git commit -m "#<task_number> - Commit message"
    ```
6. Push commited changes to the remote repository
    
    ```
    git push origin <branch_name>
    ```

### Step2: send pull request to project owner/leader/manager


Reference link: [Creating a pull request](https://help.github.com/articles/creating-a-pull-request/)

Choose the branch that contains your commits.To the left of the "Branch" menu, click the green Compare and Review button.
![Compare and Review button](https://help.github.com/assets/images/help/pull_requests/pull-request-start-review-button.png)

The Compare page will automatically select the base and compare branches; to change these, click Edit.

Reference link: [Comparing commits across time](https://help.github.com/articles/comparing-commits-across-time/#comparing-branches)

![the base and compare branches](https://help.github.com/assets/images/help/branch/comparing_branches.png)

On the Compare page, click Create pull request. Type a title and description for your pull request. Click Create pull request.
![pull request](https://help.github.com/assets/images/help/pull_requests/pullrequest-send.png)

### Step3: owner/leader/manager merge to master and delete the created branch

Reference link: [Merging a pull request](https://help.github.com/articles/merging-a-pull-request/)

1. Under your repository name, click  Pull requests.
![pull request place](https://help.github.com/assets/images/help/repository/repo-tabs-pull-requests.png)

2. In the "Pull Requests" list, click the pull request you'd like to merge. Click Merge pull request.
![merge pull request](https://help.github.com/assets/images/help/pull_requests/merge_box/pullrequest-mergebutton.png)

3. Type a commit message, or accept the default message. Under the commit message box, click Confirm merge.
![confirm merge](https://help.github.com/assets/images/help/pull_requests/merge_box/pullrequest-confirmmerge.png)

4. [Delete branch](https://help.github.com/articles/deleting-unused-branches/)

	At the bottom of a merged or closed pull request, you’ll see a button to delete the lingering branch:
![delete branch](https://help.github.com/assets/images/help/pull_requests/delete_branch_button.png)


## How to commit code when cooperate with others

1. Pull the latest changes from remote server for this branch before making some changes for your task
 
    ```
    git pull origin <branch_name>
    ```
2. List the files you've changed and those you still need to add or commit after making some changes for your task
    
    ```
    git status
    ```
3. Temporarily save the changes not committed on a stack
    
    ```
    git stash
    ```
4. Pull the latest changes from remote server for this branch
    
    ```
    git pull origin <branch_name>
    ```
5. Bring back the saved changes onto the working directory, and remove them from the stack at the same time
    
    ```
    git stash pop
    ```
6. List the files you've changed and those you still need to add or commit, if conflict try to solve it before add/commit
    
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

## Issues & Solutions
- N/A

## References: 
- [Git Reference](http://gitref.org) - Git
- [Basic Git commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html) - by Atlassian Stash
- [How To Use Git Effectively](https://www.digitalocean.com/community/tutorials/how-to-use-git-effectively) - by Jason Kurtz