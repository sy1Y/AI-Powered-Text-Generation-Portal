# Dataset Exploration Report

## 1. Objective

The purpose of this assignment is to explore a noisy text dataset, identify data quality issues, and apply appropriate Natural Language Processing (NLP) preprocessing techniques.

The cleaned text will serve as a potential input for future text generation experiments in the AI-Powered Text Generation Portal project.

## 2. Dataset Description

The dataset, `corrupt_movie_corpus.txt`, was provided by the instructor as an example of unclean textual data.

- **Dataset type:** Movie dialogue corpus
- **Primary language:** English
- **File format:** Plain text (.txt)
- **Data structure:** One dialogue record per line
- **Total records:** 304,713
- **Empty records:** 0
- **Original source:** Instructor-provided file
- **Public source URL:** Not specified
- **License:** Not specified

The original dataset was preserved without modification.

## 3. Data Exploration Method

The dataset was examined using Python.

The exploration process included:

1. Reading the original text file using UTF-8 encoding.
2. Counting the total number of records.
3. Checking for empty records.
4. Identifying common formatting problems using regular expressions.
5. Selecting 10 random text records with a fixed random seed (`42`) to ensure reproducibility.
6. Reviewing actual examples of noisy text before choosing preprocessing methods.

## 4. Identified Data Quality Issues

The initial exploration produced the following results:

| Data Quality Issue | Number of Records |
|---|---:|
| HTML formatting tags | 266,748 |
| Random noise symbols | 266,506 |
| URLs | 18 |
| Extra whitespace | 0 |
| Empty records | 0 |

### 4.1 HTML Formatting Tags

Many records contain HTML formatting tags such as `<b>`, `<i>`, and `</span>`.

These tags do not contribute to the meaning of the movie dialogue and can be removed.

### 4.2 Random Noise Symbols

The dataset contains random symbols such as `@`, `$`, `%`, and `^^` inserted between words.

These symbols are treated as noise when they appear as standalone formatting artifacts.

### 4.3 URLs

A small number of records contain URL-like patterns.

URLs were detected during exploration but were not automatically removed because their relevance was not individually verified.

### 4.4 Whitespace

No records containing repeated spaces or tab characters were detected using the initial exploration pattern.

However, removing HTML tags and noise symbols can introduce additional spaces, so whitespace normalization is still necessary.

### 4.5 Spelling and Dialogue Irregularities

Some records contain unusual spellings, incomplete sentences, informal expressions, or repeated punctuation.

These are not automatically corrected because they may reflect natural dialogue, character speech patterns, or meaningful stylistic choices.

## 5. Preprocessing Methods

The following techniques were implemented in `preprocess.py`:

| Technique | Purpose |
|---|---|
| HTML entity decoding | Convert encoded entities into readable characters |
| HTML tag removal | Remove formatting markup |
| Noise symbol removal | Remove standalone `@`, `$`, `%`, and `^^` artifacts |
| Control character removal | Remove unwanted non-printable characters |
| Whitespace normalization | Replace repeated whitespace with a single space |

The preprocessing pipeline preserves meaningful punctuation, capitalization, contractions, negation, and verb tenses.

Stopword removal, stemming, and lemmatization were not applied because these operations could reduce the quality of text intended for future generation tasks.

## 6. Before-and-After Examples

The following examples are taken from the actual instructor-provided dataset.

### Example 1 — HTML Tags and Noise Symbols

**Before:**

`I'm to take the Sikali with the main column to $ </span> the river <b>`

**After:**

`I'm to take the Sikali with the main column to the river`

**Explanation:** Removed an HTML tag and an unnecessary `$` symbol.

### Example 2 — Random Symbols

**Before:**

`Lord Chelmsford @ seems to @ want me to stay back with my @ Basutos.`

**After:**

`Lord Chelmsford seems to want me to stay back with my Basutos.`

**Explanation:** Removed standalone `@` symbols while preserving the sentence.

### Example 3 — Multiple HTML Tags

**Before:**

`</span> </span> <b> Yeah.`

**After:**

`Yeah.`

**Explanation:** Removed multiple HTML tags without changing the dialogue.

### Example 4 — Noise Within a Sentence

**Before:**

`Definitely. ^^ I suppose it all goes back to <i> Queen ^^ Elizabeth.`

**After:**

`Definitely. I suppose it all goes back to Queen Elizabeth.`

**Explanation:** Removed HTML markup and `^^` artifacts while preserving punctuation and capitalization.

### Example 5 — Mixed Formatting Noise

**Before:**

`</b> ... <b> just like the mouse. ^^`

**After:**

`... just like the mouse.`

**Explanation:** Removed formatting tags and noise while retaining the ellipsis.

## 7. Validation Results

After running the preprocessing script, the following results were obtained:

| Validation Check | Result |
|---|---:|
| Original records | 304,713 |
| Cleaned records | 304,713 |
| Modified records | 304,713 |
| Remaining targeted HTML tags | 0 |
| Remaining targeted noise symbols | 0 |
| Empty records after cleaning | 0 |

The preprocessing script successfully generated `cleaned_movie_corpus.txt`.

The record count remained unchanged, and the validation checks found no remaining targeted HTML tags or noise symbols.

## 8. Limitations

The preprocessing pipeline does not perform automatic spelling correction, sentence reconstruction, or semantic analysis.

URLs were identified but not removed automatically.

Some unusual punctuation and informal expressions remain because they may be meaningful in movie dialogue.

The dataset's original public source and license information were not provided by the instructor.

## 9. Conclusion

This assignment demonstrates a reproducible NLP preprocessing workflow using Python.

By exploring the dataset, identifying actual data quality issues, applying appropriate cleaning techniques, and validating the output, the original noisy movie dialogue corpus was transformed into a cleaner text dataset.

The cleaned corpus can be used as a starting point for future NLP and text generation experiments.