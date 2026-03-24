# visuotactile-multimodal-literature-review
PRISMA-based literature review on visuo-tactile multimodal learning

# Visuo-Tactile Multimodal Literature Review

## Research Topic

Fusion multimodale visuo-tactile et langage pour la compréhension et la description des propriétés des objets.

## Objective

This project aims to perform a systematic literature review using the PRISMA methodology on visuo-tactile multimodal learning and its extension to language-based understanding.

## Methodology

### 1. Article Collection

Articles were collected using academic databases (IEEE, Google Scholar, Scopus) with predefined search queries.

### 2. Screening Process

A two-step filtering process was applied:

* Manual filtering based on title and abstract
* Automated screening using a local LLM (qwen3:8b via Ollama)

### 3. Inclusion Criteria

* Use of vision + tactile modalities
* Multimodal learning or fusion
* Object property understanding (texture, material, stability)
* Optional: language integration

### 4. Exclusion Criteria

* Vision-only or tactile-only approaches
* Medical or unrelated domains
* No relevance to object understanding

### 5. PRISMA Flow

The PRISMA diagram summarizes:

* Number of articles identified
* Screening steps
* Final selected papers

## Structure

* data/: datasets and screening results
* scripts/: LLM-based filtering scripts
* prisma/: PRISMA counts
* queries/: search strategies

## Tools

* Python
* Ollama
* qwen3:8b LLM

## Author

Rodney Augustin

