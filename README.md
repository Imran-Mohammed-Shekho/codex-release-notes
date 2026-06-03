# 🚀 Codex Release Note Generator

Codex Release Note Generator is an AI-powered tool designed to automate the creation of professional, user-friendly release notes from your Git commit history. By leveraging OpenAI's powerful language models, it translates technical commit messages into readable highlights that your users will actually enjoy reading.

## ✨ Features

- **AI-Powered Summarization:** Uses GPT-4o (Codex) to transform messy commit logs into structured release notes.
- **Categorized Highlights:** Automatically groups changes into New Features, Bug Fixes, Documentation, and Maintenance.
- **Git Integration:** Automatically detects your latest tag and fetches all commits since the last release.
- **Mock Mode:** Test the full workflow without an API key or even a Git repository.
- **Markdown Ready:** Generates `.md` files perfect for GitHub Releases or internal documentation.

## 🛠️ How it Works

The script follows a simple process:
1. Identifies the latest Git tag (e.g., `v1.0.0`).
2. Collects all commit messages since that tag.
3. Sends those messages to OpenAI with a specialized prompt.
4. Saves a beautifully formatted `RELEASE_NOTES_vX.X.X.md` file.

---

## 📖 Essential Guides

If you are a beginner, start here:
- **[🐣 Beginner's Setup Guide](SETUP_GUIDE.md):** How to install Python, Git, and push this code to GitHub.
- **[🛡️ Contingency Plan](CONTINGENCY_PLAN.md):** What to do if you can't get an API key or run into errors.

---

## 🚀 Getting Started (No API Key Required)

You can run this tool right now in **Mock Mode** to see how it works without spending a cent or setting up an account.

### 1. Prerequisites
Ensure you have Python installed. (See the [Setup Guide](SETUP_GUIDE.md) if you don't). You can check by running:
```bash
python --version
```

### 2. Download and Run
```bash
# Clone the repository (or just download the script)
git clone https://github.com/Imran-Mohammed-Shekho/codex-release-notes.git
cd codex-release-notes

# Run in Mock Mode (Default)
python generate_release_notes.py
```
This will generate a sample `RELEASE_NOTES_v1.0.0.md` file in your directory.

---

## 🤖 Enabling Real Mode (OpenAI API)

When you're ready to use it on your actual projects, follow these steps:

### 1. Get an OpenAI API Key
1. Go to [platform.openai.com](https://platform.openai.com/).
2. Create an account and navigate to the "API Keys" section.
3. Generate a new Secret Key.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the Script
Open `generate_release_notes.py` in a text editor and change these lines:
```python
# Set MOCK_MODE to False to use the real OpenAI API
MOCK_MODE = False

# Add your key here
OPENAI_API_KEY = "your-actual-api-key-here"
```

### 4. Run it!
```bash
python generate_release_notes.py
```

---

## 🏆 Codex for Open Source Program

This project is a prime candidate for OpenAI's **Codex for Open Source** program because:

1. **High Impact for Maintainers:** Writing release notes is a tedious manual task. This tool saves maintainers hours of work by automating the most boring part of releasing software.
2. **Promotes Better Documentation:** By making it easy to generate notes, more projects will provide clear, user-facing changelogs.
3. **Showcases LLM Capabilities:** It demonstrates a practical, high-value application of Large Language Models in the developer toolchain.
4. **Accessible to All:** With its "Mock Mode" and clear instructions, it lowers the barrier for developers to start integrating AI into their workflows.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
