---
description: Review friends' report requests from the website and run the ones I pick
---

Help me work through the report requests friends sent from request.html. Use the queue tools (`list_pending`, `get_request`, `list_recent`, `mark_done`, `decline`): on my computer they come from the `research-queue` server, in a cloud session from `research-queue-cloud`. I decide what gets researched: never start a skill for a request I have not picked, either in this session or in the Inbox on the site.

1. Call `list_pending`. If nothing is waiting, say so in one line and stop.

2. Requests with `picked_at` set were already picked by me in the Inbox. If there are any, ask one AskUserQuestion question: "Run the N requests you picked?" with the options **Run the picked ones** and **Let me choose**. Show their topics in the option description. If I choose to run them, go to step 4 with those and leave the rest waiting.

3. Otherwise ask which to run, using the AskUserQuestion tool with `multiSelect: true`. One option per request, oldest first:
   - label: the topic (shorten to a few words if needed)
   - description: `#<id> · <requested_by> · <skill or "my choice"> · <date>` plus the first part of their note, if any
   Each question holds at most 4 options. If more than 4 are waiting, ask about the oldest 4 first, then the next 4 in a second question.
   Then, in one more question, ask what to do with the ones I did not pick: leave them waiting (default), or decline them. For any I decline, ask for a short reply to the friend (offer "Not something I research" as a suggestion) and call `decline` with it.

4. For each request to run, one at a time:
   - Say which command you will run, e.g. `/investment-research Nvidia (answer in English)`. If the friend chose no report type, suggest one from commands.html that fits their topic and note, preferring the lighter ones, and ask me to confirm.
   - Warn me first if the command is marked "Very high" usage on commands.html, and suggest running it in a fresh session.
   - Run it, then add the result to this site as described in the README under "Adding a report" (card, `python tools/make_pdf.py`).
     - **On my computer**: run it the way I normally do.
     - **In a cloud session** (the environment variable `CLAUDE_CODE_REMOTE` is `true`): the ai-berkshire commands are installed, and the framework itself is at `~/ai-berkshire`. Its skills refer to helper scripts as `tools/…`; run those from `~/ai-berkshire`, not from this repo, whose own `tools/` holds the site scripts.
   - Show me the verdict and the report's `id`.
   - **Publishing**: on my computer, ask before you commit and push to `main`. In a cloud session, never push to `main`: commit to a new branch, push it, open a pull request, give me its link, and ask me to merge it (the GitHub app works on the phone). The site updates a minute after the merge.
   - Only after the push to `main`, or after I say the pull request is merged, call `mark_done` with the request id and the report `id`. Add a one-line `reply` only if I give you one.

5. Finish with a short summary: done, declined, still waiting.
