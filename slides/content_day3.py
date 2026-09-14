# -*- coding: utf-8 -*-
"""Day 3 — DELIVER. Four session decks."""

S1 = [
 '''<div class="kicker">Day 3 · Session 1 · 09:30–11:00</div>
    <h1>DELIVER</h1><p class="big dim">Clean code &amp; the developer loop</p>''',

 '''<div class="center"><div class="kicker">Read this first</div>
    <h1 class="warn">You will be called<br>at random this afternoon.</h1>
    <p class="big">To explain your own code, line by line.</p>
    <p class="quote">Any line you cannot explain is struck from
    your submission — even if the tests pass.</p></div>''',

 '''<h2>Today</h2>
    <pre>09:30   clean code &amp; the developer loop
11:30   git as your AI safety net

13:45   <span class="hl">MOCK ASSESSMENT</span>    90 min, graded
15:30   <span class="hl">VIVA</span>                random, 30 marks</pre>
    <p class="dim">100 marks. Thirty of them are for explaining it.</p>''',

 '''<h2>"Readable" isn't style rules</h2>
    <p class="big">Three things. That's all.</p>
    <ol><li><b>Names say <i>what</i>, not <i>how</i></b></li>
    <li><b>One function, one job</b></li>
    <li><b>Comments say <i>why</i></b></li></ol>''',

 '''<div class="kicker">Rule 1</div><h2>Names</h2>
    <pre class="bad">def f(l, x):
    r = []
    for i in l:
        if i[1] &gt; x: r.append(i)
    return r</pre>
    <pre>def shortlist(students, min_cgpa):
    eligible = []
    for student in students:
        if student.cgpa &gt;= min_cgpa:
            eligible.append(student)
    return eligible</pre>
    <p class="big">Same logic. One of them has an obvious bug.</p>''',

 '''<div class="center"><h1>Did you spot<br>the bug in the first one?</h1>
    <p class="big"><code>i[1] &gt; x</code> should be <code>&gt;=</code></p>
    <p class="big hl">Unreadable code hides bugs.<br>
    That's not an opinion — you just proved it.</p></div>''',

 '''<div class="kicker">Rule 2</div><h2>One function, one job</h2>
    <p class="big">If the name needs the word <b>"and"</b>, split it.</p>
    <pre class="bad">def load_and_filter_and_report(path, criteria):</pre>
    <pre>def load_students(path): ...
def shortlist(students, criteria): ...
def format_report(students): ...</pre>
    <p class="dim">Three small functions are three things you can test
    separately — and three things you can explain separately in a viva.</p>''',

 '''<div class="kicker">Rule 3</div><h2>Comments say WHY</h2>
    <pre class="bad">i = i + 1    <span class="bad"># increment i</span></pre>
    <p class="dim">Noise. The line already says that.</p>
    <pre>    <span class="hl"># Inclusive: a student on exactly min_cgpa is eligible.</span>
    return student.cgpa &gt;= criteria.min_cgpa</pre>
    <p class="big">The second one would have prevented a Day 1 bug.</p>''',

 '''<div class="center"><h1>Clean code isn't decoration.</h1>
    <p class="big hl">It's bug prevention.</p>
    <p class="big dim">Half the bugs on Day 1 were only hard to find<br>
    because the code was unclear.</p></div>''',

 '''<h2>Naming quick reference</h2>
    <table><tr><th>Bad</th><th>Good</th><th>Why</th></tr>
    <tr><td><code>d</code></td><td><code>students_by_branch</code></td><td>Says what's in it</td></tr>
    <tr><td><code>tmp2</code></td><td><code>eligible</code></td><td>Says its role</td></tr>
    <tr><td><code>flag</code></td><td><code>is_placed</code></td><td>Booleans read as questions</td></tr>
    <tr><td><code>process()</code></td><td><code>shortlist()</code></td><td>Verbs say the action</td></tr>
    <tr><td><code>data</code></td><td><code>raw_csv_rows</code></td><td>"data" means nothing</td></tr></table>
    <p class="dim">Exception: <code>i</code> in a short loop is fine. Don't
    over-correct.</p>''',

 '''<h2>The developer loop</h2>
    <pre>   WRITE  -->  TEST  -->  REFACTOR WITH AI  -->  VERIFY
                              ^                     |
                              +------ commit -------+</pre>
    <p class="big warn">Refactor only when tests are green.</p>
    <p class="dim">Otherwise you can't tell whether the AI broke it,
    or it was already broken.</p>''',

 '''<h2>Why that order matters</h2>
    <div class="grid">
    <div class="card no"><h3>✕ Refactor while red</h3>
    <p>Tests fail after. Was it the AI? Was it already broken?</p>
    <p class="bad">You cannot tell. You've lost the thread.</p></div>
    <div class="card ok"><h3>✓ Refactor while green</h3>
    <p>Tests fail after? <b>The refactor did it.</b></p>
    <p class="hl">One command to undo.</p></div>
    </div>''',

 '''<div class="kicker">Exercise · 25 minutes</div>
    <h2>Refactor a Day 1 fix</h2>
    <p>Pick any tier 1–2 bug you already fixed.</p>
    <ol><li><b>Run the tests first.</b> Confirm green.</li>
    <li>Rename everything properly. Split anything doing two jobs.</li>
    <li>Run the tests again. <b>Still green?</b></li></ol>
    <p class="big warn">If they go red, you changed behaviour — not style.</p>''',

 '''<h2>Refactoring vs rewriting</h2>
    <table><tr><th>Refactoring</th><th>Rewriting</th></tr>
    <tr><td>Behaviour <b>identical</b></td><td>Behaviour changes</td></tr>
    <tr><td>Tests stay green throughout</td><td>Tests need updating</td></tr>
    <tr><td>Small, reversible steps</td><td>Big bang</td></tr>
    <tr><td class="hl">Safe</td><td class="bad">Where bugs come from</td></tr></table>
    <p class="big">AI will happily rewrite when you asked it to refactor.
    <span class="warn">Watch for that.</span></p>''',

 '''<h2>Session 1 close</h2>
    <ul><li>Names that say what · one job per function · comments say why</li>
    <li>Refactor only when green</li>
    <li>Unreadable code hides bugs — you proved it on slide 5</li></ul>
    <p class="big">Next: the safety net that makes all of this reversible.</p>''',
]

