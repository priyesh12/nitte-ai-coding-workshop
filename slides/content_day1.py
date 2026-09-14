# -*- coding: utf-8 -*-
"""Day 1 — UNDERSTAND. Four session decks."""

S1 = [
 '''<div class="kicker">Day 1 · Session 1 · 09:30–11:00</div>
    <h1>UNDERSTAND</h1><p class="big dim">Code execution &amp; common bugs</p>
    <p class="dim">AI-Enabled Coding &amp; Debugging for Placement</p>''',

 '''<h2>Get set up — 10 minutes</h2>
    <pre>git clone &lt;URL on the board&gt;
cd nitte-ai-coding-workshop
python3 check_setup.py
python3 run_tests.py bugs</pre>
    <p class="big">Expect <span class="hl">18 passing, 16 failing</span></p>
    <p class="dim">No git? Green <b>Code</b> button → Download ZIP.<br>
    Stuck 3 minutes? Hand up — pair with a neighbour.</p>''',

 '''<div class="center"><h1 class="hl">The failures<br>are the workshop.</h1></div>''',

 '''<h2>Three days</h2>
    <table>
    <tr><td class="num">1</td><td><b>UNDERSTAND</b><br><span class="dim">Debug without AI. Build the reflex.</span></td></tr>
    <tr><td class="num">2</td><td><b>DELEGATE</b><br><span class="dim">Drive any AI tool. Distrust every output.</span></td></tr>
    <tr><td class="num">3</td><td><b>DELIVER</b><br><span class="dim">Ship it. Then defend every line.</span></td></tr>
    </table>
    <p class="dim">09:30–11:00 · 11:30–13:00 · 13:45–15:15 · 15:30–17:00</p>''',

 '''<div class="kicker">Why today has no AI until 1:45</div>
    <h2>Most placement tests ban AI</h2>
    <p class="quote">Today you learn to do it without.<br>Tomorrow you learn to do it with.</p>
    <p>The people who get placed can do <span class="hl">both</span>.</p>
    <p class="dim">And in every interview, the tell is whether you can explain your own fix.</p>''',

 '''<h2>What actually happens in a screening test</h2>
    <ul>
    <li>You get code that <b>almost</b> works</li>
    <li>Some tests are <b>visible</b>. Most are <b>hidden</b>.</li>
    <li>60–90 minutes. No internet. Often no AI.</li>
    <li>They watch <b>how</b> you work, not just the final answer</li>
    </ul>
    <p class="big warn">Rewriting from scratch is the #1 way people fail.</p>''',

 '''<h2>Three kinds of bug</h2>
    <div class="grid3">
    <div class="card no"><h3>Syntax</h3><p>Python can't read your file.</p>
    <p class="dim">Nothing runs at all.</p><p class="hl">Easiest.</p></div>
    <div class="card maybe"><h3>Runtime</h3><p>It runs, then crashes.</p>
    <p class="dim">You get a traceback.</p><p class="warn">Medium.</p></div>
    <div class="card ok" style="border-top-color:var(--bad)"><h3>Logic</h3>
    <p>It runs. It finishes. It's <b>wrong</b>.</p>
    <p class="dim">No error at all.</p><p class="bad">Hardest.</p></div>
    </div>
    <p class="big">Which kind do you think costs the most marks?</p>''',

 '''<div class="kicker">Type 1</div><h2>Syntax errors</h2>
    <pre class="bad">def greet(name, company)
                        ^
SyntaxError: expected ':'</pre>
    <p>Python never even started. <b>Zero</b> of your code ran.</p>
    <p class="dim">Missing <code>:</code> <code>)</code> <code>"</code> · wrong indentation · a stray comma</p>
    <div class="ask">The caret points where the parser <b>gave up</b> —
    not always where you went wrong. Always check the line <b>above</b> too.</div>''',

 '''<div class="kicker">Type 2</div><h2>Runtime errors</h2>
    <pre class="warn">total = 0
for cgpa in cgpas:
    total = total + cgpa
return total / len(cgpa)     <span class="dim"># cgpa, not cgpas</span>

TypeError: object of type 'float' has no len()</pre>
    <p>Half your code ran, then it hit something impossible.</p>
    <p class="hl">The error names the type. The type tells you the fix.</p>''',

 '''<div class="kicker">Type 3 — the dangerous one</div>
    <h2>Logic errors</h2>
    <pre class="bad">def is_eligible(cgpa, backlogs):
    <span class="dim"># spec: "CGPA of 7.0 or above"</span>
    return cgpa &gt; 7.0 and backlogs &lt;= 1</pre>
    <p>No crash. No traceback. No warning.</p>
    <p class="big bad">Every student with exactly 7.0 is silently rejected.</p>
    <div class="ask">How would you ever notice this?</div>''',

 '''<div class="center"><h1>No traceback<br><span class="hl">≠ no bug</span></h1>
    <p class="big dim">The worst bugs don't crash.<br>They quietly give the wrong answer.</p></div>''',

 '''<div class="kicker">The one thing to remember</div>
    <h2>The debugging loop</h2>
    <pre><span class="num">1.</span> REPRODUCE     make it fail on demand
<span class="num">2.</span> HYPOTHESISE   write it down   <span class="warn">← ON PAPER</span>
<span class="num">3.</span> ISOLATE       prove which line
<span class="num">4.</span> FIX           smallest possible change
<span class="num">5.</span> VERIFY        green, nothing else broken</pre>
    <p class="big">AI is allowed from step 3. <span class="warn">Not before.</span></p>''',

 '''<h2>Step 1 — Reproduce</h2>
    <p>If you can't make it fail <b>on demand</b>, you cannot know you fixed it.</p>
    <pre>python3 run_tests.py bugs/tier0</pre>
    <ul><li>What exact input causes it?</li>
    <li>Does it fail <b>every</b> time, or sometimes?</li>
    <li>What is the <b>smallest</b> input that still fails?</li></ul>
    <p class="dim">Shrinking the input is half the diagnosis.</p>''',

 '''<h2>Step 2 — Hypothesise <span class="warn">← the whole workshop</span></h2>
    <p>One sentence, on paper, before you touch anything:</p>
    <pre class="info">"I think line 12 divides by len(cgpa) instead of
 len(cgpas), so it's taking len() of a float."</pre>
    <p>If you prompt an AI before this, you get a
    <span class="bad">confident answer to the wrong question</span>.</p>
    <p class="big">And in the viva you'll have nothing to say.</p>''',

 '''<h2>Steps 3–5</h2>
    <table>
    <tr><td class="num">3</td><td><b>Isolate</b><br>
    <span class="dim">Prove it. A print, a breakpoint, a smaller input.
    Don't guess — confirm.</span></td></tr>
    <tr><td class="num">4</td><td><b>Fix</b><br>
    <span class="dim">Smallest possible change. One character if possible.
    Never rewrite the function.</span></td></tr>
    <tr><td class="num">5</td><td><b>Verify</b><br>
    <span class="dim">Tests green — <b>and</b> nothing that used to pass now fails.</span></td></tr>
    </table>''',

 '''<div class="center"><h1>Smallest<br>possible fix.</h1>
    <p class="big dim">Rewriting the function hides what you learned<br>
    and breaks three things you didn't test.</p>
    <p class="warn">Graded on this today.</p></div>''',

 '''<div class="kicker">How we'll work</div><h2>Bug Hunt</h2>
    <ol><li><b>90 seconds silent.</b> No typing. Write one hypothesis.</li>
    <li>We collect <span class="hl">three wrong answers first.</span></li>
    <li>A student drives at the keyboard.</li>
    <li>Reproduce → isolate → fix.</li>
    <li><b>Post-mortem:</b> what was the smallest fix?</li></ol>
    <p class="dim">Being wrong out loud is the point. It's the exact thing
    that makes people freeze in interviews.</p>''',

 '''<div class="center"><div class="kicker">Bug Hunt #1</div>
    <h1>bug_01_greeting.py</h1>
    <p class="big">90 seconds. Silent. Pen down on a hypothesis.</p></div>''',

 '''<div class="kicker">Predict the output</div><h2>Drill 1</h2>
    <pre>marks = [10, 20, 30]
for i in range(1, len(marks)):
    print(marks[i])</pre>
    <div class="ask">What prints? And what did the author probably mean?</div>
    <p class="dim">Answer: 20, 30. The first element is silently skipped —
    <code>range(1, n)</code> starts at 1.</p>''',

 '''<div class="kicker">Predict the output</div><h2>Drill 2</h2>
    <pre>students = ["Asha", "Bhavya", "Chetan"]
for s in students:
    if s.startswith("B"):
        students.remove(s)
print(students)</pre>
    <div class="ask">Three names. Remove the B one. What's left?</div>
    <p class="dim">Answer: <code>['Asha', 'Chetan']</code> — correct here,
    but add a second B-name and it breaks. You'll meet this in bug_04.</p>''',

 '''<div class="kicker">Predict the output</div><h2>Drill 3</h2>
    <pre>print(10 / 3)
print(10 // 3)
print(10 % 3)
print(int(10 / 3))</pre>
    <div class="ask">Which of these gives 3? Which gives 3.333…?</div>
    <p class="dim">3.3333333333333335 · 3 · 1 · 3<br>
    <code>/</code> is always float in Python 3. <b>Always.</b></p>''',

 '''<div class="kicker">Predict the output</div><h2>Drill 4</h2>
    <pre>cgpa = 7.0
if cgpa &gt; 7.0:
    print("eligible")
else:
    print("rejected")</pre>
    <div class="ask">The rule is "7.0 or above". Is this right?</div>
    <p class="big bad">Prints "rejected". One character wrong.</p>''',

 '''<h2>Off-by-one &amp; boundaries</h2>
    <pre>  6.8   6.9   <span class="warn">7.0</span>   7.1   7.2
              ^
        "7.0 or above"

  cgpa &gt;  7.0    ○ open   — 7.0 EXCLUDED  <span class="bad">wrong</span>
  cgpa &gt;= 7.0    ● closed — 7.0 included  <span class="hl">right</span></pre>
    <p class="big warn">The #1 cause of hidden test failures.</p>
    <p class="dim">Whenever you read "or above", "at most", "up to",
    "at least" — stop and check the edge.</p>''',

 '''<h2>Words that hide a boundary</h2>
    <table><tr><th>Spec says</th><th>You need</th></tr>
    <tr><td>"7.0 or above", "at least 7.0"</td><td><code>&gt;= 7.0</code></td></tr>
    <tr><td>"above 7.0", "more than 7.0"</td><td><code>&gt; 7.0</code></td></tr>
    <tr><td>"at most 1 backlog", "up to 1"</td><td><code>&lt;= 1</code></td></tr>
    <tr><td>"fewer than 1", "under 1"</td><td><code>&lt; 1</code></td></tr>
    <tr><td>"top 3"</td><td class="warn">…what if there's a tie?</td></tr></table>
    <p class="dim">That last row is a real exercise later today.</p>''',

 '''<h2>Always ask: what input breaks this?</h2>
    <div class="grid">
    <div class="card"><h3>Empty</h3><p><code>[]</code> <code>""</code>
    <code>{}</code> <code>None</code> · <code>0</code></p></div>
    <div class="card"><h3>Boundary</h3><p>Exactly at the limit.
    One below. One above.</p></div>
    <div class="card"><h3>One element</h3><p>Loops and pairs
    often break at n=1.</p></div>
    <div class="card"><h3>Duplicates</h3><p>Two students,
    identical CGPA. Now what?</p></div>
    </div>
    <p class="big">Hidden tests are made of exactly these.</p>''',

 '''<div class="kicker">How we work today</div><h2>Pairs, rotating driver</h2>
    <ul><li>One <b>driver</b> (types), one <b>navigator</b> (reads, thinks)</li>
    <li><b>Swap every 10 minutes.</b> Enforced.</li>
    <li>The navigator is not allowed to touch the keyboard</li>
    <li>The driver is not allowed to change a line the navigator can't explain</li></ul>
    <p class="dim">This is how real engineers debug together — and it's a
    surprisingly common interview format.</p>''',

 '''<div class="center"><div class="kicker">Your turn · 25 minutes</div>
    <h1>tier0 → tier1</h1>
    <pre>python3 run_tests.py bugs/tier0</pre>
    <p class="big">Hypothesis on paper <span class="warn">before</span> you change anything.</p>
    <p class="dim">Swap driver every 10 minutes.</p></div>''',

 '''<div class="kicker">Buffer · if you're flying</div>
    <h2>Python gotchas quiz</h2>
    <pre>a = [1, 2, 3]
b = a
b.append(4)
print(a)          <span class="dim"># ?</span>

x = "5"
print(x * 3)      <span class="dim"># ?</span>

print(0.1 + 0.2 == 0.3)   <span class="dim"># ?</span></pre>
    <p class="dim">[1,2,3,4] — <code>b</code> is the same list, not a copy<br>
    "555" — string repetition, not arithmetic<br>
    False — and that one costs people their placement</p>''',

 '''<div class="kicker">Session 1 close</div><h2>What you should leave with</h2>
    <ul><li>Three kinds of bug — and logic errors are the dangerous ones</li>
    <li>The 5-step loop, with <b>hypothesis on paper</b> at step 2</li>
    <li>Smallest possible fix, never a rewrite</li>
    <li>Boundaries are where hidden tests live</li></ul>
    <p class="big">Next: reading tracebacks properly, and the print
    techniques that find what <code>print()</code> hides.</p>''',
]

