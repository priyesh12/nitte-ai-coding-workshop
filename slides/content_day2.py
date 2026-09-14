# -*- coding: utf-8 -*-
"""Day 2 — DELEGATE. Four session decks."""

S1 = [
 '''<div class="kicker">Day 2 · Session 1 · 09:30–11:00</div>
    <h1>DELEGATE</h1><p class="big dim">The seven invariants</p>
    <p class="dim">Drive any AI tool. Distrust every output.</p>''',

 '''<h2>Key check — 5 minutes</h2>
    <pre>echo $GEMINI_API_KEY</pre>
    <p class="big">Hands up if that printed something.</p>
    <p class="warn">No key? Pair up now. One key per pair is plenty —
    and driver/navigator is better practice anyway.</p>''',

 '''<div class="center"><h1>There are <span class="hl">150+</span><br>of these tools.</h1>
    <p class="big dim">OpenCode · Aider · Pi · oh-my-pi · Goose · Crush<br>
    Plandex · Codex CLI · Gemini CLI · Cline · Continue<br>
    Cursor · Claude Code · Droid · Auggie · Warp</p></div>''',

 '''<h2>And a whole layer above them</h2>
    <div class="grid">
    <div class="card"><h3>Orchestrators</h3><p>Claude Squad · vibe-kanban ·
    cmux · Orca</p><p class="dim">Run <b>fleets</b> of agents in parallel.</p></div>
    <div class="card"><h3>Infrastructure</h3><p>Context compression ·
    memory stores · security guards</p><p class="dim">Plumbing under the agents.</p></div>
    </div>
    <p class="big warn">New ones ship every week.</p>
    <p class="dim">Half of that list didn't exist a year ago.</p>''',

 '''<div class="center"><h1>You cannot learn<br>150 tools.</h1>
    <p class="big dim">And any one you memorise<br>
    will be obsolete before your notice period ends.</p></div>''',

 '''<div class="center"><h1>Don't memorise tools.<br>
    <span class="hl">Learn the primitives.</span></h1>
    <p class="big dim">All 150 are the same seven things<br>wearing different paint.</p></div>''',

 '''<h2>The seven invariants</h2>
    <table>
    <tr><td class="num">1</td><td><b>Context file</b></td><td class="dim"><code>AGENTS.md</code>, <code>CLAUDE.md</code>, <code>.cursorrules</code></td></tr>
    <tr><td class="num">2</td><td><b>Agent loop</b></td><td class="dim">prompt → plan → edit → test → repeat</td></tr>
    <tr><td class="num">3</td><td><b>Permissions</b></td><td class="dim">what runs without asking you</td></tr>
    <tr><td class="num">4</td><td><b>Diff review</b></td><td class="dim">the only real quality gate</td></tr>
    <tr><td class="num">5</td><td><b>Session state</b></td><td class="dim">resume, fork — and <code>git</code> as undo</td></tr>
    <tr><td class="num">6</td><td><b>Provider routing</b></td><td class="dim">bring your own key</td></tr>
    <tr><td class="num">7</td><td><b>Extensions</b></td><td class="dim">MCP, custom commands, subagents</td></tr>
    </table>
    <p class="big">Know these, and any new tool is a 10-minute README read.</p>''',

 '''<div class="kicker">Invariant #2</div><h2>The agent loop</h2>
    <pre>   YOU: "add students_at_risk to reports.py"
        ↓
   <span class="hl">PLAN</span>     it decides which files to read
        ↓
   <span class="hl">READ</span>     reports.py, models.py
        ↓
   <span class="hl">EDIT</span>     proposes a diff
        ↓
   <span class="hl">TEST</span>     runs your test command
        ↓
   <span class="hl">ITERATE</span>  red? go back to EDIT</pre>
    <p class="big">Every single one of the 150 is this loop.</p>''',

 '''<div class="kicker">Invariant #3</div><h2>Permissions</h2>
    <p>What can it do <b>without asking you?</b></p>
    <table><tr><th>Level</th><th>Means</th></tr>
    <tr><td>Read files</td><td class="dim">Almost always allowed</td></tr>
    <tr><td>Edit files</td><td class="warn">Usually asks first</td></tr>
    <tr><td>Run shell commands</td><td class="bad">Should always ask</td></tr>
    <tr><td>"auto-approve everything"</td><td class="bad">Tempting. Don't.</td></tr></table>
    <div class="ask">Most students never look at this setting.
    Find it in every tool you touch today.</div>''',

 '''<div class="kicker">Invariant #6 — why today costs nothing</div>
    <h2>Harness ≠ model</h2>
    <pre>   HARNESS  (on your laptop)  ---->  PROVIDER  (the model)

   OpenCode                          Google AI Studio
   Aider                             <span class="hl">ONE FREE KEY</span>
   Gemini CLI                        no card, no trial</pre>
    <p class="big">One free key unlocks <span class="hl">three of four stations</span>.</p>''',

 '''<h2>Why this matters beyond today</h2>
    <ul><li>You are <b>not locked in</b> to any company</li>
    <li>Model too expensive? Swap the provider, keep the tool</li>
    <li>Model gets better? Swap it, keep the tool</li>
    <li>Company bans a vendor? Swap it, keep the tool</li></ul>
    <p class="big hl">The harness is your habit. The model is a commodity.</p>
    <p class="dim">That sentence is a good interview answer.</p>''',

 '''<div class="kicker">Invariant #1 — the big one</div>
    <h2>The context file</h2>
    <pre><span class="dim"># AGENTS.md</span>
1. <b>Never "fix" anything under bugs/.</b> Broken on purpose.
2. <b>Standard library only.</b> No pip, no packages.
4. <b>Smallest possible change.</b> Do not refactor.
5. <b>Show the diff before applying it.</b></pre>
    <p class="big">A tool you never configured will obey this.</p>''',

 '''<h2>Same rules, two filenames</h2>
    <div class="grid">
    <div class="card"><h3><code>AGENTS.md</code></h3>
    <p>OpenCode · Codex CLI · Pi · Amp · and most open-source tools</p></div>
    <div class="card"><h3><code>CLAUDE.md</code></h3>
    <p>Claude Code</p></div>
    </div>
    <p class="dim">Others: <code>.cursorrules</code>,
    <code>.github/copilot-instructions.md</code></p>
    <p class="big">Same idea everywhere. The ecosystem just hasn't
    agreed on a filename yet.</p>''',

 '''<div class="center"><div class="kicker">Live demo</div>
    <h1>Watch a tool obey<br>a file you wrote.</h1>
    <p class="big">Ask it to read a CSV.<br>
    Watch it <span class="hl">not</span> reach for pandas.</p>
    <p class="dim">Then we delete rule 2 and ask again.</p></div>''',

 '''<h2>What just happened</h2>
    <p>One markdown file changed the behaviour of a tool
    <b>you did not configure</b>.</p>
    <p class="big hl">That is the highest-leverage thing you'll learn today.</p>
    <div class="ask">In a real job: your team's <code>AGENTS.md</code> encodes
    the house style, so every engineer's AI produces consistent code.
    That's why this matters.</div>''',

 '''<div class="kicker">Invariant #4 — the one that saves you</div>
    <h2>Diff review</h2>
    <pre>git diff</pre>
    <p class="big">The same review surface no matter <b>which</b>
    of the 150 tools made the change.</p>
    <p class="warn">If a tool won't show you a diff before applying,
    that's a reason to distrust the tool.</p>''',

 '''<div class="kicker">Invariant #5</div><h2>Session state &amp; undo</h2>
    <table><tr><th>Tool feature</th><th>Universal version</th></tr>
    <tr><td>"undo last edit"</td><td><code>git reset --hard HEAD</code></td></tr>
    <tr><td>"fork this session"</td><td><code>git branch</code></td></tr>
    <tr><td>"checkpoint"</td><td><code>git commit</code></td></tr></table>
    <p class="big">Git works in every tool, forever.</p>
    <p class="dim">Tomorrow's whole second session is this.</p>''',

 '''<div class="kicker">Invariant #7</div><h2>Extensions — know the word</h2>
    <p><b>MCP</b> — Model Context Protocol. A standard way to give an agent
    new abilities: read a database, call an API, search your docs.</p>
    <p><b>Custom commands</b> — your own shortcuts.</p>
    <p><b>Subagents</b> — the agent spawning helpers for sub-tasks.</p>
    <p class="dim">You don't need to use these today. You need to
    <b>know the words</b> when an interviewer says them.</p>''',

 '''<h2>Session 1 close</h2>
    <p class="big">Seven invariants. Then a new tool is just
    a new keyboard shortcut.</p>
    <p class="quote">The harness is your habit.<br>The model is a commodity.</p>
    <p class="dim">Next: four tools, one task, twenty minutes each.</p>''',
]