S2 = [
 '''<div class="kicker">Day 3 · Session 2 · 11:30–13:00</div>
    <h1>Git as your<br>AI safety net</h1>''',

 '''<h2>Four commands. That's today.</h2>
    <pre>git status                 <span class="dim"># what have I changed?</span>
git add -A &amp;&amp; git commit -m "working: tests green"
git diff                   <span class="dim"># what did the AI just do?</span>
git reset --hard HEAD      <span class="dim"># undo everything uncommitted</span></pre>
    <p class="big">Not git mastery. <span class="hl">Just the safety net.</span></p>''',

 '''<div class="center"><h1>Commit <span class="hl">before</span><br>you prompt.</h1>
    <p class="big dim">Then any AI change is one command away from gone.</p></div>''',

 '''<h2>The commit that saves you</h2>
    <pre>python3 run_tests.py          <span class="hl"># green?</span>
git add -A
git commit -m "working: eligibility fixed"

<span class="dim"># NOW let the AI touch it</span></pre>
    <p class="big">Message doesn't have to be beautiful.</p>
    <p class="dim">"working: X done" is enough. The point is the
    <b>restore point</b>, not the prose.</p>''',

 '''<div class="kicker">Invariant #4, again</div><h2><code>git diff</code></h2>
    <pre>+   def shortlist(students, criteria):
-       return [s for s in students if ok(s)]
+       result = []
+       for s in students:
+           if ok(s):
+               result.append(s)
+       return result</pre>
    <p class="big">You asked for a bug fix. It rewrote the function.</p>
    <p class="warn">That's scope creep — and only the diff shows it.</p>''',

 '''<h2>Reading a diff</h2>
    <table><tr><th>Symbol</th><th>Means</th></tr>
    <tr><td><code class="bad">-</code> red line</td><td>Removed</td></tr>
    <tr><td><code class="hl">+</code> green line</td><td>Added</td></tr>
    <tr><td>plain line</td><td>Unchanged, shown for context</td></tr>
    <tr><td><code>@@ -12,7 +12,9 @@</code></td><td>Where in the file</td></tr></table>
    <p class="big">Look for changes you <span class="warn">didn't ask for</span>.
    That's the whole skill.</p>''',

 '''<div class="center"><div class="kicker">Live demo</div>
    <h1>Let's wreck the repo<br>on purpose.</h1>
    <p class="big">Commit. Ask an AI to "make it more extensible."<br>
    Watch what arrives.</p></div>''',

 '''<h2>What we just saw</h2>
    <ol><li>Committed a working state</li>
    <li>Asked for "improvement"</li>
    <li>Got 40 lines where 6 were fine</li>
    <li><b>Tests still passed</b></li>
    <li><code>git reset --hard HEAD</code> — gone</li></ol>
    <p class="big warn">Step 4 is the scary one.</p>''',

 '''<div class="center"><h1>Green tests don't mean<br>
    <span class="hl">it was a good change.</span></h1>
    <p class="big dim">Tests check behaviour.<br>
    They don't check whether you can still explain it.</p></div>''',

 '''<h2>The AI trap list — from your own three days</h2>
    <table><tr><th>Trap</th><th>Looks like</th></tr>
    <tr><td>Bloat</td><td>40 lines where 6 would do</td></tr>
    <tr><td>Invented APIs</td><td>A method that doesn't exist</td></tr>
    <tr><td>Wrong defaults</td><td><code>.get(k, 0)</code> when <code>None</code> was meant</td></tr>
    <tr><td>Over-abstraction</td><td>A class hierarchy for one function</td></tr>
    <tr><td>Confident wrongness</td><td>A docstring that contradicts the code</td></tr>
    <tr><td>Scope creep</td><td>You asked for a fix, it rewrote the file</td></tr></table>''',

 '''<h2>Which trap costs you the viva?</h2>
    <div class="ask">Bloat and over-abstraction.</div>
    <p>Invented APIs crash immediately — you'll catch those.</p>
    <p class="big warn">Bloat <b>passes every test</b> and then you can't
    explain why there are 40 lines.</p>
    <p class="quote">"Why is this a class?"<br>"…the AI did that."<br>
    Zero marks.</p>''',

 '''<h2>Your 60-second review</h2>
    <ul><li>Read <b>every</b> line</li>
    <li>Does the docstring match the code?</li>
    <li><code>git diff</code> — did it touch anything I didn't ask about?</li>
    <li>Run the tests. Not just the happy path.</li>
    <li>Test the boundary. Test empty.</li>
    <li>Could this be shorter?</li>
    <li><b>Can I explain every line out loud?</b></li></ul>
    <p class="warn">If the last one is no — you cannot submit it.</p>''',

 '''<div class="kicker">Before lunch</div>
    <h2>Everyone commits a clean state</h2>
    <pre>python3 run_tests.py
git add -A
git commit -m "working: end of day 3 morning"</pre>
    <p class="big">This is your restore point for the assessment.</p>
    <p class="dim">Hands up when it's done.</p>''',

 '''<h2>Session 2 close</h2>
    <p class="quote">Commit before you prompt.<br>
    Read the diff before you accept.<br>
    Reset when it goes wrong.</p>
    <p class="big warn">After lunch: 90 minutes, graded, hidden tests.</p>''',
]

