### What is this?
This project is a small python script that takes whatever is in your clipboard and translates it for you, one line at a time.

The reason for this project is that I use google translate in my browser to translate chat logs when I play video games online, but I would like to solve the problem programatically instead. However the Google Translate REST API is quite expensive so I'm using pytesseract to convert image to text, and then translator library to translate.

### How Do I Use it?
- [How to](./src/howTo.md)

### What's next?
If I keep working on this project here are some examples of what I would like to try moving forward:
- Make it into a docker container with dependencies bundled together and that executes main.py whenever some key-combo is pressed
- Try different translations alternatives, for example OLLAMA, Azure OpenAI, DeepL.
- Programatically determine source language (tried using langdetect but it was quite unreliable.)
- Expose the functionality behind something like GRPC/REST and continue in a language I am better at, like C#.
- Unit tests.
- Resolve TODO comments.