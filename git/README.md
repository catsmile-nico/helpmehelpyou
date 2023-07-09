# Commands Collection

## General
| Description                                | Example                                           |
| ------------------------------------------ | ------------------------------------------------- |
| Change prev. commit message                | ```git commit --amend -m "New commit message."``` |
| Undo local changes to file                 | ```git restore filename```                        |
| Undo git add                               | ```git reset```                                   |
| Undo git rm to a file                      | ```git reset{filename}; git restore {filename}``` |
| Undo prev commit (Keep local changes)      | ```git reset --soft HEAD~1```                     |
| Undo prev commit (Including local changes) | ```git reset --hard HEAD~1```                     |

<br>

## Diff
| Description                                 | Example                  |
| ------------------------------------------- | ------------------------ |
| Show number of line, block changes per file | ```git diff --numstat``` |

<br>

## Remote
| Description    | Example                                  |
| -------------- | ---------------------------------------- |
| Get remote url | ```git config --get remote.origin.url``` |

<br>

## Tags
| Description         | Example                                   |
| ------------------- | ----------------------------------------- |
| Add tags            | ```git tag {tagname} {commit_id}```       |
| Push tags to remote | ```git push --tags```                     |
| Rename tags         | ```git tag {new_tagname} {old_tagname}``` |
| Delete tag          | ```git tag -d {tagname}   ```             |
| Delete remote tag   | ```git push --delete origin tagname```    |


<br>

## Misc (Github)
| Description         | Example                                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Deploy Github pages | 1. Settings > General > Repo have to be public<br/> 2. Settings > Pages > Select Source and Branch and Enforce HTTPS <br/> 3. Do fresh commit+push to trigger rebuild which can be checked at {repo}/deploments |