S2 = [
 '''<div class="kicker">Day 2 · Session 2 · 11:30–13:00</div>
    <h1>Harness rotation</h1>
    <p class="big dim">Same task. Four tools. Twenty minutes each.</p>''',

 '''<h2>The task — identical at every station</h2>
    <pre>def students_at_risk(students) -> list[Student]:
    """cgpa &lt; 6.0 OR backlogs &gt; 0, sorted by cgpa ascending."""</pre>
    <p>Add it to <code>placement_tracker/reports.py</code>. Make this pass:</p>
    <pre>python3 run_tests.py tests/visible</pre>
    <p class="warn">Do not edit the test file.</p>''',

 '''<h2>The four stations</h2>
    <table><tr><th>#</th><th>Tool</th><th>What makes it different</th></tr>
    <tr><td class="num">1</td><td><b>Gemini CLI</b></td><td>Google's own. Best free tier of anything.</td></tr>
    <tr><td class="num">2</td><td><b>OpenCode</b></td><td>Open source, 75+ providers, full TUI.</td></tr>
    <tr><td class="num">3</td><td><b>Aider</b></td><td>Patch-centric, git-native. Auto-commits.</td></tr>
    <tr><td class="num">4</td><td><b>Browser AI</b></td><td>No file access. You paste context by hand.</td></tr>
    </table>
    <p class="big">Bell every 20 minutes. <span class="warn">Hard rotation.</span></p>''',

 '''<div class="center"><h1>Unfinished is fine.</h1>
    <p class="big">The <span class="hl">comparison</span> is the deliverable,
    not the working function.</p>
    <p class="dim">Fill in the scorecard as you go — not afterwards from memory.</p></div>''',

 '''<h2>What to record at each station</h2>
    <ul><li>Minutes to first working setup</li>
    <li>Did it find the right file <b>itself</b>?</li>
    <li>Did it run the tests <b>itself</b>?</li>
    <li>Could you see the diff <b>before</b> it applied?</li>
    <li>Did it respect <code>AGENTS.md</code>?</li>
    <li>How easy was it to undo a bad edit?</li></ul>
    <p class="dim"><code>harnesses/SCORECARD.md</code> — in your repo.</p>''',

 '''<h2>And find all seven invariants</h2>
    <p>At <b>each</b> station, write down where you saw each one.</p>
    <p class="big">If a tool doesn't have one — write
    <span class="hl">"none"</span>.</p>
    <p class="dim">That's a real and interesting answer. Browser AI has
    no permissions model at all, because it can't do anything to your files.</p>''',

 '''<div class="kicker">Station 1</div><h2>Gemini CLI</h2>
    <pre>npm install -g @google/gemini-cli
gemini</pre>
    <p class="dim">Or use <code>npx</code> if you can't install globally.</p>
    <ul><li>Signs in with your Google account or the key you made</li>
    <li>Full agent loop — reads, edits, runs commands</li>
    <li>Best free tier of anything on this list</li></ul>
    <p class="warn">If everything else fails today, this is the one
    that will work.</p>''',

 '''<div class="kicker">Station 2</div><h2>OpenCode</h2>
    <pre>curl -fsSL https://opencode.ai/install | bash
opencode</pre>
    <ul><li>Open source, terminal TUI</li>
    <li><b>75+ providers</b> — this is invariant #6 made visible</li>
    <li>Reads <code>AGENTS.md</code></li>
    <li>Can run fully local models with Ollama — no account at all</li></ul>
    <div class="ask">Open its provider config. That screen <b>is</b>
    invariant #6.</div>''',

 '''<div class="kicker">Station 3</div><h2>Aider — the odd one out</h2>
    <pre>pip install aider-install &amp;&amp; aider-install
aider --model gemini/gemini-2.0-flash</pre>
    <p class="big">Architecturally <span class="hl">different</span>
    from the other three.</p>
    <ul><li>Not an agent TUI — a <b>patch applier</b></li>
    <li><b>Auto-commits every change</b> to git</li>
    <li>You add files to the chat explicitly</li></ul>
    <p class="dim">Notice how much you miss automatic file discovery.</p>''',

 '''<div class="kicker">Station 4</div><h2>Browser AI — the honest one</h2>
    <p>No file access. No tools. No loop. <b>You</b> are the agent.</p>
    <ul><li>You choose what to paste</li>
    <li>You copy the answer back</li>
    <li>You run the tests</li></ul>
    <p class="big warn">Whatever you had to paste by hand is exactly
    what the other three figured out on their own.</p>
    <p class="dim">That list is your answer to debrief question 3.</p>''',

 '''<h2>Debrief — the five questions</h2>
    <ol><li>Which station was <b>fastest</b>?</li>
    <li>Which did you <b>trust most</b>? <span class="dim">(usually a different tool — that gap is the lesson)</span></li>
    <li>What did you have to tell Station 4 that the others worked out?</li>
    <li><b>Same model. Same task. Different results. Why?</b></li>
    <li>If AI were banned tomorrow, what from today still has value?</li></ol>''',

 '''<div class="center"><h1>Question 4 is<br>the whole session.</h1>
    <p class="big">Same model behind stations 1–3.<br>
    Completely different experience.</p></div>''',

 '''<h2>Why the harness matters as much as the model</h2>
    <table><tr><th>The harness decides</th><th>Which changes</th></tr>
    <tr><td>Which files it reads</td><td>How much it actually knows</td></tr>
    <tr><td>Whether it runs your tests</td><td>Whether it catches its own errors</td></tr>
    <tr><td>How it shows you a diff</td><td>Whether you catch its errors</td></tr>
    <tr><td>What it does without asking</td><td>How much damage it can do</td></tr></table>
    <p class="big">The model writes the code. <span class="hl">The harness
    decides if it's any good.</span></p>''',

 '''<h2>Session 2 close</h2>
    <p class="big">You've now driven four tools in 90 minutes.</p>
    <p>Not one of them was hard — because you learned the
    <b>primitives</b> first.</p>
    <p class="quote">That is exactly how you'll pick up tool #151.</p>
    <p class="warn">After lunch: code that an AI wrote, that looks perfect,
    and isn't.</p>''',
]

