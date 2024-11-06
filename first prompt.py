import tkinter as tk
import random

# List of bizarre prompts
prompts = [
    'A cat made of clouds playing chess with a robot dog on the moon.',
    'An upside-down mountain floating above a city of glass.',
    'A fish riding a bicycle through a field of stars.',
    'A giant snail carrying a library on its back across the desert.',
    'A time-traveling toaster trying to prevent breakfast disasters.',
    'A dancing tree with leaves that are butterflies.',
    'A mirror reflecting a world where gravity works in reverse.',
    'A submarine sailing through the skies above an endless ocean.',
    'A painter whose canvas paints back.',
    'An orchestra composed entirely of living shadows.',
]

# Lists of random words to use for substitutions
nouns = ['dragon', 'rainbow', 'clock', 'whisper', 'galaxy', 'sphinx', 'labyrinth', 'phantom', 'echo', 'illusion']
verbs = ['dancing', 'singing', 'whispering', 'melting', 'glowing', 'transforming', 'levitating', 'shapeshifting',
         'echoing', 'vanishing']
adjectives = ['invisible', 'ethereal', 'enigmatic', 'paradoxical', 'surreal', 'phantasmagorical', 'kaleidoscopic',
              'infinite', 'timeless', 'forgotten']
adverbs = ['silently', 'gracefully', 'mysteriously', 'endlessly', 'strangely', 'unexpectedly', 'paradoxically',
           'invisibly', 'melancholically', 'vividly']


def make_weirder(prompt):
    """
    Modify the given prompt in an even weirder and more surreal way.
    This function randomly replaces some words with other random words,
    and may append an extra surreal phrase at the end.
    """
    # Split the prompt into words
    words = prompt.split()

    # Randomly decide how many words to replace (up to 3)
    num_words_to_replace = random.randint(1, 3)

    # Get indices of words to replace
    indices = list(range(len(words)))
    random.shuffle(indices)
    indices = indices[:num_words_to_replace]

    # For each selected index, replace the word with a random one
    for idx in indices:
        # Decide which type of word to replace with
        replacement_type = random.choice(['noun', 'verb', 'adjective', 'adverb'])
        if replacement_type == 'noun':
            replacement_word = random.choice(nouns)
        elif replacement_type == 'verb':
            replacement_word = random.choice(verbs)
        elif replacement_type == 'adjective':
            replacement_word = random.choice(adjectives)
        elif replacement_type == 'adverb':
            replacement_word = random.choice(adverbs)
        else:
            replacement_word = words[idx]
        # Replace the word at the index
        words[idx] = replacement_word

    # Maybe insert a random surreal phrase at the end
    if random.random() < 0.5:
        # Construct a surreal phrase
        extra_phrase = 'while the {} {} {} {}'.format(
            random.choice(adjectives),
            random.choice(nouns),
            random.choice(verbs),
            random.choice(adverbs)
        )
        # Append the phrase to the words list
        words.append(extra_phrase)

    # Join the words back into a string
    weird_prompt = ' '.join(words)

    return weird_prompt


def generate_weird_interpretation():
    """
    Randomly selects a prompt and modifies it in an even weirder way.
    Updates the text widget in the tkinter window to display the weird interpretation.
    """
    # Randomly select a prompt
    prompt = random.choice(prompts)

    # Modify it to make it weirder
    weird_prompt = make_weirder(prompt)

    # Update the text widget in the tkinter window
    text_widget.delete('1.0', tk.END)  # Clear previous text
    text_widget.insert(tk.END, weird_prompt)  # Insert new text


# Create the main tkinter window
root = tk.Tk()
root.title("Surreal Interpretation Generator")

# Create a Text widget to display the interpretation
text_widget = tk.Text(root, wrap=tk.WORD, width=60, height=10)
text_widget.pack(pady=10)

# Create the 'Generate Weird Interpretation' button
generate_button = tk.Button(root, text="Generate Weird Interpretation", command=generate_weird_interpretation)
generate_button.pack()

# Generate an initial weird interpretation
generate_weird_interpretation()

# Start the tkinter main loop
root.mainloop()