S2 = [
 '''<div class="kicker">Day 1 · Session 2 · 11:30–13:00</div>
    <h1>Tracebacks<br>&amp; print logging</h1>
    <p class="big dim">Reading what Python is telling you</p>''',

 '''<h2>Read it BOTTOM-UP</h2>
    <pre>Traceback (most recent call last):        <span class="dim">ignore</span>
  File "run_tests.py", line 42, in main  <span class="dim">← 3. how you got here</span>
  File "bug_02.py", line 12              <span class="warn">← 2. WHERE</span>
    return total / len(cgpa)
TypeError: object of type 'float' has no len()
<span class="hl">← 1. WHAT — START HERE</span></pre>
    <p class="big">Last line = <b>what</b>. Line above = <b>where</b>.</p>''',

 '''<div class="center"><h1>Students read<br>top-down and panic.</h1>
    <p class="big hl">Read the last line first.</p>
    <p class="big dim">Usually that's enough.</p></div>''',

 '''<h2>The error decoder</h2>
    <table><tr><th>Error</th><th>Plain English</th><th>Look for</th></tr>
    <tr><td><code>SyntaxError</code></td><td>Couldn't read the file</td><td>Missing <code>:</code> <code>)</code> <code>"</code></td></tr>
    <tr><td><code>IndentationError</code></td><td>Spacing inconsistent</td><td>Tabs mixed with spaces</td></tr>
    <tr><td><code>NameError</code></td><td>No such name</td><td>Typo; used before defined</td></tr>
    <tr><td><code>TypeError</code></td><td>Wrong kind of thing</td><td><code>str + int</code>, <code>len()</code> of a number</td></tr>
    <tr><td><code>AttributeError</code></td><td>No such <code>.thing</code></td><td>It's probably <code>None</code></td></tr>
    <tr><td><code>IndexError</code></td><td>Past the end</td><td>Off-by-one</td></tr>
    <tr><td><code>KeyError</code></td><td>No such dict key</td><td><code>.get()</code> — mind the default</td></tr>
    <tr><td><code>ZeroDivisionError</code></td><td>Divided by zero</td><td>Empty list, unguarded <code>len()</code></td></tr>
    <tr><td><code>ValueError</code></td><td>Right type, impossible value</td><td><code>int("abc")</code></td></tr></table>''',

 '''<h2><code>TypeError</code> — read the type</h2>
    <pre class="bad">TypeError: object of type 'float' has no len()</pre>
    <p>It tells you: something is a <b>float</b> where you expected
    something with a length.</p>
    <pre>total / len(cgpa)     <span class="bad"># cgpa is one float</span>
total / len(cgpas)    <span class="hl"># cgpas is the list</span></pre>
    <p class="big">The type in the message <span class="hl">is</span> the clue.</p>''',

 '''<h2><code>AttributeError</code> — usually <code>None</code></h2>
    <pre class="bad">AttributeError: 'NoneType' object has no attribute 'name'</pre>
    <p>Something returned <code>None</code> and you used it anyway.</p>
    <pre>student = find_student(roll_no)   <span class="dim"># returns None if not found</span>
print(student.name)              <span class="bad"># boom</span></pre>
    <div class="ask">Where did the <code>None</code> come from?
    That's the real question — not where it crashed.</div>''',

 '''<h2>The caret lies (a little)</h2>
    <pre class="bad">def greet(name, company)
                        ^
SyntaxError: expected ':'</pre>
    <p>The caret shows where the parser <b>gave up</b>,
    not always where you went wrong.</p>
    <p class="big warn">For SyntaxError, always check the line ABOVE.</p>
    <p class="dim">An unclosed bracket on line 8 usually reports on line 9.</p>''',

 '''<h2>Three print techniques</h2>
    <pre>print(f"{cgpa=}")     <span class="dim"># cgpa=7.3    name AND value</span>
print(repr(cgpa))     <span class="dim"># 7.300000000000001</span>
breakpoint()          <span class="dim"># stop here.  n / c / q</span></pre>
    <p class="big"><code>f"{x=}"</code> is the one to build a habit on.</p>
    <p class="dim">You never mislabel a variable again.</p>''',

 '''<div class="center"><h1><code>repr()</code> finds bugs<br>
    <span class="hl">that <code>print()</code> hides.</span></h1>
    <pre>print(7.300000000000001)        <span class="dim"># 7.3</span>
print(repr(7.300000000000001))  <span class="hl"># 7.300000000000001</span></pre>
    <p class="big warn"><code>print()</code> is lying to you to be helpful.</p></div>''',

 '''<h2><code>breakpoint()</code> — the 4 commands</h2>
    <pre>breakpoint()          <span class="dim"># put this line in your code</span>

(Pdb) <span class="hl">n</span>     next line
(Pdb) <span class="hl">c</span>     continue (run to the end)
(Pdb) <span class="hl">q</span>     quit
(Pdb) <span class="hl">p x</span>   print the value of x</pre>
    <p>You can type <b>any</b> Python at the <code>(Pdb)</code> prompt.</p>
    <p class="dim">No install. Built into Python. Works on a locked-down lab machine.</p>''',

 '''<h2>Where to put the print</h2>
    <p>Not at the crash. <b>Before</b> it — where the value is still good.</p>
    <pre>def shortlist(students, min_cgpa):
    print(f"{len(students)=}")          <span class="hl"># entry</span>
    result = []
    for s in students:
        print(f"{s['name']=} {s['cgpa']=}")   <span class="hl"># each step</span>
        ...
    print(f"{len(result)=}")            <span class="hl"># exit</span></pre>
    <p class="big">Entry · each step · exit. That's the pattern.</p>''',

 '''<div class="center"><div class="kicker">Bug Hunt #2</div>
    <h1>bug_04_toppers.py</h1>
    <p class="big warn">This one does not crash.</p>
    <p class="big">It just keeps the wrong students.</p></div>''',

 '''<div class="kicker">Deep dive</div><h2>Mutating while iterating</h2>
    <pre class="bad">for student in students:
    if not student["placed"]:
        students.remove(student)</pre>
    <pre>index:  0       1        2
      [Asha,  Bhavya,  Chetan]
       ok     remove   
after: [Asha,  Chetan]
              ^ iterator now at index 2 = past the end
                <span class="bad">Chetan was never checked</span></pre>
    <p class="big">The list shrank under the loop.</p>''',

 '''<h2>Why it passes one test and fails the next</h2>
    <table><tr><th>Input</th><th>Result</th></tr>
    <tr><td>One unplaced student</td><td class="hl">Correct ✓</td></tr>
    <tr><td><b>Two unplaced, side by side</b></td><td class="bad">Skips one ✗</td></tr>
    <tr><td>Everyone unplaced</td><td class="bad">Keeps half ✗</td></tr></table>
    <p class="big warn">This is what a hidden test looks like.</p>
    <p class="dim">Your visible test passed. You shipped it. You failed.</p>''',

 '''<h2>The fix: build a new list</h2>
    <pre class="bad">for student in students:              <span class="bad"># mutating</span>
    if not student["placed"]:
        students.remove(student)</pre>
    <pre>return [s for s in students if s["placed"]]   <span class="hl"># new list</span></pre>
    <p class="big">Never modify a list you're looping over.</p>
    <p class="dim">Build a new one, or loop over a copy: <code>for s in students[:]</code></p>''',

 '''<div class="center"><h1>A green test proves<br>the test passed.</h1>
    <p class="big dim">Not that your code is right.</p></div>''',

 '''<div class="kicker">Deep dive</div><h2>The mutable default argument</h2>
    <pre class="bad">def register(name, drive=[]):
    drive.append(name)
    return drive

register("Asha")    <span class="dim"># ['Asha']</span>
register("Bhavya")  <span class="bad"># ['Asha', 'Bhavya']  ← ?!</span></pre>
    <p>The <code>[]</code> is created <b>once</b>, when the function is
    <b>defined</b> — not on each call.</p>
    <p class="big warn">Every call shares the same list.</p>''',

 '''<h2>The fix, and why it's an interview favourite</h2>
    <pre>def register(name, drive=None):
    if drive is None:
        drive = []
    drive.append(name)
    return drive</pre>
    <div class="ask">Try it yourself: <code>print(register.__defaults__)</code>
    between calls. You can watch the list grow.</div>
    <p class="dim">Asked constantly in Python interviews. Worth memorising
    as a pattern, not a rule.</p>''',

 '''<div class="kicker">Deep dive</div><h2>Floats don't do what you think</h2>
    <pre>&gt;&gt;&gt; 0.1 + 0.2
0.30000000000000004

&gt;&gt;&gt; 6.9 + 0.4
7.300000000000001

&gt;&gt;&gt; 6.9 + 0.4 == 7.3
<span class="bad">False</span></pre>
    <p>Computers store numbers in binary. <code>0.1</code> in binary is
    like <code>1/3</code> in decimal — it never ends.</p>''',

 '''<h2>Never use <code>==</code> on floats</h2>
    <pre class="bad">if cgpa == 7.3:          <span class="bad"># fails for computed values</span></pre>
    <pre>if abs(cgpa - 7.3) &lt; 1e-9:    <span class="hl"># tolerance</span></pre>
    <p class="big">Or better: <span class="hl">don't use floats for marks at all.</span></p>
    <p class="dim">Store CGPA × 100 as an integer. Or use <code>Decimal</code>.
    Banks don't store money as floats, and neither should you.</p>
    <div class="ask">Which fix would you defend in an interview — and why?
    Both are right. Say so.</div>''',

 '''<div class="center"><div class="kicker">Your turn · 35 minutes</div>
    <h1>tier2</h1>
    <pre>python3 run_tests.py bugs/tier2</pre>
    <p class="big">Use <code>f"{x=}"</code> and <code>repr()</code>.</p>
    <p class="dim">Hypothesis first. Swap driver every 10 minutes.</p></div>''',

 '''<div class="kicker">Buffer · stretch</div><h2><code>is</code> vs <code>==</code></h2>
    <pre>a = [1, 2]
b = [1, 2]
print(a == b)    <span class="dim"># True  — same contents</span>
print(a is b)    <span class="dim"># False — different objects</span>

x = "CSE"
y = "CSE"
print(x is y)    <span class="warn"># True... sometimes. Don't rely on it.</span></pre>
    <p class="big"><code>==</code> asks "same value?" · <code>is</code> asks
    "same object?"</p>
    <p class="dim">Only use <code>is</code> for <code>None</code>,
    <code>True</code>, <code>False</code>.</p>''',

 '''<div class="kicker">Buffer · stretch</div><h2>Shallow vs deep copy</h2>
    <pre>original = [["Asha"], ["Bhavya"]]
copy = original[:]          <span class="dim"># shallow</span>
copy[0].append("Chetan")
print(original)             <span class="bad"># [['Asha','Chetan'], ['Bhavya']]</span></pre>
    <p>The outer list is new. The inner lists are <b>the same objects</b>.</p>
    <pre>import copy
deep = copy.deepcopy(original)   <span class="hl"># fully independent</span></pre>''',

 '''<div class="kicker">Session 2 close</div><h2>What you should leave with</h2>
    <ul><li>Read tracebacks <b>bottom-up</b> — last line first</li>
    <li><code>f"{x=}"</code> and <code>repr()</code> as reflexes</li>
    <li>Never mutate a list you're iterating</li>
    <li>Never <code>==</code> on floats</li>
    <li>Mutable defaults are evaluated once</li></ul>
    <p class="big">After lunch: your first AI contact —
    and some strict rules about it.</p>''',
]

