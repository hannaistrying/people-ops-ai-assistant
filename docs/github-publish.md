# Publish to GitHub

Target repository: `https://github.com/hannaistrying/people-ops-ai-assistant`

1. Keep the repository **private** until you finish the privacy review.
2. Download and unzip `people-ops-ai-assistant-github-ready.zip`.
3. Open your repository on GitHub and select **Add file → Upload files**.
4. Upload the **contents** of the extracted `people-ops-ai-assistant` folder (not the folder itself), preserving subdirectories.
5. Review every filename and commit the changes. Do not upload internal exports, actual workplace messages, private screenshots, or secrets.
6. Check README links and run `python -m unittest discover -s tests -v` locally if available.
7. Make the repository public only after inspecting files **and commit history**. Deleted files remain in history.

If the GitHub web interface doesn't preserve the folder structure for your upload, use GitHub Desktop or git instead:

```bash
git init
git add .
git commit -m "Initial People Ops AI Assistant starter kit"
git branch -M main
git remote add origin https://github.com/hannaistrying/people-ops-ai-assistant.git
git push -u origin main
```

The repository must already exist, and authentication is required.
