# 🛡️ Contingency Plan: What if things go wrong?

Software development rarely goes perfectly. Here is how to handle common roadblocks.

## 1. "I can't get an OpenAI API Key"
If you are waitlisted, in a restricted region, or can't access OpenAI:

- **Alternative 1: Anthropic (Claude)**
  - Claude is an excellent alternative. You can get an API key at [console.anthropic.com](https://console.anthropic.com/).
  - To use it, you'd just need to swap the `openai` library for `anthropic`.
- **Alternative 2: Google (Gemini)**
  - Google offers a very generous free tier for Gemini Pro. Get a key at [aistudio.google.com](https://aistudio.google.com/).
- **Alternative 3: Local Models (Ollama)**
  - If you want to run AI entirely on your own computer (no internet/key needed), install [Ollama](https://ollama.com/).
  - You can change the script to talk to `localhost:11434` instead of OpenAI.

## 2. "I don't have enough GitHub Stars"
The Codex program often looks for "active" projects.
- **Value over Stars:** In your application, emphasize the **utility** of the tool. Explain that it's a new project specifically designed to solve a problem you've observed in the community.
- **Show, Don't Tell:** Use the "Mock Mode" output to show what the tool *can* do. Even with 0 stars, a repository that has a clean README, a LICENSE, and GitHub Actions (which we included!) looks professional.

## 3. "The script crashes with a 'ModuleNotFoundError'"
- This usually means you haven't installed the `openai` library.
- **Fix:** Run `pip install openai` in your terminal.
- If it says `pip` is not recognized, try `python -m pip install openai`.

## 4. "Git says 'Permission Denied'"
- This happens if your GitHub login isn't set up in your terminal.
- **Fix:** Use the [GitHub Desktop](https://desktop.github.com/) app. It's much easier for beginners. You can just drag and drop your folder into the app and click "Publish."

## 5. How to demonstrate value without a Live API Call
If you can't get a key in time for the deadline:
1. **Focus on the Mock Mode:** Your repository still shows your ability to architect a tool, handle errors, and provide fallbacks.
2. **Provide "Golden" Examples:** In your repository, create a folder called `examples/` and put several pre-generated release notes there. This proves the tool works even if the reviewer doesn't run it themselves.
