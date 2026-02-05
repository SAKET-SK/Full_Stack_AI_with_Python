## Chapter 1: Introduction to Git

Git = Version Control. 

It is like a checkpoint in a video game, where you store the progress. If anything goes wrong, you may restart it from there.

---

### What problem does Git solve?

Before Git, teams faced 3 massive problems:

<b>Problem 1: No history you can trust</b>

Files were saved as:

```
final.doc
final_v2.doc
final_v3_REAL_FINAL.doc
```

No way to know, Who changed what, When and Why

<b>Problem 2: Collaboration chaos</b>

Two developers editing the same file → overwrites

There was No conflict detection Nor accountability

<b>Problem 3: Central point of failure</b>

Older systems (like SVN):

One central server, if goes Server down = work stops; No offline work

Git was created to solve all three, permanently.

---

### What is Git

Git = Distributed Version Control System

A Version control system consistently tracks changes to your files over the period of time. The word "Distributed" is a game changer, which simply means Every developer has:

- Full copy of the repository
- Full history
- Full branches
- Full commits

There is no single point of failure.

Interview gold line: “In Git, every clone is a complete repository, not just a working copy.”

---

### Difference between Git and GitHub

“Git is the version control system, while GitHub is a remote repository hosting service built on top of Git.”

---

### Git's Internal Thinking

Git does NOT track files. Instead Git tracks snapshots, not differences.

Every commit is a snapshot of the entire project and most importantly every commit is linked to previous snapshots. This makes Git extremely fast and reliable

---

### Core Areas of git

```
WORKING DIRECTORY -----git add----- STAGING AREA -----git commit----- REPOSITORY -----git push----- GITHUB
```

<b>Working Directory</b> is your actual file and where you write code. It also contains changes which are not tracked yet.

<b>Staging Area</b> (Index) is a preparation area. You choose what goes into the next commit. This is Git’s secret weapon

<b>Repository</b> (.git folder)

Basically contains:
- All commits
- All history
- All branches
- Entire project memory

Git allows you to:
- Work offline
- Experiment safely using branches
- Roll back bad changes instantly
- Collaborate without stepping on each other
- Review code via history and diffs

This is why every serious engineering team uses Git.

---

### Git origins

Git was created by Linus Torvalds in 2005.

Why?
Linux kernel development and Existing tools were:
- Slow
- Centralized
- Paid / restrictive

Design goals:
- Speed
- Simplicity
- Distributed
- Integrity (cryptographic hashing)

Bonus interview line: “Git uses SHA-1 hashes to ensure the integrity of commits.”

---

### High-level flow:

```
→ Stage changes
→ Commit
→ Push to remote
→ Create PR
→ Review
→ Merge
```

---

### Interview Bonus

Q1: What is Git?

Ans: Git is a distributed version control system that tracks snapshots of a project and allows multiple developers to collaborate efficiently with full history available locally.

Q2: What does “distributed” mean in Git?

Ans: Each developer has a full copy of the repository, including history and branches, allowing offline work and no single point of failure.

Q3: What is the staging area?

Ans: It is an intermediate area where changes are prepared before being committed, allowing granular control over commits.


