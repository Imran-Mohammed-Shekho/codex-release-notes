# Contributing to Codex Release Note Generator

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Our Process

We use GitHub to track bugs and features. If you want to contribute code, please:

1. **Fork the repository** and create your branch from `main`.
2. **Install dependencies**: `pip install -r requirements.txt`.
3. **Write code!** If you've added code that should be tested, add tests.
4. **Run the script** in Mock Mode to ensure basic functionality isn't broken.
5. **Issue a Pull Request**.

## Mock Mode Development

To make it easy for everyone to contribute (even those without an OpenAI API key), we have a `MOCK_MODE` in `generate_release_notes.py`.

- When working on UI or logic that doesn't involve the LLM prompt, keep `MOCK_MODE = True`.
- If you are improving the AI prompt, please provide example outputs in your PR.

## Code of Conduct

Please be respectful and helpful in all interactions. We aim to build a welcoming community for developers of all skill levels.

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
