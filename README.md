# 🍱 Anime-Inspired Recipe Generator

A fun and creative AI-powered application that generates anime-themed recipes like Naruto Ramen or Food Wars-inspired sushi rolls. Built with Python, Streamlit, and open-source language models.

---

## 🌟 Features

- 🤖 Anime-style recipe generation using open-source LLMs
- 📊 Nutritional data validation via free nutrition APIs
- 🍜 Customizable recipe suggestions with ingredients and instructions
- 🎨 (Optional) Image generation for recipes using DALL·E or Stable Diffusion
- 📱 User-friendly interface built with Streamlit

---

## 🧰 Tech Stack

| Layer        | Tools / Services Used                                 |
|--------------|--------------------------------------------------------|
| Frontend     | Streamlit                                              |
| Backend      | Python, Transformers (Hugging Face LLMs)               |
| AI Models    | Mistral-7B (optional), Open Source via Hugging Face    |
| Nutrition API| [OpenFoodFacts](https://world.openfoodfacts.org/)      |

---

## 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/anime-recipe-generator.git
cd anime-recipe-generator

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

