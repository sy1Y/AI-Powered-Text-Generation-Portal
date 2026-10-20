# Assignment — NLP Text Preprocessing and Data Cleaning

## Project Overview

The objective of this assignmet is to explore a noisy text dataset, identify data quality issues, and implement a Python preprocessing pipeline to produce cleaner text for future NLP and text generation tasks.

## Dataset

- **Filename:** `corrupt_movie_corpus.txt`
- **Source:** Instructor-provided dataset
- **Format:** Plain text (.txt)
- **Language:** Primarily English
- **Content:** Movie dialogue
- **Total records:** 304,713
- **Empty records:** 0

Each line is treated as one text record. The original dataset is preserved without modification.

The dataset was provided directly by the instructor. Its original public source URL and license information were not specified.

## Data Exploration

Initial exploration identified the following issues:

| Data Quality Issue | Records Detected |
|---|---:|
| HTML tags | 266,748 |
| Random noise symbols | 266,506 |
| URLs | 18 |
| Extra whitespace | 0 |
| Empty records | 0 |

The dataset contains formatting tags such as `<i>`, `<b>`, and `</span>`, along with random noise symbols including `@`, `$`, `%`, and `^^`.

Ten random records were sampled using a fixed random seed of 42 to make the exploration reproducible.

## Text Preprocessing

The Python script `preprocess.py` performs the following operations:

1. Decodes HTML entities.
2. Removes common HTML formatting tags.
3. Removes standalone noise symbols.
4. Removes unwanted control characters.
5. Normalizes whitespace.

Meaningful punctuation, capitalization, contractions, negation, and verb tenses are preserved whenever possible.

Stopword removal, stemming, and lemmatization are intentionally excluded because this dataset may be used for future text generation tasks.

## Project Files

- `corrupt_movie_corpus.txt` — Original unclean dataset.
- `cleaned_movie_corpus.txt` — Cleaned output.
- `preprocess.py` — Data exploration, cleaning, and validation script.
- `README.md` — Project documentation.
- `exploration_report.md` — Exploration findings and before-and-after examples.

## How to Run

From the root directory of the GitHub repository, run:

```powershell
uv run --no-project python wk3_text_preprocessing/preprocess.py
```

The script uses only Python standard-library modules, so no additional packages are required.

## Results and Validation

- Original records: **304,713**
- Cleaned records: **304,713**
- Modified records: **304,713**
- Remaining targeted HTML tags: **0**
- Remaining targeted noise symbols: **0**
- Empty records after cleaning: **0**

The original and cleaned datasets have the same number of records.

## Limitations

The cleaning process does not automatically correct spelling mistakes or reconstruct incomplete dialogue. A small number of URLs may remain because they were not automatically classified as irrelevant.

The preprocessing pipeline focuses on removing identifiable formatting noise while preserving the meaning and structure of the original text.

## Conclusion

This assignment demonstrates a basic NLP preprocessing workflow, including dataset exploration, text cleaning, output generation, and validation.

The resulting text corpus is cleaner and more suitable for subsequent NLP experiments and text generation development.