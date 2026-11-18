# AI-Powered Text Generation Portal

An end-to-end AI-powered text generation project developed as part of the Open Avenues Build Project. The project covers web scraping, text preprocessing, training a character-level GPT model, and building an interactive web application for movie-style dialogue generation.

## 1. Project Overview

The goal of this project was to explore the complete workflow of developing a text generation application, from data collection and preparation to language model training and web integration.

The final application uses a custom-trained nanoGPT model to generate movie-style dialogue through a Flask-based web interface.

The project was developed in Python, with model training performed locally on a CPU.

## 2. Project Workflow

### Week 2: Web Scraping

- Developed a Python web scraper using `requests` and `BeautifulSoup`.
- Extracted country names, capitals, populations, and areas from ScrapeThisSite.
- Organized the extracted information into a structured CSV file.
- Practiced collecting and storing data from web pages.

Directory: `wk2_web_scraping/`

*This was an independent web scraping exercise. The scraped country data was not used to train the final language model.*

### Week 3: Text Preprocessing

- Prepared a movie dialogue corpus for language model training.
- Implemented text cleaning and preprocessing in Python.
- Explored the dataset and documented preprocessing observations.
- Generated a cleaned text corpus for subsequent training.

Directory: `wk3_text_preprocessing/`

### Weeks 4–5: Language Model Training

- Explored the nanoGPT framework and its training pipeline.
- Practiced training a small GPT model using a sample dataset.
- Prepared the movie dialogue dataset for character-level language modeling.
- Trained an initial lightweight GPT model on the cleaned movie dialogue corpus.
- Conducted a second training run with a larger model architecture and a longer context window.

The final model was trained locally using CPU resources.

### Weeks 6–7: Web Application Development

- Developed a Flask backend to connect the trained model to a web application.
- Created a custom HTML interface with a vintage cinema-inspired design.
- Integrated text generation functionality using the trained nanoGPT checkpoint.
- Added a loading indicator and disabled the generation button while processing requests.
- Adjusted text generation settings to improve the output experience.

Directory: `myNanoGPT/`

## 3. Final Model Configuration

The final model is a character-level GPT trained on movie dialogue text using nanoGPT.

| Parameter | Final Configuration |
|---|---|
| Model Architecture | GPT-style Transformer |
| Transformer Layers | 6 |
| Attention Heads | 6 |
| Embedding Dimension | 192 |
| Context Length (Block Size) | 128 |
| Batch Size | 16 |
| Gradient Accumulation Steps | 1 |
| Training Iterations | 5,000 |
| Learning Rate | 0.001 |
| Minimum Learning Rate | 0.0001 |
| Warmup Iterations | 100 |
| Dropout | 0.2 |
| Training Device | CPU |
| Dataset | Movie Dialogue Corpus |

The final trained checkpoint is stored at:

`myNanoGPT/out_movies2/ckpt.pt`

The initial model used a smaller architecture with four Transformer layers, four attention heads, an embedding dimension of 128, and a context length of 64.

The second training run increased model capacity and training duration to explore improvements in text generation.

## 4. Web Application

The final application provides a simple interface for generating movie-style dialogue.

**Features:**
- Custom vintage cinema-inspired user interface.
- Text generation using a locally trained GPT model.
- Flask backend for handling generation requests.
- Loading feedback while the model generates text.
- Support for repeated text generation requests.

**Technologies:** Python, PyTorch, nanoGPT, Flask, HTML, CSS, and JavaScript.

## 5. Project Structure

```text
AI-Powered-Text-Generation-Portal/
├── wk2_web_scraping/
│   ├── scraper.py
│   └── countries.csv
├── wk3_text_preprocessing/
│   ├── preprocess.py
│   ├── cleaned_movie_corpus.txt
│   └── exploration_report.md
├── myNanoGPT/
│   ├── app.py
│   ├── index.html
│   ├── config.py
│   ├── model.py
│   ├── train.py
│   ├── sample.py
│   ├── configurator.py
│   ├── observations.md
│   ├── data/
│   │   └── movies/
│   │       ├── input.txt
│   │       ├── meta.pkl
│   │       └── prepare.py
│   └── out_movies2/
│       └── ckpt.pt
├── .gitignore
└── README.md
```

## 6. How to Run the Application

### Step 1: Clone the Repository

```bash
git clone https://github.com/sy1Y/AI-Powered-Text-Generation-Portal.git
cd AI-Powered-Text-Generation-Portal/myNanoGPT
```

### Step 2: Install Dependencies

Use a compatible Python environment and install the required packages:

```bash
python -m pip install torch numpy flask
```

### Step 3: Start the Flask Application

```bash
python app.py
```

### Step 4: Open the Web Interface

Open the following address in your browser:

`http://127.0.0.1:5000`

Click the generation button to generate movie-style dialogue.

**Note:** The application runs the model locally on a CPU, so text generation may take some time depending on the computer's hardware.

## 7. Results and Limitations

The project successfully demonstrated an end-to-end workflow for building a locally trained text generation application.

The final model can generate character-level text based on patterns learned from movie dialogue data and display the output through a functional web interface.

However, the generated dialogue may contain grammatical errors, incomplete sentences, or inconsistencies in meaning.

These limitations are associated with the relatively small model architecture, character-level tokenization, limited training iterations, and CPU-based training constraints.

Future improvements could include using a larger pretrained language model, subword tokenization, additional training data, and more extensive model evaluation.

## 8. Key Takeaways

Through this project, I gained practical experience in:

- Web scraping and structured data collection.
- Text cleaning and dataset preparation.
- Understanding and configuring GPT-style language models.
- Training and experimenting with Transformer architectures.
- Connecting machine learning models to Flask applications.
- Developing a user-facing interface for AI-generated content.
- Managing and documenting an end-to-end AI project using Git and GitHub.

This project helped me better understand the engineering workflow required to transform a language model experiment into an interactive application.
