## 🚀 New Features
- Add support for custom OpenAI API endpoints
- Release notes now include a "How to Test" section automatically
- Added `--version` flag to print current tool version

## 🐛 Bug Fixes
- Fix crash when git repository has no tags
- Fix Markdown formatting for bullet points with special characters

## 📚 Documentation
- Update README with GitHub Actions badge example
- Add troubleshooting section for common API key errors

## 🔧 Maintenance
- Bump openai dependency to v1.0.0
- Add pre-commit hook configuration

## 🧪 How to Test
1. Run `python generate_release_notes.py` on a repository with 5+ commits since last tag
2. Verify output contains all four sections (Features, Fixes, Docs, Maintenance)
3. Check that the "How to Test" section has 2-3 actionable bullet points
