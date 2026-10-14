
import csv

import requests
from bs4 import BeautifulSoup


# Target website for the web scraping assignment
URL = "https://www.scrapethissite.com/pages/simple/"
OUTPUT_FILE = "countries.csv"


def scrape_countries():
    """Retrieve and extract country data from the website."""

    # Step 1: Fetch the webpage
    response = requests.get(URL, timeout=20)
    response.raise_for_status()

    # Step 2: Parse the HTML document
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find all country containers
    country_elements = soup.find_all("div", class_="country")

    if not country_elements:
        raise ValueError("No country elements were found on the page.")

    countries = []

    # Step 4: Extract information from each country
    for country in country_elements:
        name_tag = country.find("h3", class_="country-name")
        capital_tag = country.find("span", class_="country-capital")
        population_tag = country.find("span", class_="country-population")
        area_tag = country.find("span", class_="country-area")

        # Skip incomplete records
        if not all([name_tag, capital_tag, population_tag, area_tag]):
            print("Warning: Skipping a country with missing fields.")
            continue

        name = name_tag.get_text(strip=True)
        capital = capital_tag.get_text(strip=True)
        population = int(population_tag.get_text(strip=True).replace(",", ""))
        area = float(area_tag.get_text(strip=True).replace(",", ""))

        countries.append({
            "Name": name,
            "Capital": capital,
            "Population": population,
            "Area": area,
        })

    return countries


def save_to_csv(countries):
    """Save the extracted country data to a CSV file."""

    fieldnames = ["Name", "Capital", "Population", "Area"]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(countries)


def main():
    try:
        countries = scrape_countries()

        if not countries:
            print("No valid country records were extracted.")
            return

        save_to_csv(countries)

        print(f"Successfully scraped {len(countries)} countries.")
        print(f"Data saved to {OUTPUT_FILE}")

        print("\nFirst five countries:")
        for country in countries[:5]:
            print(country)

        names = [country["Name"] for country in countries]

        if len(names) != len(set(names)):
            print("Warning: Duplicate country names detected.")
        else:
            print("\nValidation: No duplicate country names found.")

    except requests.RequestException as error:
        print(f"Network error: {error}")

    except (ValueError, TypeError) as error:
        print(f"Data processing error: {error}")


if __name__ == "__main__":
    main()
