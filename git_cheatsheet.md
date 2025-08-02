# 🧾 Git Command Cheat Sheet

A quick reference to essential Git commands used for version control and collaboration.

---

## 🔧 Initialize & Clone

```bash
git init                   # Initialize a new Git repository
git clone <repo-url>       # Clone an existing repository
```

---

## 📁 Track & Commit Changes

```bash
git status                 # Show current status of changes
git add .                  # Stage all changes for commit
git commit -m "message"    # Commit staged changes with a message
```

---

## 🚀 Push & Pull

```bash
git remote add origin <ssh-url>   # Add remote repository
git push -u origin main           # Push commits to GitHub
git pull                          # Pull latest changes from remote
```

---

## 🌿 Branching & Merging

```bash
git branch                        # List all branches
git checkout -b new-feature       # Create and switch to a new branch
git checkout main                 # Switch back to main branch
git merge new-feature             # Merge branch into main
```

---

## 🧠 Undo & Fix Mistakes

```bash
git log                           # View commit history
git reset --hard HEAD^           # Undo the last commit
git revert <commit-hash>         # Revert a specific commit
git stash                         # Temporarily save changes
git stash pop                     # Reapply stashed changes
```

---

## 🔐 SSH Setup for GitHub

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"     # Generate SSH key
# Add the public key to GitHub (Settings > SSH and GPG keys)
git clone git@github.com:username/repo.git            # Clone using SSH
```

---

✅ Keep this file in your repository as internal documentation for future reference.