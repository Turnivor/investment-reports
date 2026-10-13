# Friends-only site and report requests: technical setup

The setup notes for whoever builds or maintains this. The site owner's own short guide is separate and only covers his few clicks.

What it does: the site moves from GitHub Pages to Cloudflare Pages, behind a sign-in that only lets in emails on a list. Friends can ask for reports on `request.html`. Research still runs only on the owner's own computer, in Claude Code, when he picks a request with `/queue`.

```
 friends ──sign in──▶ Cloudflare Access ──▶ site on Cloudflare Pages ◀── GitHub Action publishes main
                                             └─ request.html ─▶ /api/requests ─▶ D1 database (the queue)
 owner ── Claude Code ── /queue ── tools/queue_mcp.py ───────────────────────────▶ same D1 database
```

| Piece | Where | Cost |
|---|---|---|
| Site, Request page, API (`functions/`) | this repo, published to Cloudflare Pages by [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) | free |
| Sign-in and the friends list | Cloudflare One (Zero Trust) → Access | free up to 50 users; needs a card on file, charges nothing |
| Google sign-in (optional) | a Google Cloud project's OAuth client | free, no card |
| Request queue | Cloudflare D1 | free |
| `/queue` | the owner's computer, set up once with [`tools/setup-queue.cmd`](tools/setup-queue.cmd) (Windows) or [`tools/setup-queue.command`](tools/setup-queue.command) (Mac) | his Claude plan |

No secret is stored in the repo. Secrets live in GitHub Actions secrets, Cloudflare settings, and the owner's local Claude Code settings.

Names used below (change them consistently if you pick others):

| | |
|---|---|
| Pages project | `officium-advocati-diaboli` (must match `PAGES_PROJECT` in `deploy.yml`) → `https://officium-advocati-diaboli.pages.dev` |
| D1 database | `investment-requests` |
| Access team | `officium-advocati-diaboli` → `officium-advocati-diaboli.cloudflareaccess.com` |

---

## 1. Cloudflare account and Access team

1. Cloudflare account at dash.cloudflare.com.
2. Open **Zero Trust** (Cloudflare One), choose the team name, plan **Free**, add a payment card (not charged). The team name can be changed later under **Settings → Team domain**, but Google sign-in and `ACCESS_TEAM_DOMAIN` must then be updated too.

## 2. Database and Pages project

From any clone of this repo (needs Node.js; `npx wrangler login` once):

```bash
npx wrangler d1 create investment-requests                          # note the database_id it prints
npx wrangler d1 execute investment-requests --remote --file db/schema.sql
npx wrangler pages project create officium-advocati-diaboli --production-branch main
```

If `d1 execute` complains it cannot find the database, run the schema in the dashboard instead: **Storage & Databases → D1 → investment-requests → Console**, paste `db/schema.sql`, run.

The project is a "direct upload" project: GitHub Actions publishes to it (step 5). Cloudflare's own Git connection is not used, because it needs the repo owner's GitHub login, and an upload project cannot be switched to it later anyway.

In the dashboard, **Workers & Pages → officium-advocati-diaboli → Settings**:
- **Bindings → Add → D1 database**: variable name `DB`, database `investment-requests`.
- **Variables and secrets** (production): `ACCESS_TEAM_DOMAIN` and `ACCESS_AUD`, filled in at the end of step 3.

Keep configuration in the dashboard. Never commit a `wrangler.toml`: if one is in the published folder, it replaces the dashboard settings. (A local test `wrangler.toml` is fine if it is listed in `.git/info/exclude`.)

## 3. Lock the site to friends (Cloudflare Access)

All in **Cloudflare One → Access controls**.

1. **Policies → Add a policy**: name `Friends`, action **Allow**, include **Emails** → the owner's email and each friend's. This list is the one place to add or remove people later.
2. **Applications → Create new application → Self-hosted**:
   - Public hostname: **Subdomain empty**, Domain `officium-advocati-diaboli.pages.dev`, Path empty.
   - Policies: `Friends`.
   - Login methods: **One-time PIN** (add Google after step 4). With only one method, turn on **Apply instant authentication** so the method picker is skipped.
   - Session duration: e.g. 1 month, so friends rarely need a new code.
   - Name: e.g. `Officium site`. Create.
3. Protect preview addresses too. Every publish also gets its own address (`<hash>.officium-advocati-diaboli.pages.dev`), which is public unless covered. **Workers & Pages → the project → Settings → General → Access policy → Enable.** This creates a second, locked application for `*.officium-advocati-diaboli.pages.dev` allowing only Cloudflare account members. Leave it as it is. (Its hostname cannot be edited; that is why step 2 creates the main application by hand.)
4. Copy into the project's **Variables and secrets** (step 2), then redeploy:
   - `ACCESS_TEAM_DOMAIN` = `officium-advocati-diaboli.cloudflareaccess.com` (shown under Settings → Team domain; also visible in the address bar of the sign-in page)
   - `ACCESS_AUD` = the **Application Audience (AUD) Tag** of the step 2 application. Several tags can be given separated by commas; add the preview application's tag only if the Request page should also work on preview addresses.
   - `ADMIN_EMAILS` = the owner's email (several separated by commas). Only these can open the Inbox (step 8b).

