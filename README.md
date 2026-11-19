# Ethiopian Market Intelligence AI

Amharic-English product information extraction and price analytics for informal
online markets (starting with public fashion Telegram channels).

> Status: early development. Research baseline in `docs/research/`.

## Goal
Turn unstructured product ads into structured data (category, price, size, colour,
condition, language), match the same product across sellers, and analyse advertised
prices over time, then evaluate honestly where the models work and fail.

## Pipeline
1. Collection (Telethon, public channels only)
2. Preprocessing and language identification
3. Annotation (hand-labelled sample)
4. Extraction: rules baseline vs fine-tuned multilingual model vs LLM
5. Product matching with multilingual embeddings
6. Price analytics and Streamlit demo

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then fill in Telegram API credentials
```

## Structure
```
configs/    channel list and settings
data/       raw, interim, annotated, processed (git-ignored)
docs/       research, competitor tests
src/emi/    collection, preprocessing, extraction, matching, analytics
app/        Streamlit demo
tests/      unit tests
```

## Ethics and data
Only public channels, minimal personal data, no redistribution of raw posts.
Advertised price is not a transaction price, and ad frequency is not demand.