S3 = [
 '''<div class="kicker">Day 3 · Session 3 · 13:45–15:15</div>
    <h1>Mock assessment</h1>
    <p class="big dim">90 minutes · graded · any tool allowed</p>''',

 '''<h2>The brief</h2>
    <pre>day3/mock/BRIEF.md</pre>
    <p class="big warn">Read the whole thing before you write anything.</p>
    <p class="dim">In your repo. Also on screen. Read it twice —
    the second read is where the marks are.</p>''',

 '''<h2>Three parts</h2>
    <table><tr><th>Part</th><th>What</th><th>Time</th></tr>
    <tr><td class="num">A</td><td>Fix 2 bugs in <code>drive.py</code></td><td>30 min</td></tr>
    <tr><td class="num">B</td><td>Build <code>generate_drive_report()</code></td><td>45 min</td></tr>
    <tr><td class="num">C</td><td>Commit your work</td><td>15 min</td></tr></table>
    <p class="dim">Part C is worth marks. Don't skip it.</p>''',

 '''<h2>What Part B must return</h2>
    <table><tr><th>Key</th><th>Type</th><th>Meaning</th></tr>
    <tr><td><code>company</code></td><td>str</td><td>from criteria</td></tr>
    <tr><td><code>eligible</code></td><td>list[str]</td><td>names, <b>best first</b></td></tr>
    <tr><td><code>rejected</code></td><td>list[dict]</td><td><code>{name, reason}</code></td></tr>
    <tr><td><code>eligible_count</code></td><td>int</td><td>how many</td></tr>
    <tr><td><code>eligibility_rate</code></td><td>float</td><td>percent, 2dp</td></tr></table>
    <p class="warn">Exactly these keys. No more, no fewer.</p>''',

 '''<h2>The rules in the brief</h2>
    <ul><li>"Best first" = CGPA, then fewest backlogs, then roll number</li>
    <li><code>reason</code> is the <b>first</b> criterion they fail</li>
    <li>Empty list → rate is <code>0.0</code>, not a crash</li>
    <li>The input list must <b>not</b> be modified</li></ul>
    <p class="big warn">Every one of those is tested.</p>''',

 '''<div class="center"><h1>There are hidden tests<br>you cannot see.</h1>
    <p class="big">Re-read the brief.</p>
    <p class="big hl">Every rule in it is tested.</p></div>''',

 '''<h2>How 100 marks split</h2>
    <table>
    <tr><td>Part A — both bugs fixed, minimally</td><td class="num">15</td></tr>
    <tr><td>Part B — visible tests</td><td class="num">20</td></tr>
    <tr><td>Part B — <b>hidden tests</b></td><td class="num">20</td></tr>
    <tr><td>Clean code</td><td class="num">10</td></tr>
    <tr><td>Git hygiene</td><td class="num">5</td></tr>
    <tr><td><b>Viva — explaining your code</b></td><td class="num">30</td></tr>
    </table>''',

 '''<div class="center"><h1>30 marks for<br>explaining it.</h1>
    <p class="big dim">That's not padding.</p>
    <p class="big hl">In a real interview it's closer to 100%.</p></div>''',

 '''<h2>Your strategy</h2>
    <ol><li><b>Read the brief twice.</b> Underline every rule.</li>
    <li>Run the tests. See what's already failing.</li>
    <li><b>Part A first</b> — it's 15 marks and it's quick.</li>
    <li>Commit as soon as A is green.</li>
    <li>Part B. Reuse what's in <code>placement_tracker/</code>.</li>
    <li>Test the edge cases yourself before you stop.</li></ol>''',

 '''<h2>Reuse beats rewriting</h2>
    <p><code>placement_tracker/</code> already has code you can use.</p>
    <p class="big">Writing it again from scratch is
    <span class="warn">wasted time and extra bugs</span>.</p>
    <div class="ask">A real interviewer notices this. "Did you check what
    already existed?" is a question they actually ask.</div>''',

 '''<div class="center"><div class="kicker">Start</div>
    <h1>90 minutes.</h1>
    <p class="big">Any tool allowed.</p>
    <p class="warn">You must be able to explain every line.</p></div>''',

 '''<div class="center"><div class="kicker">30 minutes gone</div>
    <h1>Part A should be done.</h1>
    <p class="big">Green? <span class="hl">Commit now.</span></p></div>''',

 '''<div class="center"><div class="kicker">40 minutes left</div>
    <h1>Part B — start now</h1>
    <p class="big dim">If you haven't started the feature,
    stop fixing and start building.</p></div>''',

 '''<div class="center"><div class="kicker">10 minutes left</div>
    <h1 class="warn">Commit what works.</h1>
    <p class="big">A committed partial solution beats an
    uncommitted perfect one.</p></div>''',

 '''<div class="center"><div class="kicker">Time</div><h1>Stop.</h1>
    <p class="big">Hands off keyboards.</p>
    <p class="dim">Viva in 15 minutes. Look over your own code —
    you're about to explain it.</p></div>''',
]

