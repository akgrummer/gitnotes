to add a branch that points to the upstream main (that can be accessed on my machine) use:
(this is after the upstream "remote" has already been added as a remote repository)
`git checkout -b main upstream/main`

to switch to another branch use:
`git switch <branchName>`
to see all of the information:
`git branch -a -v`

to grab a file from another branch:
(run from the branch you wan the file to end up)
`git checkout otherbranch myfile.txt`
https://stackoverflow.com/a/307872/9042976