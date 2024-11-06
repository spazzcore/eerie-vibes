Eerie Vibes

A Lesson in Prompt Engineering

This project started as a simple class assignment, and, for me, I guess it still kind of is. The instruction was straightforward: use a Large Language Model (LLM) of my choice to create a program that generates images. I had a specific plan in mind: I wanted 10 custom draw_image functions, each with a unique "eerie" vibe. These functions would be mapped to user input, and both the user input and generated images would display in a GUI wrapped in Pygame. My challenge to myself was not to write any code directly—instead, I’d see how far I could get by relying entirely on an LLM (GPT-4, by OpenAI) for all code generation. I wanted to push the LLM to design the eerie theme while handling all the details in Python, PIL, and Pygame.

What you see here is the final product of about two hours of troubleshooting and prompt engineering. I used OpenAI’s ChatGPT-4 model, specifically the advanced reasoning option in the GPT-4-01 preview, to guide the code development. I only debugged within one thread, sticking with the initial prompt and modifying instructions as needed.
How It Works

Design & Theme: The LLM selected the colors, shapes, and objects to fit what it thought of as an eerie vibe.

Code Structure: The project has a few main parts: GUI Setup, A Pygame-based interface with a text input box and a submission button, which lets the user type prompts and trigger image generation. Image Functions, 10 custom draw_image functions, each creating a unique spooky image (like a “sinister cat” or “eerie sun”) using PIL. These functions are mapped to words in the user input, generating different images based on specific keywords. Dynamic Background, each time an image is generated, the background is randomly filled with dark, muted shapes for an added eerie effect. Prompt and Display; A random eerie prompt is displayed alongside the generated images and user input, creating an interactive, spooky-themed experience.


Prompt Instructions: My prompt instructions to the LLM were simple but specific: "use Python, PIL, and Pygame to create eerie vibes with 10 distinct image functions mapped to user input.

Challenges: The primary challenges were in GUI functionality and button/interaction design. The LLM generated all of the structural code, including input handling, button design, and prompt display. It took some troubleshooting on my end to get everything running smoothly, but the core logic and eerie vibe came directly from the LLM’s generated code. Also the images were initioaly just squares and circles that it called "cat' or "house" etc. I explained that I wanted these to be more detailed and fit the aesthetic. And the final result we have here, is just that. It took almost no more prompting after the initial run.

Overall, it's fascinating to see how this version came to capturing the vibe I originally said through prompts alone, with no hands-on coding. I was tempted to add a simple pre trained NN model ala SpaCy or huggingface to make more dynamic experience. However with my challenge of no hands on coding that would have certainly added another 2 hours to the project I am sure. I think given enough time and patience you can prompt engineer your way to some crazy projects I bet. Just imagine what the next generation of LLMs will bring.
