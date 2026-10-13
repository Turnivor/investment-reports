# One-time setup of /queue in Claude Code on Windows. Started by double-clicking setup-queue.cmd.
# It asks for one paste: the three lines you were sent
#   ACCOUNT=...
#   DATABASE=...
#   TOKEN=...
# Nothing is stored in the repo; the values go into your own Claude Code settings.

$ErrorActionPreference = 'Stop'
$Repo = Split-Path -Parent $PSScriptRoot

function Done-Pause { Write-Host ''; Read-Host 'Press Enter to close this window' | Out-Null }
function Fail($msg) { Write-Host ''; Write-Host "X  $msg" -ForegroundColor Red; Done-Pause; exit 1 }
function Ok($msg) { Write-Host "OK $msg" -ForegroundColor Green }
function Find-Exe($name, $candidates) {
  $cmd = Get-Command $name -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($cmd) { return $cmd.Source }
  foreach ($c in $candidates) { if ($c -and (Test-Path $c)) { return $c } }
  return $null
}

Write-Host 'Setting up /queue for Claude Code'
Write-Host '================================='
Write-Host ''

# 1. Claude Code must be installed
$Claude = if ($env:CLAUDE_EXE) { $env:CLAUDE_EXE } else {
  Find-Exe 'claude' @("$env:USERPROFILE\.local\bin\claude.exe", "$env:APPDATA\npm\claude.cmd")
}
if (-not $Claude) { Fail 'Claude Code was not found. Install it first, then double-click setup-queue.cmd again.' }
Ok 'Claude Code found'

# 2. uv runs the queue script with the right Python and its one library, without touching your Python setup
$Uv = if ($env:UV_EXE) { $env:UV_EXE } else { Find-Exe 'uv' @("$env:USERPROFILE\.local\bin\uv.exe") }
if (-not $Uv) {
  Write-Host '... installing uv (a small Python helper, about 20 seconds)'
  try {
    powershell -NoProfile -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex" | Out-Null
  } catch { Fail 'Could not install uv. Check the internet connection and try again.' }
  $Uv = Find-Exe 'uv' @("$env:USERPROFILE\.local\bin\uv.exe")
  if (-not $Uv) { Fail 'uv was installed but could not be found. Close this window and double-click setup-queue.cmd again.' }
}
Ok 'uv ready'

# 3. The three values (hidden while pasting)
Write-Host ''
Write-Host 'Paste the three lines you were sent (ACCOUNT=..., DATABASE=..., TOKEN=...).'
Write-Host 'Nothing will show while you paste. If it keeps waiting, press Enter.'
$vals = @{}
for ($i = 0; $i -lt 6 -and $vals.Count -lt 3; $i++) {
  $secure = Read-Host -AsSecureString
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
  try { $line = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }
  foreach ($part in ($line -split "[`r`n]+")) {
    $p = $part.Trim()
    if ($p -match '^(ACCOUNT|DATABASE|TOKEN)=(.+)$') { $vals[$Matches[1]] = $Matches[2].Trim() }
  }
}
if ($vals.Count -lt 3) { Fail 'Not all three lines arrived. Double-click setup-queue.cmd again and paste all three.' }
Ok 'Got the three values'

# 4. Check they work before saving anything
Write-Host '... checking the connection to the request queue'
$env:CLOUDFLARE_ACCOUNT_ID = $vals['ACCOUNT']
$env:CLOUDFLARE_D1_ID = $vals['DATABASE']
$env:CLOUDFLARE_API_TOKEN = $vals['TOKEN']
$py = @"
import sys
sys.path.insert(0, sys.argv[1])
import queue_mcp
r = queue_mcp.query("SELECT COUNT(*) AS n FROM requests WHERE status = 'pending'")
print("OK " + str(r["results"][0]["n"]))
"@
$ErrorActionPreference = 'Continue'
$check = ($py | & $Uv run --quiet --no-project --python '>=3.10' --with 'mcp[cli]' python - (Join-Path $Repo 'tools') 2>&1 | Out-String)
$ErrorActionPreference = 'Stop'
Remove-Item Env:CLOUDFLARE_ACCOUNT_ID, Env:CLOUDFLARE_D1_ID, Env:CLOUDFLARE_API_TOKEN -ErrorAction SilentlyContinue
if ($check -match 'OK (\d+)') {
  Ok "Connected. Requests waiting right now: $($Matches[1])"
} else {
  Write-Host (($check -split "`n" | Select-Object -Last 3) -join "`n")
  Fail 'The connection check failed. Ask for the three lines again (the token may be wrong or expired).'
}

# 5. Register the queue tools with Claude Code, for every folder
$ErrorActionPreference = 'Continue'
& $Claude mcp remove research-queue --scope user 2>&1 | Out-Null
& $Claude mcp add --scope user research-queue `
  -e "CLOUDFLARE_ACCOUNT_ID=$($vals['ACCOUNT'])" `
  -e "CLOUDFLARE_D1_ID=$($vals['DATABASE'])" `
  -e "CLOUDFLARE_API_TOKEN=$($vals['TOKEN'])" `
  -- $Uv run --quiet --no-project --python '>=3.10' --with 'mcp[cli]' python (Join-Path (Join-Path $Repo 'tools') 'queue_mcp.py') 2>&1 | Out-Null
$added = $LASTEXITCODE
$ErrorActionPreference = 'Stop'
if ($added -ne 0) { Fail 'Claude Code did not accept the queue tools.' }
Ok 'Queue tools added to Claude Code'

# 6. The /queue command, for every folder
$cmdDir = Join-Path (Join-Path $env:USERPROFILE '.claude') 'commands'
New-Item -ItemType Directory -Force -Path $cmdDir | Out-Null
try { Copy-Item (Join-Path (Join-Path (Join-Path $Repo '.claude') 'commands') 'queue.md') (Join-Path $cmdDir 'queue.md') -Force }
catch { Fail 'Could not copy the /queue command.' }
Ok '/queue command installed'

Write-Host ''
Write-Host 'All set. Open Claude Code (in any folder) and type:  /queue'
Write-Host "If you move this folder ($Repo), run setup-queue.cmd again from its new place."
Done-Pause
