import argparse
from utils import extract_text_from_clipboard, preprocess_text, translate_text

def main():
    parser = argparse.ArgumentParser(description='Extract and translate text from clipboard image.')
    parser.add_argument('--source', default='rus', help='Source language code (default: "rus" for Russian)')
    parser.add_argument('--target', default='en', help='Target language code (default: "en" for English)')
    args = parser.parse_args()

    source_lang = args.source
    target_lang = args.target

    extracted_text = extract_text_from_clipboard(source_lang)

    preprocessed_text = preprocess_text(extracted_text)

    lines = preprocessed_text.split('\n')
    translated_lines = []

    for line in lines:
        if line.strip():
            try:
                translated_line = translate_text(line, source_lang, target_lang)
                translated_lines.append(translated_line)
            except Exception:
                translated_lines.append('Was not translatable') ##TODO: Translate error message to target_lang

    translated_text = '\n'.join(translated_lines)
    print("Translated Text:", translated_text)

if __name__ == '__main__':
    main()