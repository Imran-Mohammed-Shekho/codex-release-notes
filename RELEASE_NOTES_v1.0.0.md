# Release Notes - v1.0.0 (2026-06-02)

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
- Verify that `RELEASE_NOTES_v1.0.0.md` is created in the current directory.
