# Friends-only site and report requests

This turns the site into a private one for friends, with a page where they can ask for reports.
Research still runs only on your own computer, in Claude Code, when you decide to run it.

```
 friends ──sign in──▶ Cloudflare Access ──▶ the site (Cloudflare Pages, from this repo)
                                             └─ request.html ──▶ /api/requests ──▶ D1 database (the queue)
 you ── Claude Code ── /queue ── tools/queue_mcp.py ─────────────────────────────▶ same D1 database
```

| Piece | Where it lives | Cost |
|---|---|---|
| The site, `request.html`, the API in `functions/` | this repo, published by Cloudflare Pages | free |
| Sign-in (email code, or Google) and the friends list | Cloudflare Zero Trust → Access | free up to 50 users; asks for a card, charges nothing |
| The request queue | Cloudflare D1 | free |
| `/queue` and `tools/queue_mcp.py` | your computer, with Claude Code | your Claude plan |

Nothing secret is stored in this repo. The two secrets (a Cloudflare API token, and optionally a GitHub token) live in Cloudflare's settings and in your local Claude Code settings.

---

## 1. Cloudflare account

Create one at dash.cloudflare.com. If someone else sets this up for you, see **Handing it over** at the end.

## 2. The queue database

1. **Storage & Databases → D1 → Create**. Name it `investment-requests`.
2. Open it → **Console**, paste the contents of [`db/schema.sql`](db/schema.sql), run it.
3. Note the **Database ID** (shown on the database page). You need it in step 6.

## 3. Publish the site with Cloudflare Pages

1. **Workers & Pages → Create → Pages → Import an existing Git repository**. If it offers a Worker first, look for the Pages option.
2. Connect GitHub and pick `Turnivor/investment-reports`. **This needs the repo owner's GitHub account**, because it installs Cloudflare's GitHub app on the repo.
3. Build settings: framework preset **None**, build command **empty**, build output directory **`/`** (the repo root, where `index.html` is). Production branch `main`.
4. Deploy. The site appears at `https://<project>.pages.dev`. From now on every push to `main` republishes it, including the daily price update.
5. Project → **Settings → Bindings → Add → D1 database**: variable name **`DB`**, database `investment-requests`.

The site works now but is still open to everyone. The request page will say the login is not set up yet: that is expected until step 4.

## 4. Lock it to friends with Cloudflare Access

