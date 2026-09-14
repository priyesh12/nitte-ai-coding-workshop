# Get your free API key — do this tonight (5 minutes)

> **Day 2 does not work without this.** One free key unlocks three of our four
> lab stations. It is free. There is no credit card, no trial, no expiry.
> If any screen asks for payment details, you are on the wrong page — stop.

---

## Step 1 — create the key

1. Go to **https://aistudio.google.com/apikey**
2. Sign in with **any** Google account (your personal Gmail is fine)
3. Click **Create API key**
4. Click **Copy**

It looks like `AIzaSy...` and is about 39 characters.

> **Treat it like a password.** Don't paste it into a chat window, don't put it
> in a WhatsApp group, don't commit it to Git. If you ever leak one, delete it
> on that same page and make a new one — takes 10 seconds, no harm done.

## Step 2 — save it on your machine

Replace `PASTE_YOUR_KEY_HERE` with what you copied.

### macOS / Linux
```bash
echo 'export GEMINI_API_KEY="PASTE_YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```
> Using bash instead of zsh? Use `~/.bashrc` in both lines.

### Windows — PowerShell
```powershell
setx GEMINI_API_KEY "PASTE_YOUR_KEY_HERE"
```
> **Then close PowerShell and open a new one.** `setx` only affects new windows.

## Step 3 — prove it worked

### macOS / Linux
```bash
echo $GEMINI_API_KEY
```
### Windows — PowerShell
```powershell
echo $env:GEMINI_API_KEY
```

**It must print your key.** If it prints nothing, or prints the literal text
`$GEMINI_API_KEY`, it did not work — see below.

---

## If it didn't work

| What happened | Fix |
|---|---|
| Prints nothing | You didn't reopen the terminal. Close it completely, open a new one, try again. |
| Prints `$GEMINI_API_KEY` literally | You're on Windows CMD, not PowerShell. Use PowerShell. |
| `command not found: setx` | You're on Mac/Linux — use the macOS/Linux commands. |
| Key page asks for billing | Wrong page. Use **aistudio.google.com/apikey**, not Google Cloud Console. |
| Google account is a college account that blocks it | Use a personal Gmail. Takes 2 minutes to make one. |
| Genuinely stuck | **Stop after 15 minutes.** Bring it to Day 2 — you'll pair with someone who has a key and lose nothing. |

---

## Bring to Day 2

- [ ] `echo $GEMINI_API_KEY` prints a key
- [ ] Your laptop, charged
- [ ] Your Day 1 hypothesis sheet

> **No key, no problem** — you'll pair up. But try. Doing this yourself is the
> first half of invariant #6, which is the thing that makes these tools free.
