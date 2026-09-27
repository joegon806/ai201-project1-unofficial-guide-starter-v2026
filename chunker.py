"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass
from pathlib import Path

import config
from ingest import Document

# Splits a paragraph after '.', '!' or '?' when whitespace follows. The corpus is
# plain prose with no abbreviations ("e.g.", "Dr.") to trip it up, so this is
# good enough here — it would need more care on messier text.
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def source_name(source: str) -> str:
    """'guide_halden_bay.md' -> 'halden bay'. The 'guide_' prefix says nothing."""
    return Path(source).stem.removeprefix("guide_").replace("_", " ")


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    One sentence per chunk, prefixed with where that sentence came from.

    Every chunk reads "<place>, <section>: <sentence>" — for example
    "halden bay, Eat and drink: Everything closes by 9pm...". The corpus is a
    set of guides that all use the same headings, so a bare sentence like
    "Buses run four times a day" is useless on its own: nothing in it says which
    town it describes. Folding the filename and the heading into the chunk text
    puts that context where the embedding can see it, not just in the citation.

    Splitting per sentence rather than per section keeps each chunk to roughly
    one fact, so a question about parking doesn't have to match a paragraph that
    is mostly about restaurants.
    """
    chunks: list[Chunk] = []

    for doc in documents:
        name = source_name(doc.source)

        # Group the document's lines into sections.
        # A line that starts with '#' is a Markdown heading, so it opens a new section.
        # Anything before the first heading gets a section of its own.
        sections: list[list[str]] = []
        for line in doc.text.splitlines():
            if line.startswith("#") or not sections:    # if this is the start of a new page or a header
                sections.append([])                     # create a new section
            sections[-1].append(line)                   # append the line to the section

        # then turn each sentence of each section into a Chunk
        index = 0
        for section in sections:
            header = section[0].lstrip("#").strip() if section[0].startswith("#") else ""

            # Join the body onto one line first — paragraphs wrap mid-sentence,
            # so a single sentence can span two lines.
            body = " ".join(line.strip() for line in section[1:] if line.strip())

            # The top heading repeats the place name ("# Halden Bay"), so in that
            # one section the header adds nothing.
            prefix = f"{name}, {header}" if header and header.lower() != name else name

            for sentence in SENTENCE_END.split(body):
                sentence = sentence.strip()
                if sentence:
                    chunks.append(
                        Chunk(
                            text=f"{prefix}: {sentence}",
                            source=doc.source,
                            index=index,
                            produced_by="chunker.py::split_documents",
                        )
                    )
                    index += 1

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