The API in `functions/api/_middleware.js` checks Access's signed token against these two values on every call, so it stays closed even if Access were misconfigured. A wrong tag shows on the Request page as "Your sign-in has expired"; opening `/api/requests` directly shows the exact reason.

## 4. Google sign-in (optional)

1. **console.cloud.google.com** → new project (e.g. `Officium Advocati Diaboli`).
2. **APIs & Services → OAuth consent screen** (also called Google Auth Platform): user type **External**, app name, support email, developer email. Scopes: none beyond the defaults (email, profile).
3. **Publish the app** (Audience / Publishing status → **In production**). While it says *Testing*, only listed test users can sign in. With only the default scopes no Google review is needed.
4. **Credentials (Clients) → Create → OAuth client ID → Web application.** Authorized redirect URI:
   `https://officium-advocati-diaboli.cloudflareaccess.com/cdn-cgi/access/callback`
   Copy the Client ID and Client secret.
5. **Cloudflare One → Settings → Authentication → Login methods → Add new → Google**: paste both, save, **Test**.
6. Open the step 3.2 application → **Login methods**: tick Google next to One-time PIN, turn **instant authentication off** (there are now two choices).

Google's sign-in screen shows the consent screen's app name and support email, so set those to the owner's details at handover.

## 5. Automatic publishing from GitHub

1. Cloudflare → **Manage account → Account API tokens → Create token** → custom: **Account · Cloudflare Pages · Edit**, this account only. Account tokens belong to the account, not a person, so they keep working when the person who made them leaves.
2. The **Account ID** is on the Workers & Pages overview page.
3. GitHub repo → **Settings → Secrets and variables → Actions → New repository secret** (needs Admin on the repo):
   - `CLOUDFLARE_API_TOKEN` = the token
   - `CLOUDFLARE_ACCOUNT_ID` = the account ID
4. **Actions → Deploy to Cloudflare → Run workflow.** From now on it publishes after every push to `main` and after each daily price update. Before the secrets exist it does nothing and passes.

## 6. Make the repo private, turn off the old site

Only after the Cloudflare site works with sign-in:

1. GitHub → **Settings → General → Danger zone → Change visibility → Private.**
2. **Settings → Pages**: unpublish / set the source to none, so `turnivor.github.io/investment-reports` stops serving.

The daily price Action keeps running (private repos get a monthly allowance of free Action minutes; this job uses about a minute a day). Anything published while public may already have been copied.

Side effects: link previews (the `og.png` card) no longer appear when the link is shared, because preview bots cannot sign in. The `og:` tags and the "Website" line in the README still point to github.io; update them to the new address when convenient.

## 7. `/queue` on the owner's computer

1. Cloudflare → **Account API tokens → Create token** → **Account · D1 · Edit**, this account only.
2. Send the owner three lines, privately (a messenger, not a public channel):
   ```
   ACCOUNT=<account id>
   DATABASE=<investment-requests database id>
   TOKEN=<the D1 token>
   ```
3. In his copy of the repo he double-clicks **`tools/setup-queue.cmd`** on Windows (it runs `setup-queue.ps1`; if Windows shows "Windows protected your PC", **More info → Run anyway**) or **`tools/setup-queue.command`** on a Mac (if macOS refuses, right-click → Open), and pastes the three lines. If Windows Terminal warns about pasting several lines, choose to paste anyway. The script installs `uv` if needed (which brings its own Python), checks the connection, registers the `research-queue` MCP server for all folders (`claude mcp add --scope user`), and copies `/queue` to `~/.claude/commands/`.

`/queue` then lists waiting requests as tick boxes and only runs what he picks. See [`.claude/commands/queue.md`](.claude/commands/queue.md).

## 8. Email when a request arrives (optional)

The API can open a GitHub issue per new request; GitHub emails the owner, like the price alerts.

1. The **repo owner** creates a fine-grained GitHub token: repository access only `investment-reports`, permission **Issues: Read and write**. (Only the owner can make a token for his own repo.)
2. Pages project → **Variables and secrets**: `GITHUB_TOKEN` as a **secret**, `GITHUB_REPO` = `Turnivor/investment-reports` as text. Redeploy.

## 8b. The Inbox (owner only, works on a phone)

`inbox.html` lists waiting requests with **Pick** and **Decline**. Picking runs nothing: it marks the request, friends see it as "Accepted", and `/queue` offers picked requests first. Only emails in `ADMIN_EMAILS` (step 3.5) can use it; the Request page shows an Inbox link to them.

A database created before the Inbox existed needs one extra column: run [`db/migrate-002-picked.sql`](db/migrate-002-picked.sql) once in **D1 → investment-requests → Console**. (A database made from the current `schema.sql` already has it.)

## 9. `/queue` from the phone (Claude Code cloud sessions)