S3 = [
 '''<div class="kicker">Day 1 · Session 3 · 13:45–15:15</div>
    <h1>AI as explainer</h1>
    <p class="big dim">First contact — with rules</p>''',

 '''<h2>Nothing to install</h2>
    <p class="big">Any free AI in a browser. <span class="hl">Your phone is fine.</span></p>
    <p class="dim">ChatGPT · Gemini · Claude — free tiers all work.
    No account juggling, no keys, no setup. That comes tomorrow.</p>''',

 '''<h2>The rules for today</h2>
    <div class="grid">
    <div class="card ok"><h3>✓ Allowed</h3>
    <p>"explain this traceback"</p><p>"what does this line do"</p>
    <p>"what does this error mean"</p><p>"give me 3 edge cases"</p></div>
    <div class="card no"><h3>✕ Banned</h3>
    <p>"fix it"</p><p>"write this for me"</p><p>"solve this problem"</p></div>
    </div>
    <p class="big">AI is a <span class="hl">tutor</span> today,
    not a mechanic.</p>''',

 '''<div class="center"><h1>Why ban "fix it"?</h1>
    <p class="big">Because you'd learn nothing,<br>
    and tomorrow you'd trust it blindly.</p>
    <p class="quote">You cannot review code<br>you never understood.</p></div>''',

 '''<h2>AI is a genuinely great tutor</h2>
    <ul><li>Infinitely patient. Ask the same thing five times.</li>
    <li>Never makes you feel stupid for asking.</li>
    <li>Explains the <b>general concept</b> very well.</li>
    <li>Available at 2am the night before your test.</li></ul>
    <p class="big hl">Use it for this. It's genuinely better than most textbooks.</p>''',

 '''<h2>And a poor mechanic</h2>
    <ul><li>Confidently wrong about <b>your specific code</b></li>
    <li>Invents functions that don't exist</li>
    <li>Rewrites 40 lines when 1 character was wrong</li>
    <li>Agrees with you when you're wrong</li></ul>
    <p class="big warn">It has never seen your codebase. It's guessing —
    very fluently.</p>''',

 '''<h2>The prompt that teaches you something</h2>
    <pre class="info">Here is a Python traceback:

&lt;paste the WHOLE traceback&gt;

And here is the function it points at:

&lt;paste the function&gt;

Explain what this error means and what usually
causes it. <span class="hl">Do NOT fix it</span> — I want to find the bug myself.</pre>
    <p class="big">That last line is what makes it teaching.</p>''',

 '''<h2>The prompt that finds edge cases</h2>
    <pre class="info">Explain what this function does, step by step.

&lt;paste the function&gt;

Then tell me: <span class="hl">what input would make it
behave unexpectedly?</span></pre>
    <p class="big">The second question is where the value is.</p>
    <p class="dim">This is how you generate your own hidden tests.</p>''',

 '''<div class="center"><div class="kicker">Drill · 30 minutes</div>
    <h1>Explain a bug<br>you already fixed</h1>
    <p class="big">Take a bug from this morning. Ask AI to explain
    the <b>original</b> error.</p>
    <p class="warn">Compare it against what you actually found.</p></div>''',

 '''<h2>What to watch for</h2>
    <div class="ask">Did the AI describe the <b>bug class</b> correctly
    but get <b>your specific line</b> wrong?</div>
    <p>That gap is the most important thing you'll notice today.</p>
    <ul><li>General concept → usually excellent</li>
    <li>Your actual code → often generic, sometimes wrong</li></ul>
    <p class="big warn">Tomorrow you'll be trusting it with real code.
    Remember this feeling.</p>''',

 '''<div class="kicker">Drill · 30 minutes</div>
    <h2>Context changes everything</h2>
    <p>Ask about <code>bug_04</code> <b>twice</b>:</p>
    <ol><li>Paste <b>only</b> the function. Ask what's wrong.</li>
    <li>Now paste the function <b>and the failing test</b>. Ask again.</li></ol>
    <p class="big">Night and day.</p>
    <p class="dim">You just discovered invariant #1. It gets a name tomorrow.</p>''',

 '''<div class="center"><h1>AI is only as good<br>as the context you give it.</h1>
    <p class="big dim">Same model. Same question.<br>
    Completely different answer.</p></div>''',

 '''<h2>Prompts that get you in trouble</h2>
    <table><tr><th>Don't say</th><th>Because</th></tr>
    <tr><td>"fix this"</td><td>You get a rewrite and learn nothing</td></tr>
    <tr><td>"make it better"</td><td>"Better" is undefined — you get bloat</td></tr>
    <tr><td>"is this correct?"</td><td>It will usually just agree with you</td></tr>
    <tr><td>"optimise this"</td><td>Cleverness you can't explain in a viva</td></tr>
    <tr><td>"write a function to process students"</td><td>Vague in, invented out</td></tr></table>''',

 '''<div class="kicker">Group · 20 minutes</div>
    <h2>Where did it help? Where did it mislead?</h2>
    <p class="big">Real examples from the room. We're writing these
    on the board.</p>
    <p class="dim">Keep them. We reuse this list tomorrow when we take
    apart AI-written code that looks perfect.</p>''',

 '''<div class="kicker">Session 3 close</div><h2>The rule that carries forward</h2>
    <p class="quote">Hypothesis first.<br>Then ask.</p>
    <p>You now know what AI is good at (explaining) and
    what it's poor at (your specific code).</p>
    <p class="big">Next session is graded.
    <span class="warn">And your hypothesis is worth more than your fix.</span></p>''',
]

