#!/usr/bin/env python3
"""
Codex Release Note Generator
Uses OpenAI GPT-4 to convert git commit history into professional release notes.
"""

import subprocess
import sys
import os
from datetime import datetime

# ==============================================================================
# CONFIGURATION
# ==============================================================================
# Set MOCK_MODE to True to run without an OpenAI API key.
# Set MOCK_MODE to False to use the real OpenAI API.
MOCK_MODE = True

# Your OpenAI API Key (only needed if MOCK_MODE = False)
# You can also set this as an environment variable: export OPENAI_API_KEY='your-key'
OPENAI_API_KEY = "YOUR_API_KEY_HERE"
# ==============================================================================

def get_last_tag():
    """Get the most recent git tag"""
    try:
        tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
        return tag
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def get_commits_since_tag(tag):
    """Get commit messages since the last tag"""
    try:
        if tag:
            cmd = ["git", "log", f"{tag}..HEAD", "--oneline", "--pretty=format:- %s"]
        else:
            cmd = ["git", "log", "--oneline", "--pretty=format:- %s"]

        commits = subprocess.check_output(cmd, text=True).strip()
        return commits if commits else "No new commits since last tag."
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "- Initial commit\n- Added core functionality\n- Improved UI"

def generate_mock_notes(version):
    """Return realistic but fake release notes"""
    return f"""# Release Notes - {version} ({datetime.now().strftime('%Y-%m-%d')})

## 🚀 New Features
- **Smart Summarization:** Automatically condense dozens of commits into readable highlights using AI.
- **Markdown Export:** Clean, ready-to-paste formatting for GitHub Releases.
- **Tag Auto-Detection:** Automatically finds your last release to determine what's new.

## 🐛 Bug Fixes
- Fixed an issue where tags with special characters caused script failures.
- Resolved a timeout error when processing very large commit histories.

## 📚 Documentation
- Added detailed installation guide to README.
- Included example output in the documentation folder.

## 🧪 How to Test
- Run `python generate_release_notes.py` in your terminal.
- Verify that `RELEASE_NOTES_{version}.md` is created in the current directory.
"""

def generate_release_notes(commits, version):
    """Use Codex to generate release notes from commits"""

    api_key = os.environ.get("OPENAI_API_KEY") or OPENAI_API_KEY

    # Check if we should use MOCK mode
    if MOCK_MODE or not api_key or api_key == "YOUR_API_KEY_HERE":
        if not MOCK_MODE:
            print("⚠️  Warning: API Key not found or still set to placeholder. Falling back to MOCK mode.")
        return generate_mock_notes(version)

    try:
        # Import only when needed to avoid dependency issues in MOCK mode
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a technical writer generating release notes for an open source project.

**Version:** {version}
**Date:** {datetime.now().strftime('%Y-%m-%d')}

**Commits since last release:**
{commits}

Generate release notes with these sections:
## 🚀 New Features
## 🐛 Bug Fixes
## 📚 Documentation
## 🔧 Maintenance
## ⚠️ Breaking Changes (if any)

If a section has no items, omit it.
Keep each bullet point clear and user-focused (not developer jargon).
Add a "## 🧪 How to Test" section with 2-3 bullet points.

Output ONLY valid Markdown. No explanations before or after.
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1000
        )

        return response.choices[0].message.content
    except ImportError:
        print("❌ Error: 'openai' library not installed. Run 'pip install openai'.")
        print("⚠️  Falling back to MOCK mode.")
        return generate_mock_notes(version)
    except Exception as e:
        print(f"❌ API Error: {e}")
        print("⚠️  Falling back to MOCK mode.")
        return generate_mock_notes(version)

def main():
    print("\n🔍 Codex Release Note Generator")
    print("-" * 40)
    
    # Get last tag
    last_tag = get_last_tag()
    if last_tag:
        print(f"📌 Last tag: {last_tag}")
    else:
        print("📌 No previous tags found or not a git repo. Using sample data.")
    
    # Get commits
    commits = get_commits_since_tag(last_tag)
    
    # Determine next version
    if last_tag:
        parts = last_tag.lstrip('v').split('.')
        if len(parts) == 3:
            try:
                parts[2] = str(int(parts[2]) + 1)
                next_version = 'v' + '.'.join(parts)
            except ValueError:
                next_version = 'v1.0.1'
        else:
            next_version = 'v1.0.1'
    else:
        next_version = 'v1.0.0'
    
    print(f"🏷️  Generating notes for: {next_version}")

    if MOCK_MODE:
        print("🎭 Running in MOCK mode (no API key required)...")
    else:
        print("🤖 Calling OpenAI API (Real mode)...")
    
    # Generate notes
    notes = generate_release_notes(commits, next_version)

    # Save to file
    output_file = f"RELEASE_NOTES_{next_version}.md"
    try:
        with open(output_file, 'w') as f:
            f.write(notes)
        print(f"✅ Success! Release notes saved to: {output_file}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

    print("\n" + "="*50)
    print("PREVIEW:")
    print("="*50)
    print(notes[:800] + ("..." if len(notes) > 800 else ""))

if __name__ == "__main__":
    main()