Cloud sessions run Claude Code on Anthropic's servers, on this repo, under the owner's own Claude plan (no extra cost, same usage limits). He starts them from the **Code** tab of the Claude app or at claude.ai/code. Docs: [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web), [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments).

All of this happens in **the owner's** Claude account, once:

1. Open claude.ai/code (or the app's Code tab) and follow the onboarding: connect GitHub and install the **Claude GitHub App** on `Turnivor/investment-reports` only.
2. Edit the cloud environment (the cloud icon next to the environment name):
   - **Network access: Full.** The research reads many websites that the default "Trusted" list does not include.
   - **Setup script:** paste the whole of [`tools/cloud-setup.sh`](tools/cloud-setup.sh). It installs the ai-berkshire commands (cloned from GitHub into `~/ai-berkshire`) and Google Chrome for the PDFs. It runs once and is cached.
   - **API credentials** (Pro and Max plans): **Add credential** → name `Cloudflare queue`, allowed website `api.cloudflare.com`, header `Authorization`, prefix `Bearer`, value = the D1 token from step 7. Anthropic's proxy adds it to requests on the way out, so the token never enters the session. On a Team plan, which has no API credentials yet, put `CLOUDFLARE_API_TOKEN=<token>` under **Environment variables** instead (anyone using that environment can read it).
3. Start a session on `investment-reports` and type `/queue`.

How it fits together: the repo's [`.mcp.json`](.mcp.json) starts the queue tools as `research-queue-cloud` (with the account and database IDs, which are not secret), and `/queue` comes from the repo's `.claude/commands/`. In a cloud session `/queue` never pushes to `main`: it pushes a branch and opens a pull request, the owner merges it (the GitHub app works on a phone), the deploy workflow publishes, and then the request is marked done.

On his own computer, Claude Code may ask whether to use `research-queue-cloud` from `.mcp.json`: answer no. His local `research-queue` from step 7 is the one for his computer.

If the account or database ever changes, update the two IDs in `.mcp.json`.

## Testing

- **Locally** (no real sign-in): create a git-excluded `wrangler.toml` with `pages_build_output_dir = "."`, a `[[d1_databases]]` binding `DB`, and `[vars] DEV_EMAIL = "you@example.com"`; run the schema with `npx wrangler d1 execute <name> --local --file db/schema.sql`; then `npx wrangler pages dev --port 8788` and open `http://localhost:8788/request.html`. `DEV_EMAIL` only works on localhost.
- **On Cloudflare**: open the site in a private window → sign-in → the Request page says "Signed in as …" → send a request → `npx wrangler d1 execute investment-requests --remote --command "SELECT * FROM requests"`. An email not in `Friends` must be refused. `curl -i https://officium-advocati-diaboli.pages.dev/api/requests` must redirect to the sign-in, not return data.
- To sign out: `/cdn-cgi/access/logout` on the site.

## Handover

When the person who built this hands it to the owner:

- **Cloudflare**: invite the owner under **Manage account → Members** as **Super Administrator**. He accepts and adds his own card under **Billing**; then the builder removes herself. Account API tokens (steps 5 and 7) keep working.
- **Google Cloud**: **IAM & Admin → IAM → Grant access** → his Google account, role **Owner**. He accepts; set the consent screen's support email to his; then remove the builder.
- **GitHub**: lower or remove the builder's role on the repo.
- **Clean up test leftovers**: any test Pages project and D1 database, `npx wrangler logout` on the builder's computer, and her personal API tokens.

## Files

| File | What it does |
|---|---|
| [`request.html`](request.html) | The Request page: the form, and the friend's own requests with status and report links |
| [`functions/api/requests.js`](functions/api/requests.js) | List, add, cancel. Friends see only their own requests, can have 3 waiting, and can pick only the lighter report types |
| [`functions/api/_middleware.js`](functions/api/_middleware.js) | Checks the Access sign-in token on every API call |
| [`db/schema.sql`](db/schema.sql) | The queue table |
| [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) | Publishes to Cloudflare Pages |
| [`tools/queue_mcp.py`](tools/queue_mcp.py) | Queue tools for Claude Code: `list_pending`, `get_request`, `list_recent`, `mark_done`, `decline` |
| [`tools/setup-queue.cmd`](tools/setup-queue.cmd) + [`.ps1`](tools/setup-queue.ps1), [`tools/setup-queue.command`](tools/setup-queue.command) | One-time `/queue` setup: Windows, Mac |
| [`.claude/commands/queue.md`](.claude/commands/queue.md) | The `/queue` command |
| [`inbox.html`](inbox.html), [`functions/api/inbox.js`](functions/api/inbox.js) | The owner's Inbox: pick or decline from a phone |
| [`db/migrate-002-picked.sql`](db/migrate-002-picked.sql) | One-time column for databases made before the Inbox |
| [`.mcp.json`](.mcp.json), [`tools/cloud-setup.sh`](tools/cloud-setup.sh) | Queue tools and setup for cloud sessions |