S4 = [
 '''<div class="kicker">Day 3 · Session 4 · 15:30–17:00</div>
    <h1>Code defense</h1><p class="big dim">The viva · 30 marks</p>''',

 '''<h2>Format</h2>
    <ul><li><b>5 minutes each.</b> Called at <b>random</b>.</li>
    <li>I pick one function. You walk me through it, line by line.</li>
    <li>Then 2–3 questions.</li></ul>
    <p class="dim">Not everyone will be called. Everyone should be ready —
    that's why it's random.</p>''',

 '''<h2>How 30 marks split</h2>
    <table>
    <tr><td><b>Line-by-line walkthrough</b></td><td class="num">10</td></tr>
    <tr><td>Complexity</td><td class="num">5</td></tr>
    <tr><td>Edge cases</td><td class="num">5</td></tr>
    <tr><td>Design justification</td><td class="num">5</td></tr>
    <tr><td><b>Honesty about AI use</b></td><td class="num">5</td></tr>
    </table>''',

 '''<div class="center"><h1>Honesty is marked<br><span class="hl">UP.</span></h1>
    <div class="grid" style="margin-top:1.5em">
    <div class="card ok"><h3>✓ Scores higher</h3>
    <p>"The AI wrote this line and I don't fully understand it."</p></div>
    <div class="card no"><h3>✕ Scores zero</h3>
    <p>A confident bluff that collapses on one follow-up.</p></div>
    </div></div>''',

 '''<h2>Why honesty scores</h2>
    <p>I'm not testing whether you used AI. <b>Everyone used AI.</b></p>
    <p class="big">I'm testing whether you <span class="hl">know what you
    don't know</span>.</p>
    <p class="dim">An engineer who flags uncertainty is safe to hire.
    One who bluffs ships bugs into production and can't explain them.</p>''',

 '''<h2>The strike rule</h2>
    <p class="quote">Any line you cannot explain is struck from your
    submission — and scores zero in Parts A and B, even if the tests pass.</p>
    <p class="big warn">This is the rule that makes the other 70 marks real.</p>''',

 '''<h2>Walkthrough questions</h2>
    <ul><li>Walk me through this function, line by line.</li>
    <li>Why a <code>list</code> here and not a <code>dict</code>?</li>
    <li>What happens on the <b>first</b> iteration of that loop?</li>
    <li>What's the value of <code>reason</code> when the student
    <b>is</b> eligible?</li></ul>''',

 '''<h2>Complexity questions</h2>
    <ul><li>What's the time complexity? <b>Point at the line that dominates.</b></li>
    <li>You sort inside the function — what does that cost?</li>
    <li>5000 students instead of 5. What breaks first?</li>
    <li>Could you do this in one pass? Would you <b>want</b> to?</li></ul>
    <p class="dim">You met an O(n²) that timed out on Day 1. Same idea.</p>''',

 '''<h2>Answering a complexity question</h2>
    <pre class="bad">"It's O(n)."</pre>
    <p class="dim">Fine. Forgettable.</p>
    <pre>"O(n log n) — the loop over students is O(n), but the
 sort dominates at O(n log n). Space is O(n) because
 I build a new list rather than modify the input."</pre>
    <p class="big">Point at the line. <span class="hl">Always point at the line.</span></p>''',

 '''<h2>Edge case questions</h2>
    <ul><li>What happens with an empty list? <b>Show me.</b></li>
    <li>A student exactly on the CGPA bar — eligible? Where's that decided?</li>
    <li>Two students, identical CGPA and backlogs. What decides the order?</li>
    <li>What if <code>allowed_branches</code> is empty?</li></ul>
    <p class="warn">"I didn't handle that" is an acceptable answer.
    "I didn't think about it" is not.</p>''',

 '''<h2>AI questions — everyone gets one</h2>
    <ul><li>Which parts did AI write? Which did you change?</li>
    <li>Did it suggest anything you <b>rejected</b>? Why?</li>
    <li>How did you check it was right?</li>
    <li>What would you have done with <b>no AI</b> today?</li></ul>
    <p class="big hl">Question 2 is the one that impresses.</p>''',

 '''<div class="center"><h1>"I rejected its first answer<br>because it mutated the input list."</h1>
    <p class="big hl">That single sentence is a job offer.</p>
    <p class="big dim">It proves you reviewed, understood,<br>
    and had the judgement to say no.</p></div>''',

 '''<h2>Watching counts too</h2>
    <p>Most of you won't be called. <b>Watch anyway.</b></p>
    <p class="big">You'll learn nearly as much from 14 vivas
    as from giving one.</p>
    <p class="dim">Note the answers that landed. Note the ones that
    fell apart. That's your interview prep, free.</p>''',

 '''<div class="kicker">Debrief</div><h2>The best answers we heard</h2>
    <p class="big">And why they worked.</p>''',

 '''<h2>Three days</h2>
    <table><tr><th>Day 1</th><th>Day 2</th><th>Day 3</th></tr>
    <tr><td>Find it</td><td>Delegate it</td><td>Defend it</td></tr>
    <tr><td>The loop</td><td>The invariants</td><td>The viva</td></tr>
    <tr><td>Hypothesis first</td><td>Review the diff</td><td>Explain every line</td></tr>
    </table>
    <p class="big">One method, three settings.</p>''',

 '''<div class="center"><h1>Find it. Explain it.<br><span class="hl">Defend it.</span></h1>
    <p class="big">With or without AI.</p>
    <p class="quote">The tools will all be different in a year.<br>
    The method won't.</p></div>''',

 '''<div class="center"><h1 class="hl">Good luck<br>with your placements.</h1>
    <p class="big dim">Everything from these three days<br>
    stays in the repo. Keep using it.</p></div>''',
]

DECKS = [
 ("day3-s1.html", "DAY 3 · S1", "Day 3 S1 — Clean Code & the Dev Loop", S1),
 ("day3-s2.html", "DAY 3 · S2", "Day 3 S2 — Git as an AI Safety Net", S2),
 ("day3-s3.html", "DAY 3 · S3", "Day 3 S3 — Mock Assessment", S3),
 ("day3-s4.html", "DAY 3 · S4", "Day 3 S4 — Code Defense & Viva", S4),
]