S3 = [
 '''<div class="kicker">Day 2 · Session 3 · 13:45–15:15</div>
    <h1>The sabotage drill</h1>
    <p class="big dim">AI wrote this. Every function has a bug.</p>''',

 '''<div class="center"><h1>An AI wrote this code.</h1>
    <p class="big">It is clean. It is commented. It is idiomatic.</p>
    <p class="big warn">Every function has a bug.</p></div>''',

 '''<h2>The rules</h2>
    <ul><li><b>20 minutes.</b> Reading only.</li>
    <li><span class="bad">No running the code.</span></li>
    <li><span class="bad">No AI.</span></li>
    <li>Write down every bug you think you've found</li></ul>
    <pre>day2/sabotage/ai_output.py</pre>
    <p class="dim">I'm not telling you how many there are.</p>''',

 '''<div class="center"><div class="kicker">20 minutes · reading only</div>
    <h1>Go.</h1></div>''',

 '''<div class="kicker">Before we run it</div>
    <h2>What did you find?</h2>
    <p class="big">Hands up. Let's put them on the board.</p>
    <p class="dim">Be specific — function name and line.</p>''',

 '''<h2>Now run it</h2>
    <pre>python3 run_tests.py day2/sabotage</pre>
    <p class="big">Four functions. <span class="warn">Four bugs.</span>
    Six failing tests.</p>
    <div class="ask">How many did you find by reading?</div>''',

 '''<div class="kicker">Bug 1</div><h2><code>calculate_percentage</code></h2>
    <pre>if total_count == 0:
    return 0.0
return round((placed_count / total_count) * 100, 2)</pre>
    <p>Handles zero. Rounds properly. Clean docstring.</p>
    <pre class="bad">calculate_percentage(500, 200)   →   250.0</pre>
    <p class="big">More students placed than exist.</p>
    <p class="dim">Real data has typos. Returning 250% isn't
    "handling" it — it's hiding it.</p>''',

 '''<div class="kicker">Bug 2 — the nasty one</div>
    <h2><code>paginate</code></h2>
    <pre>"""Pages are 1-indexed, so page 1 returns
   the first per_page students."""

start = page * per_page</pre>
    <p class="big bad">Page 1 starts at index 10.</p>
    <p class="big">The docstring is a <span class="bad">lie</span>.</p>
    <p class="dim">And the lie is exactly what made you skip reading the code.</p>''',

 '''<div class="kicker">Bug 3</div><h2><code>get_cgpa</code></h2>
    <pre>return float(student.get("cgpa", 0.0))</pre>
    <p>Looks like textbook defensive programming.</p>
    <pre class="bad">get_cgpa({})               → 0.0   ✓
get_cgpa({"cgpa": None})   → <span class="bad">TypeError</span></pre>
    <p class="big">The default <b>only</b> fires when the key is
    <span class="hl">missing</span>.</p>
    <p class="dim">A student whose CGPA isn't entered yet has
    <code>cgpa=None</code>. The key exists. Crash.</p>''',

 '''<div class="kicker">Bug 4</div><h2><code>merge_skill_lists</code></h2>
    <pre>existing.extend(incoming)
return sorted(set(existing))</pre>
    <p>Returns the right answer. <b>And silently modifies the
    caller's list.</b></p>
    <pre class="bad">original = ["Python"]
merge_skill_lists(original, ["SQL"])
print(original)   → ['Python', 'SQL']   <span class="bad">← ?!</span></pre>
    <p class="dim">You met this exact class of bug on Day 1.</p>''',

 '''<h2>All four, together</h2>
    <table><tr><th>Function</th><th>Bug</th><th>Day 1 echo</th></tr>
    <tr><td><code>calculate_percentage</code></td><td>No validation</td><td>Edge cases</td></tr>
    <tr><td><code>paginate</code></td><td>Off-by-one</td><td>Boundaries</td></tr>
    <tr><td><code>get_cgpa</code></td><td>Default never fires</td><td>Wrong assumptions</td></tr>
    <tr><td><code>merge_skill_lists</code></td><td>Mutates caller's list</td><td>Mutation bugs</td></tr></table>
    <p class="big">Nothing new. <span class="hl">You already knew all four
    classes.</span></p>''',

 '''<div class="center"><h1>So why were they<br>so hard to see?</h1></div>''',

 '''<div class="center"><h1>Beautiful code<br><span class="hl">lowers your guard.</span></h1>
    <p class="big dim">You skim clean code.<br>You scrutinise ugly code.</p>
    <p class="big warn">AI output is always clean.<br>
    So your guard is always down.</p></div>''',

 '''<h2>The six traps</h2>
    <table><tr><th>Trap</th><th>Looks like</th></tr>
    <tr><td>Bloat</td><td>40 lines where 6 would do</td></tr>
    <tr><td>Invented APIs</td><td>A method that doesn't exist</td></tr>
    <tr><td>Wrong defaults</td><td><code>.get(k, 0)</code> when <code>None</code> was meant</td></tr>
    <tr><td>Over-abstraction</td><td>A class hierarchy for one function</td></tr>
    <tr><td><b>Confident wrongness</b></td><td>A docstring that contradicts the code</td></tr>
    <tr><td>Scope creep</td><td>You asked for a fix, it rewrote the file</td></tr></table>
    <p class="dim">Full checklist: <code>handouts/ai-traps.md</code></p>''',

 '''<h2>Which of these passes a sample test?</h2>
    <div class="ask">All four. Every single one passes the happy path.</div>
    <p class="big warn">This is precisely what a screening test does to you.</p>
    <ul><li>Sample case: passes</li><li>You submit</li>
    <li>Hidden tests: three failures</li>
    <li>You have no idea why — you never understood the code</li></ul>''',

 '''<div class="center"><h1>You may not submit a line<br>
    <span class="hl">you cannot explain out loud.</span></h1>
    <p class="big warn">Graded tomorrow. In front of the room.</p></div>''',

 '''<div class="kicker">The flip · 25 minutes</div>
    <h2>Ask AI for tests, not solutions</h2>
    <pre class="info">Write edge-case tests for this function.
<span class="hl">Do NOT change the implementation.</span>

&lt;paste the function&gt;

Cover: empty input, single element, boundary
values, duplicates, and anything that breaks it.
Plain asserts - no pytest.</pre>''',

 '''<div class="center"><h1>Tests are cheap to verify<br>
    and expensive to write.</h1>
    <p class="big hl">Code is the opposite.</p>
    <p class="big dim">This is the best trade you can make with an AI.</p></div>''',

 '''<h2>Why this is the habit that gets you placed</h2>
    <ul><li>You can <b>check</b> a test in 5 seconds — does it test what it says?</li>
    <li>Checking generated <b>code</b> takes as long as writing it</li>
    <li>Generated tests find <b>your</b> bugs too</li>
    <li>You stay the author of the logic — so you can defend it</li></ul>
    <p class="big">Use AI where verification is cheap.</p>''',

 '''<h2>Session 3 close</h2>
    <p class="quote">The problem isn't that AI writes bad code.<br>
    It's that AI writes <b>beautiful</b> bad code.</p>
    <p class="big">Your 60-second review, every time:
    read every line · docstring vs code · <code>git diff</code> ·
    run the tests · test the boundary · test empty.</p>''',
]

