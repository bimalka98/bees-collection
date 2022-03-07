# [git revert Commit](https://www.freecodecamp.org/news/git-revert-commit-how-to-undo-the-last-commit/) 

1. to reset to the last commit and also remove all unstaged changes     `git reset --hard HEAD~1`, instead of `HEAD~1`  SHA of the commit can also be used.
2. to change the origin execute `git push -f origin main` after the above command

# [Track a new remote branch created on GitHub](https://stackoverflow.com/questions/11262703/track-a-new-remote-branch-created-on-github)

If you don't have an existing local branch, it is truly as simple as:

```
git fetch
git checkout <remote-branch-name>
```
