from transformers import pipeline

# Load a public text generation model
generator = pipeline("text-generation", model="gpt2")

def generate_anime_recipe(character="Naruto", theme="ramen"):
    prompt = f"""You are an anime chef. Write a creative recipe inspired by the anime character {character} and their favorite food, {theme}.
Include:
- A fun anime-style title 🍜
- Ingredients list 🥕
- Cooking instructions 🍳
- Emojis and flair 🎌"""

    result = generator(prompt, max_new_tokens=200, temperature=0.8)
    return result[0]['generated_text']

# Run it
if __name__ == "__main__":
    print("\n🎌 Anime-Inspired Recipe:\n")
    print(generate_anime_recipe())
