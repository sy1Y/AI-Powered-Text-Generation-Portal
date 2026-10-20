
from pathlib import Path
import random
import re
import html

# Define the location of the original dataset
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "corrupt_movie_corpus.txt"
OUTPUT_FILE = BASE_DIR / "cleaned_movie_corpus.txt"


def clean_text(text):
    """Remove unwanted noise while preserving meaningful dialogue."""

    # Decode HTML entities, such as &amp; and &quot;.
    text = html.unescape(text)

    # Remove HTML formatting tags.
    text = re.sub(r"</?(?:i|b|span)\b[^>]*>", " ", text, flags=re.I)

    # Remove standalone random noise symbols.
    text = re.sub(r"\^\^", " ", text)
    text = re.sub(r"(?<!\w)[@$%]+(?!\w)", " ", text)

    # Remove unwanted control characters.
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)

    # Normalize extra whitespace.
    text = re.sub(r"\s+", " ", text)

    return text.strip()



def preprocess_data():
    """Clean the dataset and save the results."""

    with open(INPUT_FILE, "r", encoding="utf-8-sig") as file:
        original_lines = file.read().splitlines()

    # Apply the cleaning function to each record.
    cleaned_lines = [clean_text(line) for line in original_lines]

    # Save the cleaned dataset without changing the original.
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(cleaned_lines) + "\n")

    # Count modified records.
    changed_records = sum(
        original != cleaned
        for original, cleaned in zip(original_lines, cleaned_lines)
    )

    # Validate the number of records.
    assert len(original_lines) == len(cleaned_lines)

    print("\n=== Cleaning Results ===")
    print(f"Original records: {len(original_lines)}")
    print(f"Cleaned records: {len(cleaned_lines)}")
    print(f"Modified records: {changed_records}")
    print(f"Output file: {OUTPUT_FILE.name}")

    
    # Validate the cleaned dataset.
    remaining_html = sum(
        bool(re.search(r"</?(?:i|b|span)\b[^>]*>", line, re.I))
        for line in cleaned_lines
    )

    remaining_noise = sum(
        bool(re.search(r"\^\^|(?<!\w)[@$%]+(?!\w)", line))
        for line in cleaned_lines
    )

    empty_after = sum(
        not line.strip() for line in cleaned_lines
    )

    print("\n=== Validation Results ===")
    print(f"Remaining HTML tags: {remaining_html}")
    print(f"Remaining noise symbols: {remaining_noise}")
    print(f"Empty records after cleaning: {empty_after}")

    assert remaining_html == 0, "HTML tags remain."
    assert remaining_noise == 0, "Noise symbols remain."


    # Display five before-and-after examples.
    print("\n=== Before and After Examples ===")

    shown = 0

    for original, cleaned in zip(original_lines, cleaned_lines):
        if original != cleaned:
            print(f"\nBefore: {original[:200]}")
            print(f"After:  {cleaned[:200]}")
            shown += 1

        if shown >= 5:
            break


def explore_data():
    """Explore the original movie dialogue dataset."""

    # Read the original dataset
    with open(INPUT_FILE, "r", encoding="utf-8-sig") as file:
        lines = file.read().splitlines()

    # Count total and empty records
    total_records = len(lines)
    empty_records = sum(not line.strip() for line in lines)

    print("=== Dataset Exploration ===")
    print(f"Total records: {total_records}")
    print(f"Empty records: {empty_records}")
    print("Primary language: English")
    print("Data format: Plain text (one dialogue record per line)")

    # Identify HTML tags
    html_count = sum(
        bool(re.search(r"</?[a-zA-Z][^>]*>", line))
        for line in lines
    )

    # Identify random noise symbols
    noise_count = sum(
        bool(re.search(r"\^\^|(?<!\w)[@$%]+(?!\w)", line))
        for line in lines
    )

    # Identify URLs
    url_count = sum(
        bool(re.search(r"https?://|www\.", line))
        for line in lines
    )

    # Identify extra whitespace
    whitespace_count = sum(
        bool(re.search(r" {2,}|\t", line))
        for line in lines
    )

    print("\n=== Data Quality Issues ===")
    print(f"Records containing HTML tags: {html_count}")
    print(f"Records containing noise symbols: {noise_count}")
    print(f"Records containing URLs: {url_count}")
    print(f"Records containing extra whitespace: {whitespace_count}")

    # Select 10 reproducible random samples
    random.seed(42)
    sample_indices = random.sample(
        range(total_records),
        min(10, total_records)
    )

    print("\n=== Sample Original Records ===")

    for index in sample_indices:
        print(f"\nRecord {index + 1}:")
        print(lines[index][:300])


if __name__ == "__main__":
    explore_data()
    preprocess_data()
