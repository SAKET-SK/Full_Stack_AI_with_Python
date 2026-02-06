### Chapter 2: Git init and hidden folders

## Basic Commmand

```bash
git init
```

git init creates a hidden .git directory that contains all metadata, history, configuration, and references required for Git to function.

If you just execute the ls command, you will not see the hidden folders, to view the hidden folders, you need to execute ls -la. This way you can view all the hidden folders.

If .git exists -> Git exists in that folder, and the folder is trackable i.e it tracks the changes.

If .git is not present -> The folder is non-trackable

---

## Practical Walkthrough

Step 1: Create a normal folder

```
mkdir git-demo
cd git-demo
```

At this point:

This is just a normal directory. Git has no idea this folder exists

Check:

```
git status
```


Output:

```
fatal: not a git repository
```

Step 2: Initialize Git
```
git init
```


Output (typical):

```
Initialized empty Git repository in .../git-demo/.git/
```

My Terminal Dump 

```

saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab
$ source C:/Users/saket.khopkar/anaconda3/Scripts/activate base
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab
$ cd Git
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git
$ mkdir second_folder third_folder
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git
$ ls
first_folder/  second_folder/  third_folder/
(base) 
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git
$ git --version
git version 2.42.0.windows.1
(base) 
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git
$ cd first_folder
(base) 
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder
$ git -init
unknown option: -init
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]
(base) 
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder
$ git init
Initialized empty Git repository in D:/gen_ai-lab/Git/first_folder/.git/
(base) 
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder (master)
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
(base) 
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder (master)
$ cd ..
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder (master)
$ cd ..
$ cd ..
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git
$ cd first_folder
(base)
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder (master)
$ ls -la
total 4
drwxr-xr-x 1 saket.khopkar 197121 0 Feb  5 11:39 ./
drwxr-xr-x 1 saket.khopkar 197121 0 Feb  5 10:44 ../
drwxr-xr-x 1 saket.khopkar 197121 0 Feb  5 11:39 .git/
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder (master)
$ cd .git
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder/.git (GIT_DIR!)
$ ls
config  description  HEAD  hooks/  info/  objects/  refs/
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder/.git (GIT_DIR!)
$ cd ..
(base)
saket.khopkar@DESKTOP-HOCCP1V MINGW64 /d/gen_ai-lab/Git/first_folder (master)
$

```

Git did one thing only; Created a .git directory

Step 3: Verify Hidden Folder Exists (Windows)

```
ls -la
```


You will now see the hidden .git folder

---

## What is in .git ?

Think of .git as Git’s database + memory + rulebook.

Inside .git, you’ll find (conceptually):

```
.git/
│
├── HEAD
├── config
├── objects/
├── refs/
├── hooks/
└── index
```

- HEAD : Points to the current branch; basically tells the git where it is. “HEAD is a reference to the currently checked-out branch or commit.”
- config : It is repository specific configuration which overrides the global config
- objects/ (folder) : Stores commit, files and trees. Stored in Compressed, Hashed and in immutable format. “Git stores data as objects addressed by SHA-1 hashes.”
- refs/ (folder) : Contains Branch Pointers, Tags and Remote References
- index (Staging Area) : This tracks what changed; its a binary "file" not a folder.

## Practical: Prove Git Exists Without Commits

Create a file:

```
echo "Hello Git" > file.txt
```

Check status:

```
git status
```

Output:

```
On branch main
Untracked files:
  file.txt
```

Empty Repository ≠ No Repository

After git init:

Repo is valid and History is empty ; Also Branch exists (usually main) and mainly .git exists

Interview answer:

“An empty Git repository means no commits yet, not that Git is uninitialized.”

---

## What Happens If You Delete .git?

```
rm -rf .git
```

```
Result:

All history: gone

All branches: gone

Commits: gone

Files: still there
```

Interview killer line:

“Deleting the .git folder removes all version control metadata but leaves working files intact.”

---

## Questions for Interview (CheatSheet)

Q1: What does git init do?

It initializes a new Git repository by creating a .git directory that stores all version control metadata.

Q2: What is stored in the .git folder?

Commits, branches, configuration, references, and the staging index.

Q3: Is .git part of the project source code?

No. It’s Git’s internal metadata and is usually hidden.

Key thing to remember : 

```
No .git → No Git
.git exists → Git controls everything
```
