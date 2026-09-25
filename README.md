# The Unofficial Guide

Joseph Gonzales; corpus: city_guides

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This system searches through city guide documents so it can answer your questions about them. It can answer questions about aspects of a city, such as food, transport, or attractions, as well as questions about the cities in general, such as good seasons or the best places to visit overall. The system will answer your question to the best of its ability and cite the document from which it got its information.

## Chunking Strategy

**Chunk size:** One section (Header + Following paragraphs)

**Overlap:** None

The documents in city_guides are uniformly structured such that each section pertains to a single topic and is started with a markdown header. This makes the sections perfect to be turned into chunks, with each chunk pertaining to a single topic and distinguished by headers.

## Sample Chunks

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `guide_corry_vale.md#6` — produced by: `chunker.py::split_documents`

```
## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: `guide_givens_mill.md#3` — produced by: `chunker.py::split_documents`

```
## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `guide_kestrelford.md#6` — produced by: `chunker.py::split_documents`

```
## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::split_documents`

```
## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.
```

## Sample Answer

**Question:** "Where is the nearest full hospital?"

**Answer:** According to `guide_accessibility.md`, the nearest full hospital is in Marchwood. However, the other guides (`guide_thornby_wells.md`, `guide_kestrelford.md`, `guide_pellew_sands.md`, `guide_halden_bay.md`, `guide_givens_mill.md`, `guide_elder_ness.md`, and `guide_marchwood.md`) state that the nearest full hospital is in Brightwater.

Sources retrieved: guide_accessibility.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

**My relevance cutoff:** 0.7

| Question | In corpus? | Best distance |
|---|---|---|
| "Where is the nearest full hospital?" | Yes | 0.313 |
| "Which month is excellent everywhere?" | Yes | 0.476 |
| "Where does every railway line in the region meet?" | Yes | 0.476 |
| "Which city has no public transport of any kind?" | Yes | 0.580 |
| "What’s the main cuisine in Halden Bay?" | Yes | 0.317 |
| "What is the capital of Mongolia?" | No | 0.754 |
| "How do I change the oil in a diesel engine?" | No | 0.892 |
| "Who won the 1994 World Cup?" | No | 0.899 |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.846 |
| "How do I write a for loop in Rust?" | No | 0.813 |

## How I Used AI

**1.**
After I wrote the last two acceptance criteria, I asked Claude to tell me how it would test them. Claude responded with clear test instructions, flagging conditions, and pass conditions, showing me that my criteria are clear and testable.

**2.**
Additionally, after I wrote my own code for the new chunker function, I asked Claude if there is a more efficient way to write it. In response, Claude rewrote my chunker code to fix bugs I had overlooked and to use a more efficient algorithm. 

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 4/4 | 4/4 | 4/4 | MET |
| 3. Gate stops out-of-corpus questions | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. A chunk is a section of a document | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Each answer is accompanied with a direct quote | 5 of 5 | 0 of 4 | 0 of 4 | 0 of 4 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Real Outputs:

### Criterion 1. Retrieved chunk contains the answer
File: chunker.py; Function: split_documents

```
Where is the nearest full hospital? — run 1
...
**[2] `guide_thornby_wells.md#7`** — distance 0.4339 (chunked by `chunker.py::split_documents`)

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```


### Criterion 2. Every answer names a source
File: generate.py; Function: answer_from_chunks

```
Based on `guide_accessibility.md`, the nearest full hospital is in Marchwood. (Note: The other documents state that the nearest full hospital is in Brightwater.)
```

### Criterion 3. Gate stops out-of-corpus questions
File: app.py; Function: _ask_one
```
>python app.py ask "What's 2+2"                    
(best distance 0.839, cutoff 0.7)

I don't have enough information about that.
```

### Criterion 4. A chunk is a section of a document
File: chunker.py; Function: split_documents

```
Where is the nearest full hospital? — run 1
...
**[2] `guide_thornby_wells.md#7`** — distance 0.4339 (chunked by `chunker.py::split_documents`)

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

### Criterion 5 (MISSED). Each answer is accompanied with a direct quote
File: generate.py; Function: answer_from_chunks

```
Which city has no public transport of any kind? — run 2
...
Elder Ness has no public transport of any kind, according to `guide_elder_ness.md`.
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer. | MET | For each of the questions, at least one of the chunks retrieved does include the correct answer. Unless you disqualify Question 3 ("every railway line"), whose chunks did not include the sentence that directly answers the question, and instead includes a sentence that indirectly answers the question.
| REVISED-1 | For at least 4 of 5 questions, at least one of the top three retrieved chunks contain the answer. | MISSED | Question 4 ("no public transport")'s answer, while correct, is found in the top 8th chunk, not in the top 3. Additionally, the top 3 chunks of Question 3 ("every railway line"), which did not yield an answer, do not contain the sentence that directly answers the question (although, the very top chunk does indirectly reference the correct answer).
| 2 | Every answer names a source. | MET | All of the answers directly name which document(s) it got its answer info from, because this functionality is baked into the answer-generation prompt.
| 3 | Gate stops out-of-corpus questions. | MET | All of the out-of-corpus questions yielded high distance, did not call the model, and responded with the refusal statement.
| NEW | Gate does not stop in-corpus questions. | MISSED | This new criterion is inspired by Criterion 3. Missed because the system failed to answer Question 3 ("every railway line").
| 4 | A chunk is a section of a document. | MET | Every chunk retrieved follows the header-and-paragraphs structure designed in split_documents in chunker.py.
| REVISED-4 | A chunk contains useful information. | MISSED | This revision of Criterion 4 aims to address the effect of the chunk rather than its design. Missed because some chunks are only a header with no paragraph.
| REVISED-4 | A chunk only contains one fact of information. | MISSED | Directly inspired by the failure of Question 3 ("every railway line"), and also builds off of Criterion 4. Question 3 failed because the direct answer to the question was contained as a small sentence in a larger chunk, such that the rest of the chunk was irrelevant and lowered the distance score.
| 5 | Each answer is accompanied with a direct quote. | MISSED | None of the answers provide a direct quote, because neither the answer-generation prompt nor the code have functionality implemented for direct quotes.

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
