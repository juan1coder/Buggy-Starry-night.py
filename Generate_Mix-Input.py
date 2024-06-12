import random
import datetime

# List of main ideas
main_ideas = [
    "A whimsical image featuring a cat in the center, clouds, sun, rainbow, rain, fog, smoke, neon colors",
    "plague doctor samurai geisha cyborg",
    "futuristic knight with dragon",
    "steampunk astronaut in victorian dress",
    "cyberpunk detective in neon city",
    "mythical forest guardian with animal companions"
]

# List of artists
artists = [
    "Pascal Blanche",
    "Hermann Stenner",
    "Simon Stalenhag",
    "Gustavé Doré",
    "Alex Grey",
    "Alphonse Mucha",
    "Nekro",
    "Josan Gonzalez",
    "Vincent van Gogh",
    "Paul Gauguin",
    "Edvard Munch",
    "Egon Schiele",
    "Franz Marc",
    "Wassily Kandinsky",
    "Gustav Klimt",
    "Odilon Redon",
    "Arnold Böcklin",
    "Grant Wood",
    "Katsushika Hokusai",
    "Yoshitaka Amano",
    "Akira Toriyama",
    "Utagawa Kuniyoshi",
    "Rembrandt",
    "Cezanne",
    "Caravaggio",
    "Botticelli",
    "Michelangelo"
]

# List of colors
colors = [
    "black and white",
    "green and yellow",
    "red and blue",
    "purple and orange",
    "pink and teal",
    "cyan and magenta",
    "gold and silver",
    "neon colors"
]

# List of extra details
extra_details = [
    "Jugendstil",
    "graceful",
    "delicate",
    "daintiness",
    "svelte",
    "vivid colors",
    "intense black shadows",
    "film noir",
    "vibrating colors",
    "symmetry",
    "hyper detailed",
    "trending on artstation",
    "octane render",
    "8K resolution",
    "4K resolution",
    "16K resolution",
    "detailed",
    "render on trainstation",
    "halftone colors",
    "pencil drawing",
    "2D",
    "brush stroke",
    "charcoal drawing",
    "lithograph",
    "colorful comic",
    "volumetric lighting",
    "isometric",
    "3D",
    "texture",
    "hyper realism",
    "intricate",
    "photographic",
    "Realism",
    "Monet"
]

# List of emotional characteristics
emotional_characteristics = [
    "highly atmospheric",
    "dreamy",
    "moody",
    "gloomy",
    "dark",
    "whimsical",
    "ethereal",
    "rage",
    "joy",
    "grace",
    "dynamic",
    "sad",
    "blue",
    "nightmarish",
    "spooky",
    "Gothic",
    "breathtaking",
    "passionate",
    "sober",
    "cold",
    "neutral",
    "nostalgic",
    "mysterious",
    "hopeful",
    "serene"
]

def generate_prompt(user_main_idea, user_emotional_characteristics):
    # Use a random main idea if user input is empty
    if not user_main_idea.strip():
        user_main_idea = random.choice(main_ideas)
    
    # Randomly select 3 artists
    selected_artists = random.sample(artists, 3)
    
    # Randomly select colors
    selected_colors = random.choice(colors)
    
    # Randomly select 5 extra details
    selected_extra_details = random.sample(extra_details, 5)
    
    # If user doesn't provide emotional characteristics, add 3 random ones
    user_emotional_characteristics = [emotion.strip() for emotion in user_emotional_characteristics if emotion.strip()]
    if not user_emotional_characteristics:
        user_emotional_characteristics = random.sample(emotional_characteristics, 3)
    elif len(user_emotional_characteristics) == 1:
        existing_emotion = user_emotional_characteristics[0]
        remaining_emotions = [emotion for emotion in emotional_characteristics if emotion != existing_emotion]
        additional_emotions = random.sample(remaining_emotions, 2)
        user_emotional_characteristics = [existing_emotion] + additional_emotions

    # Create the prompt
    prompt = {
        "main_idea": user_main_idea,
        "artists": selected_artists,
        "colors": selected_colors,
        "extra_details": selected_extra_details,
        "emotional_characteristics": user_emotional_characteristics
    }
    
    return prompt

# Get user input for the main idea
user_main_idea = input("Enter your creative idea: ").strip()

# Get user input for emotional characteristics
user_emotional_characteristics = input("Enter emotional characteristics (comma-separated): ").strip().split(",")

# Generate and print a random prompt
prompt = generate_prompt(user_main_idea, user_emotional_characteristics)
print(prompt)

# Format the prompt as a detailed description
formatted_prompt = f"""Main Idea: {prompt['main_idea']}
Artists: {', '.join(prompt['artists'])}
Colors: {prompt['colors']}
Extra Details: {', '.join(prompt['extra_details'])}
Emotional Characteristics: {', '.join(prompt['emotional_characteristics']) if prompt['emotional_characteristics'] else 'None provided'}"""

print("\nFormatted Prompt:")
print(formatted_prompt)

# Create a unique name tag with the current date and time
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
unique_name_tag = f"art_prompt_{current_time}"

# Save the formatted prompt to a file in the /tmp folder
output_file_path = f"/tmp/{unique_name_tag}.txt"
with open(output_file_path, "w") as file:
    file.write(formatted_prompt)

print(f"\nPrompt saved to {output_file_path}")

