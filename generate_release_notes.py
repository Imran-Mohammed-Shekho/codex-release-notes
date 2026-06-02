#!/usr/bin/env python3
"""
Codex Release Note Generator
Uses OpenAI GPT-4 to convert git commit history into professional release notes.
"""

import subprocess
import sys
import os
from datetime import datetime
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_last_tag():
    """Get the most recent git tag"""
    try:
        tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
        return tag
    except subprocess.CalledProcessError:
        return None

def get_commits_since_tag(tag):
    """Get commit messages since the last tag"""
    if tag:
        cmd = ["git", "log", f"{tag}..HEAD", "--oneline", "--pretty=format:- %s"]
    else:
        cmd = ["git", "log", "--oneline", "--pretty=format:- %s"]
    
    commits = subprocess.check_output(cmd, text=True).strip()
    return commits if commits else "No new commits since last tag."

def generate_release_notes(commits, version):
    """Use Codex to generate release notes from commits"""
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
        model="gpt-4o",  # Codex uses GPT-4o backend
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )
    
    return response.choices[0].message.content

def main():
    print("🔍 Codex Release Note Generator")
    print("-" * 40)
    
    # Check for API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("❌ ERROR: OPENAI_API_KEY environment variable not set")
        print("   Export it: export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)
    
    # Get last tag
    last_tag = get_last_tag()
    if last_tag:
        print(f"📌 Last tag: {last_tag}")
    else:
        print("📌 No previous tags found. Using all commits.")
    
    # Get commits
    commits = get_commits_since_tag(last_tag)
    print(f"📝 Found {len(commits.split(chr(10)))} commit lines")
    
    # Determine next version
    if last_tag:
        # Simple version bump (patch)
        parts = last_tag.lstrip('v').split('.')
        if len(parts) == 3:
            parts[2] = str(int(parts[2]) + 1)
            next_version = 'v' + '.'.join(parts)
        else:
            next_version = 'v1.0.1'
    else:
        next_version = 'v1.0.0'
    
    print(f"🏷️  Generating notes for: {next_version}")
    print("🤖 Calling Codex API...")
    
    # Generate notes
    try:
        notes = generate_release_notes(commits, next_version)
        
        # Save to file
        output_file = f"RELEASE_NOTES_{next_version}.md"
        with open(output_file, 'w') as f:
            f.write(notes)
        
        print(f"✅ Success! Release notes saved to: {output_file}")
        print("\n" + "="*50)
        print("PREVIEW:")
        print("="*50)
        print(notes[:800] + ("..." if len(notes) > 800 else ""))
        
    except Exception as e:
        print(f"❌ API Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
