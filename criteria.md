# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
In order to produce accurate answers, the system must be able to accurately find chunks that are close in distance to the question. The fifth question, "What's the main cuisine in Halden Bay?", however, does not use the same wording as the sentence that its answer comes from, so the system's distance AI might struggle to match the question to the chunk.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The system should cite a source document every time it presents an answer so the user knows what document the system got its information from and can verify that the information actually is in the document cited. Every test question asks about a sentence that is specifically and clearly stated in the documents, so the system should be able to cite at least one source document for every test answer.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in all 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
This prevents the system from giving inaccurate or hallucinated information to the user if the system does not have enough information from the documents to give an accurate answer based on them.

---

## 4. A chunk is a section of a document
A chunk consists of a section header and the paragraph(s) that immediately follow.

**Why this target:**
The documents in city_guides are uniformly formatted so that paragraphs that pertain to one general thought are sectioned under a header. This is a good basis for how the system will split the text into chunks.



---

## 5. Each answer is accompanied with a direct quote
If the system gives an answer, the system supports its answer with at least one quote from the source chunk(s) named which contains the appropriate information.

**Why this target:**
Giving a direct quote gives support to the system’s answer and shows exactly what sentence or phrase it got the answer from.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
