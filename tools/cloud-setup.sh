#!/bin/bash
# Setup script for the Claude Code cloud environment that runs /queue from the phone.
# Paste this whole file into the environment's "Setup script" box at claude.ai/code (FRIENDS-SETUP.md, step 9).
# It runs once per environment (then cached) before Claude starts: it installs the ai-berkshire research
# commands and their helper scripts, and Google Chrome, which tools/make_pdf.py uses for the report PDFs.

git clone --depth 1 https://github.com/xbtlin/ai-berkshire.git "$HOME/ai-berkshire" 2>/dev/null \
  || git -C "$HOME/ai-berkshire" pull --ff-only 2>/dev/null || true
mkdir -p "$HOME/.claude/commands"
cp "$HOME/ai-berkshire/skills/"*.md "$HOME/.claude/commands/" 2>/dev/null || true

if ! command -v google-chrome >/dev/null 2>&1; then
  curl -fsSL -o /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y -q /tmp/chrome.deb >/dev/null 2>&1 || true
fi
exit 0