S4 = [
 '''<div class="kicker">Day 1 · Session 4 · 15:30–17:00</div>
    <h1>The practical</h1><p class="big dim">Graded · pairs · 60 minutes</p>''',

 '''<h2>Format</h2>
    <ul><li><b>4 bugs</b>, ones you haven't seen</li>
    <li><b>60 minutes</b>, in your pairs</li>
    <li><b>Hypothesis sheet handed in</b> — your own paper</li>
    <li>AI allowed — <span class="warn">but only after the hypothesis is written</span></li></ul>''',

 '''<h2>Your hypothesis sheet</h2>
    <pre>BUG # ____

1. Expected:
2. Actually got:
3. My hypothesis:          <span class="warn">← BEFORE any AI</span>
4. Fix (lines changed: __):
5. Was I right?  Y / partly / N</pre>
    <p class="dim">Fold a page in half. One bug per half-page.</p>''',

 '''<h2>How you're scored</h2>
    <table>
    <tr><td>Tests green</td><td class="num">4</td></tr>
    <tr><td><b>Hypothesis was correct</b></td><td class="num">3</td></tr>
    <tr><td><b>Fix was minimal</b> (no rewrites)</td><td class="num">2</td></tr>
    <tr><td>Explained it out loud</td><td class="num">1</td></tr>
    </table>
    <p class="big warn">You can score 6/10 without fixing anything.</p>''',

 '''<div class="center"><h1>Interviewers hire<br>the reasoning,<br>
    <span class="hl">not the keystrokes.</span></h1></div>''',

 '''<h2>Why "minimal fix" is worth marks</h2>
    <div class="grid">
    <div class="card no"><h3>✕ Rewrote the function</h3>
    <p>Can't say what was wrong.</p><p>Broke two things not tested.</p>
    <p class="dim">Interviewer: "so what was the bug?" — silence.</p></div>
    <div class="card ok"><h3>✓ Changed one character</h3>
    <p>Knows exactly what was wrong.</p><p>Nothing else could break.</p>
    <p class="dim">"<code>&gt;</code> should have been <code>&gt;=</code>." Hired.</p></div>
    </div>''',

 '''<div class="center"><div class="kicker">Start</div>
    <h1>60 minutes</h1>
    <pre>python3 run_tests.py bugs</pre>
    <p class="big">Reproduce → <span class="warn">hypothesise</span> →
    isolate → fix → verify</p></div>''',

 '''<div class="center"><div class="kicker">30 minutes gone</div>
    <h1>Halfway</h1>
    <p class="big">Stuck on one? <span class="hl">Move on.</span></p>
    <p class="dim">Come back. A fresh look beats twenty more minutes of staring.
    That's true in the real test too.</p></div>''',

 '''<div class="center"><div class="kicker">10 minutes left</div>
    <h1>Finish your sheets</h1>
    <p class="big warn">The sheet is worth more than the fix.</p>
    <p class="dim">Question 5 especially — "was I right?"
    An honest "no" scores.</p></div>''',

 '''<div class="kicker">Live solve · 30 minutes</div>
    <h2>The ones nobody got</h2>
    <p class="big">I'll drive. I'll think out loud.</p>
    <p class="dim">Including the parts where I don't know yet.
    That's what debugging actually looks like.</p>''',

 '''<h2>What we saw today</h2>
    <table><tr><th>Bug</th><th>Class</th><th>Lesson</th></tr>
    <tr><td>greeting</td><td>Syntax</td><td>Caret points where the parser gave up</td></tr>
    <tr><td>average</td><td>Runtime</td><td>The type in the message is the clue</td></tr>
    <tr><td>eligible</td><td><span class="warn">Boundary</span></td><td><code>&gt;</code> vs <code>&gt;=</code> — #1 hidden test killer</td></tr>
    <tr><td>toppers</td><td>Logic</td><td>Never mutate what you iterate</td></tr>
    <tr><td>register</td><td>Logic</td><td>Mutable defaults evaluate once</td></tr>
    <tr><td>cutoff</td><td>Logic</td><td>Never <code>==</code> on floats</td></tr></table>''',

 '''<div class="center"><h1>Every one of those<br>is a real screening test bug.</h1>
    <p class="big dim">Not a teaching exercise.<br>
    These are the actual failure modes.</p></div>''',

 '''<div class="kicker">Homework · 5 minutes · do it now</div>
    <h2>Get your free API key</h2>
    <pre>https://aistudio.google.com/apikey</pre>
    <p>Sign in with any Google account → <b>Create API key</b> → Copy</p>
    <pre><span class="dim">Mac/Linux</span>  echo 'export GEMINI_API_KEY="KEY"' &gt;&gt; ~/.zshrc
<span class="dim">Windows</span>    setx GEMINI_API_KEY "KEY"   <span class="dim">(reopen terminal)</span>
<span class="dim">Check</span>      echo $GEMINI_API_KEY</pre>
    <p class="warn">Free. No card. Day 2 does not work without it.</p>''',

 '''<h2>If it doesn't work</h2>
    <table><tr><th>Problem</th><th>Fix</th></tr>
    <tr><td>Prints nothing</td><td>Reopen the terminal completely</td></tr>
    <tr><td>Prints <code>$GEMINI_API_KEY</code></td><td>You're in CMD — use PowerShell</td></tr>
    <tr><td>Asks for billing</td><td>Wrong page. Use <b>aistudio.google.com</b></td></tr>
    <tr><td>College account blocked</td><td>Use a personal Gmail</td></tr>
    <tr><td>Stuck 15 min</td><td>Stop. You'll pair tomorrow. Fine.</td></tr></table>
    <p class="dim">Full steps: <code>harnesses/GET-YOUR-KEY.md</code> in your repo.</p>''',

 '''<div class="center"><div class="kicker">Tomorrow</div>
    <h1>DELEGATE</h1>
    <p class="big">Same skill. AI in the loop.</p>
    <p class="quote">The hypothesis rule doesn't go away.<br>
    It's the only thing that makes AI safe.</p></div>''',
]

DECKS = [
 ("day1-s1.html", "DAY 1 · S1", "Day 1 S1 — Code Execution & Common Bugs", S1),
 ("day1-s2.html", "DAY 1 · S2", "Day 1 S2 — Tracebacks & Print Logging", S2),
 ("day1-s3.html", "DAY 1 · S3", "Day 1 S3 — AI as Explainer", S3),
 ("day1-s4.html", "DAY 1 · S4", "Day 1 S4 — Debugging Practical", S4),
]