1. Open **Zero Trust** from the dashboard. Pick a team name (e.g. `turnivor`) and the **Free** plan. It asks for a payment card but does not charge on the Free plan.
2. Back in the Pages project: **Settings → General → Enable access policy**. This protects preview addresses only, so widen it to the main address too (Cloudflare's own steps, from their "Pages known issues" page):
   1. Select **Manage** on the new policy. In **Access → Applications**, open the project's application → **Configure**.
   2. Under **Public hostname**, delete the `*` in **Subdomain** and **Save** (rename the application if it complains about a duplicate name).
   3. Go back to the Pages project → **Settings → General** and select **Enable access policy** again, so previews are protected too.
   4. You now have two Access applications: `<project>.pages.dev` and `*.<project>.pages.dev`.
3. Open the `<project>.pages.dev` application → **Policies**. Edit the policy (or add one): **Action: Allow**, **Include → Emails**: your own email and each friend's. Session duration: 1 month is comfortable.
4. **Zero Trust → Settings → Authentication**: **One-time PIN** should be on. Friends type their email and get a code; no account needed. You can add **Google** as a login method too if you like.
5. Copy two values into the Pages project → **Settings → Variables and secrets** (type: text), then **redeploy** (Deployments → latest → Retry deployment):
   - `ACCESS_TEAM_DOMAIN`: `<team>.cloudflareaccess.com` (shown under Zero Trust → Settings → Team name)
   - `ACCESS_AUD`: the **Application Audience (AUD) Tag** of the `<project>.pages.dev` application (on its overview / basic information). To let the request page work on preview addresses too, add the preview application's tag after a comma.

**Check it:** open the site in a private window. You should get the Cloudflare sign-in, a code by email, then the site. Send a test request on the Request page and see it under **D1 → Console** with `SELECT * FROM requests;`.

To add or remove a friend later: edit the email list in step 4.3. That is all.

## 5. Make the GitHub repo private

Only after step 4 works:

1. GitHub → repo **Settings → General → Danger zone → Change visibility → Private**.
2. **Settings → Pages**: make sure the old `turnivor.github.io/investment-reports` site is gone (unpublish it if it is still there).

The daily price Action keeps running: private repos get a monthly allowance of free Action minutes and this job uses about a minute a day. Reports published while the repo was public may already have been copied; going private protects everything from now on.

Small side effect: link previews (the `og.png` card when the link is pasted in a chat) stop working, because the preview bots cannot sign in.

## 6. The queue on your computer

1. Cloudflare → **My Profile → API Tokens → Create token → Custom token**. Permission: **Account · D1 · Edit**, limited to this account. Copy the token.
2. Your **Account ID** is on the Workers & Pages overview page (right side).
3. In a terminal:

   ```bash
   pip install "mcp[cli]"
   claude mcp add --scope user research-queue \
     -e CLOUDFLARE_ACCOUNT_ID=<account id> \
     -e CLOUDFLARE_D1_ID=<database id from step 2> \
     -e CLOUDFLARE_API_TOKEN=<token> \
     -- python3 /full/path/to/investment-reports/tools/queue_mcp.py
   cp /full/path/to/investment-reports/.claude/commands/queue.md ~/.claude/commands/
   ```

   `--scope user` and the copy make `/queue` work in any folder, including the ai-berkshire one where you run the research. The token is kept in your local Claude Code settings, not in the repo.
4. In Claude Code, type **`/queue`**. Claude lists the waiting requests as tick boxes, asks what to do with the rest, runs only what you pick, adds the report to the site the usual way, and after you push, marks the request done so the friend gets a link. The first time, Claude Code asks permission to use the queue tools: choose to always allow.

## 7. Optional: an email when a request arrives

The site can open a GitHub issue for each new request, and GitHub emails you (the same way the price alerts do).

1. GitHub → **Settings → Developer settings → Fine-grained tokens → Generate**: repository access **only `investment-reports`**, permission **Issues: Read and write**.
2. Pages project → **Settings → Variables and secrets**: add `GITHUB_TOKEN` as a **secret** with that token, and `GITHUB_REPO` = `Turnivor/investment-reports` as text. Redeploy.

Close the issue when you have dealt with the request.

---

## Handing it over

If someone set this up for you in their own accounts:

- **Cloudflare:** they invite you under **Manage account → Members** as **Super Administrator**. You replace their card with yours under **Billing**, then remove them. The site, database and Access settings stay as they are.
- **Cloudflare API token (step 6):** create your own; theirs stops working when they leave the account.
- **GitHub token (step 7):** must be yours, or issues will be opened in their name. Replace the `GITHUB_TOKEN` secret.
- **GitHub repo:** remove them as a collaborator if you like.
- **Friends list:** check the emails in step 4.3.

## Files

| File | What it does |
|---|---|
| [`request.html`](request.html) | The Request page: the form and the friend's own requests with their status and report links |
| [`functions/api/requests.js`](functions/api/requests.js) | The API behind it: list, add, cancel. Friends can only see and cancel their own requests, have at most 3 waiting, and can pick only the lighter report types |
| [`functions/api/_middleware.js`](functions/api/_middleware.js) | Checks the Cloudflare Access sign-in on every API call, so the API stays closed even if Access were misconfigured |
| [`db/schema.sql`](db/schema.sql) | The queue table |
| [`tools/queue_mcp.py`](tools/queue_mcp.py) | Gives Claude Code the queue tools: `list_pending`, `get_request`, `list_recent`, `mark_done`, `decline` |
| [`.claude/commands/queue.md`](.claude/commands/queue.md) | The `/queue` command |
