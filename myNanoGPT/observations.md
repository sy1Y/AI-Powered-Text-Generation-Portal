
# Week 5 – Movie Dialogue Text Generation Observations

## 1. Objective

The goal of Week 5 was to train a small character-level GPT model using the cleaned movie dialogue dataset from Week 3 and generate new text using NanoGPT.

## 2. Dataset Preparation

- Dataset: Cleaned movie dialogue corpus from Week 3
- Original records: 304,713
- Total characters: 16,948,556
- Vocabulary size: 92 unique characters
- Training tokens: 15,253,700 (90%)
- Validation tokens: 1,694,856 (10%)

I adapted NanoGPT's `prepare.py` to tokenize the movie dialogue dataset and generate `train.bin`, `val.bin`, and `meta.pkl`.

## 3. Model Configuration

I trained a small character-level GPT model on my laptop using CPU.

- Batch size: 12
- Block size: 64
- Transformer layers: 4
- Attention heads: 4
- Embedding dimension: 128
- Dropout: 0.0
- Maximum iterations: 2,000
- Evaluation interval: 250
- Evaluation iterations: 20

## 4. Training Loss Observations

The training loss generally decreased as training progressed.

| Iteration | Training Loss |
|-----------|---------------|
| 0 | 4.5270 |
| 150 | 3.4139 |
| 1000 | 1.9115 |
| 1040 | 1.8055 |
| 1080 | 1.7247 |
| 1870 | 1.5431 |
| 1880 | 1.4419 |
| 1890 | 1.5457 |
| 1900 | 1.4897 |
| 1910 | 1.4624 |
| 1920 | 1.4899 |
| 1930 | 1.6988 |
| 1940 | 1.4321 |
| 1950 | 1.5005 |
| 1960 | 1.4786 |
| 1970 | 1.5451 |
| 1980 | 1.5122 |
| 1990 | 1.6927 |

### Observations

- The training loss decreased significantly from approximately 4.53 to around 1.4–1.7 in later iterations.
- The loss fluctuated between iterations, but the overall trend was downward.
- The improvement became more gradual during later training.
- Training was relatively slow because the model was running on CPU.
- The decrease in training loss suggests that the model was learning patterns from the movie dialogue dataset.
- Further evaluation using validation loss would be necessary to assess generalization and overfitting.

## 5. Text Generation Results

After training, I successfully generated text using `sample.py` and the saved model checkpoint.

Examples of generated text:

> How I didn't think about of one the woman concer of here.

> I've just happened?

> Right. I'm sue your schoole was before the were she gount anything to SIRE WKE Sherk.

> Yeah.

### Observations

- The model generated English text with recognizable words and sentence-like structures.
- Some outputs resembled conversational dialogue.
- The generated text included punctuation and short responses commonly found in movie conversations.
- However, many sentences contained spelling mistakes, grammatical errors, and unclear meanings.
- The model learned basic character and language patterns but did not consistently generate coherent dialogue.

## 6. Issues Encountered and Fixes

Training stopped near iteration 1990 because of a `ZeroDivisionError` in the learning rate scheduling function.

The error was caused by a zero denominator in the learning rate decay calculation.

I updated `config.py` with the following settings:

```python
max_iters = 2000
lr_decay_iters = 2000
warmup_iters = 100
```

I then checked the configuration and confirmed that the denominator was 1900 instead of zero.

The configuration check passed successfully.

A previously saved checkpoint (`out_movies/ckpt.pt`) was available and successfully used for text generation, so restarting the entire training process was unnecessary.

The complete training run was not repeated after the configuration fix.

## 7. Conclusion

In Week 5, I successfully prepared my cleaned movie dialogue dataset for NanoGPT, trained a character-level GPT model on CPU, and generated new movie-style text.

The training loss showed a clear overall decrease, indicating that the model learned patterns from the dataset.

Although the generated text was not always grammatically correct or coherent, the experiment demonstrated the complete workflow from text preprocessing and tokenization to model training and text generation.

For future improvements, I could experiment with additional training, different model configurations, and generation parameters to improve text quality.