S4 = [
 '''<div class="kicker">Day 2 · Session 4 · 15:30–17:00</div>
    <h1>Cold start<br>&amp; bake-off</h1>
    <p class="big dim">A tool nobody taught you</p>''',

 '''<div class="center"><h1>15 minutes.<br>The README only.</h1>
    <p class="big">Install it. Point it at your key. Finish a task.</p>
    <p class="dim">Goose · Crush · Plandex — you pick.</p></div>''',

 '''<h2>Why this is the real exam</h2>
    <p>You cannot be taught 150 tools.</p>
    <p class="big hl">You can learn to onboard yourself onto any of them.</p>
    <p class="warn">"How do you pick up new technology?"</p>
    <p class="dim">You <b>will</b> be asked this. Today is your answer.</p>''',

 '''<h2>Your onboarding checklist</h2>
    <p>Use the seven invariants as a checklist on any new tool:</p>
    <ol><li>Where's the <b>context file</b>?</li>
    <li>How do I see the <b>agent loop</b>?</li>
    <li>What are the <b>permission</b> defaults?</li>
    <li>How do I see a <b>diff</b> before it applies?</li>
    <li>How do I <b>undo</b>?</li>
    <li>How do I point it at <b>my provider</b>? ← usually the blocker</li>
    <li>What <b>extensions</b> does it take?</li></ol>''',

 '''<div class="center"><div class="kicker">Go · 15 minutes</div>
    <h1>README only.</h1>
    <p class="big dim">No asking me. No asking another AI how to use it.</p></div>''',

 '''<h2>Debrief — what blocked you?</h2>
    <div class="ask">Almost always: pointing it at a provider.</div>
    <p class="big">That's <span class="hl">invariant #6</span>.</p>
    <p>Now you know why we spent the morning on the difference between
    a harness and a model.</p>
    <p class="dim">Half the room succeeding is a completely fine outcome.</p>''',

 '''<div class="center"><div class="kicker">The bake-off · 35 minutes</div>
    <h1>Same bug.<br>Four harnesses.<br>Race.</h1></div>''',

 '''<h2>Rules</h2>
    <ul><li>One bug, none of you have seen it</li>
    <li>Your pair picks <b>one</b> harness and commits to it</li>
    <li>Record: <b>time</b>, and <b>did it work first try</b></li>
    <li>You must be able to <b>explain the fix</b> to claim the win</li></ul>
    <p class="warn">That last rule is not optional. An unexplained fix
    doesn't count.</p>''',

 '''<div class="kicker">Results</div><h2>Let's plot it</h2>
    <p class="big">Harness on one axis. Time on the other.</p>
    <div class="ask">Look at the board. Is there a pattern by tool?</div>''',

 '''<div class="center"><h1>There's no correlation<br>with the tool.</h1>
    <p class="big">The winners are the pairs who<br>
    <span class="hl">decomposed the problem before prompting.</span></p></div>''',

 '''<div class="center"><h1>The tool is not the skill.</h1>
    <p class="big hl">You are the skill.</p></div>''',

 '''<h2>What actually separated the winners</h2>
    <ul><li>They <b>reproduced</b> the failure first</li>
    <li>They formed a <b>hypothesis</b> before opening any tool</li>
    <li>They gave the tool the <b>failing test</b>, not just the code</li>
    <li>They <b>read the diff</b> instead of accepting it</li>
    <li>They ran the tests <b>themselves</b></li></ul>
    <p class="big warn">That's Day 1. With a faster keyboard.</p>''',

 '''<h2>Two days in</h2>
    <table><tr><th>Day 1</th><th>Day 2</th></tr>
    <tr><td>The debugging loop</td><td>Still the loop — with a tool</td></tr>
    <tr><td>Hypothesis first</td><td>Hypothesis <b>before prompting</b></td></tr>
    <tr><td>Read the traceback</td><td>Read the <b>diff</b></td></tr>
    <tr><td>Test the boundary</td><td>AI <b>writes</b> the boundary tests</td></tr>
    <tr><td>Smallest fix</td><td>Reject the bloat</td></tr></table>
    <p class="big">Same method. Better leverage.</p>''',

 '''<div class="center"><div class="kicker">Tomorrow</div>
    <h1>DELIVER</h1>
    <p class="big">Build something end-to-end.<br>Then defend every line.</p>
    <p class="quote">Any line you cannot explain<br>
    is struck from your submission.</p>
    <p class="dim">No homework. Rest. Tomorrow is the heavy day.</p></div>''',
]

DECKS = [
 ("day2-s1.html", "DAY 2 · S1", "Day 2 S1 — The Seven Invariants", S1),
 ("day2-s2.html", "DAY 2 · S2", "Day 2 S2 — Harness Rotation", S2),
 ("day2-s3.html", "DAY 2 · S3", "Day 2 S3 — The Sabotage Drill", S3),
 ("day2-s4.html", "DAY 2 · S4", "Day 2 S4 — Cold Start & Bake-Off", S4),
]
