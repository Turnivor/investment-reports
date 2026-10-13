---
description: Review friends' report requests from the website and run the ones I pick
---

Help me work through the report requests friends sent from request.html. Use the `research-queue` MCP tools. I decide what gets researched: never start a skill for a request I have not picked in this session.

1. Call `list_pending`. If nothing is waiting, say so in one line and stop.

2. Ask me which to run, using the AskUserQuestion tool with `multiSelect: true`. One option per request, oldest first:
   - label: the topic (shorten to a few words if needed)
   - description: `#<id> · <requested_by> · <skill or "my choice"> · <date>` plus the first part of their note, if any
   Each question holds at most 4 options. If more than 4 are waiting, ask about the oldest 4 first, then the next 4 in a second question.

3. For the requests I did not pick, ask in one AskUserQuestion question what to do with them: leave them waiting (default), or decline them. For any I decline, ask for a short reply to the friend (offer "Not something I research" as a suggestion) and call `decline` with it.

4. For each request I picked, one at a time:
   - Say which command you will run, e.g. `/investment-research Nvidia (answer in English)`. If the friend chose no report type, suggest one from commands.html that fits their topic and note, preferring the lighter ones, and ask me to confirm.
   - Warn me first if the command is marked "Very high" usage on commands.html, and suggest running it in a fresh session.
   - Run it the way I normally do, then add the result to this site as described in the README under "Adding a report" (card, `python tools/make_pdf.py`).
   - Show me the verdict and the report's `id`, and ask before you commit and push.
   - After the push, call `mark_done` with the request id and the report `id`. Add a one-line `reply` only if I give you one.

5. Finish with a short summary: done, declined, still waiting.
