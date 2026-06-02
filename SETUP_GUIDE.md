# 🐣 Beginner's Setup Guide

This guide will take you from "zero to hero" – even if you've never used a terminal or written a line of code before.

## 1. Install Your Tools

### Step 1: Install Python
Python is the language that runs our script.
- **Windows:** Go to [python.org](https://www.python.org/downloads/windows/), download the "Stable Release" installer, and **CRITICAL:** Check the box that says **"Add Python to PATH"** before clicking Install.
- **Mac:** Open "Terminal" (search for it in Spotlight) and type `brew install python` (requires Homebrew) or download from [python.org](https://www.python.org/downloads/macos/).

### Step 2: Install Git
Git is a tool that tracks changes in your code and lets you upload it to GitHub.
- **Windows:** Download and install [Git for Windows](https://git-scm.com/download/win).
- **Mac:** Type `git --version` in Terminal. If it's not there, it will prompt you to install "Xcode Command Line Tools."

---

## 2. Create Your GitHub Repository

1. Log in to [GitHub](https://github.com/).
2. Click the **+** icon in the top right and select **New repository**.
3. Name it `codex-release-notes`.
4. Set it to **Public**.
5. Do **NOT** initialize with a README, License, or Gitignore (we already have them!).
6. Click **Create repository**.

---

## 3. Push the Code to GitHub

Open your terminal (Command Prompt on Windows, Terminal on Mac) and run these commands one by one:

```bash
# 1. Create a folder on your computer
mkdir codex-project
cd codex-project

# 2. [PASTE ALL THE FILES I GENERATED INTO THIS FOLDER]

# 3. Initialize Git
git init

# 4. Add the files
git add .

# 5. Save the changes
git commit -m "Initial commit: AI Release Note Generator"

# 6. Link to GitHub (REPLACE 'your-username' with your actual GitHub name)
git branch -M main
git remote add origin https://github.com/your-username/codex-release-notes.git

# 7. Upload!
git push -u origin main
```

---

## 4. Test the Mock Version Locally

In the same terminal window, run:
```bash
python generate_release_notes.py
```
You should see a message saying "Success!" and a new file named `RELEASE_NOTES_v1.0.0.md` will appear in your folder. Open it to see the result!

---

## 5. Get an OpenAI API Key

Even if you don't have one now, here is how you get it for free (OpenAI usually gives $5 in trial credits):
1. Go to [platform.openai.com](https://platform.openai.com/signup).
2. Sign up.
3. Click on the "API Keys" tab on the left sidebar.
4. Click **+ Create new secret key**.
5. **Copy it immediately** – you won't see it again!

---

## 6. Switch to "Real Mode"

1. Open `generate_release_notes.py` in Notepad or TextEdit.
2. Find line 15: `MOCK_MODE = True`. Change it to `MOCK_MODE = False`.
3. Find line 19: `OPENAI_API_KEY = "YOUR_API_KEY_HERE"`. Paste your key inside the quotes.
4. Install the "OpenAI" helper: `pip install openai`.
5. Run the script again: `python generate_release_notes.py`.

---

## 7. Submit Your Application

1. Open `application_form_text.txt`.
2. Go to the OpenAI Codex for Open Source application page.
3. Copy and paste each section from the text file into the form.
4. **Celebrate!** You've just submitted a professional AI project.
