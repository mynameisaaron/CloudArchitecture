import os
import argparse
from io import StringIO

def process_directory(directory_path, file_types):
    file_structure = []
    combined_code = StringIO()

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory_path)
            file_extension = file.split('.')[-1].lower()

            if file_extension in file_types:
                file_structure.append(f"{relative_path}: {file_extension.upper()} file")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        combined_code.write(f"\n\n--- {relative_path} ---\n\n")
                        combined_code.write(f.read())
                except UnicodeDecodeError:
                    print(f"Warning: Unable to read {file_path} with UTF-8 encoding. Skipping.")

    return file_structure, combined_code.getvalue()

def main():
    parser = argparse.ArgumentParser(description="Process website files and combine them.")
    parser.add_argument("directory", help="Path to the website directory")
    parser.add_argument("--output", default="combined_website_code.txt", help="Output file name")
    parser.add_argument("--html-css", action="store_true", help="Include only HTML and CSS files")
    parser.add_argument("--html-js", action="store_true", help="Include only HTML and JavaScript files")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return

    file_types = ['html']
    if args.html_css:
        file_types.append('css')
    elif args.html_js:
        file_types.append('js')
    else:
        file_types.extend(['css', 'js'])

    file_structure, combined_code = process_directory(args.directory, file_types)

    final_content = "File Structure:\n"
    final_content += "\n".join(file_structure)
    final_content += "\n\nCombined Code:\n"
    final_content += combined_code

    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Website files processed and combined successfully! Output saved to {args.output}")
    except IOError as e:
        print(f"Error writing to {args.output}: {e}")

if __name__ == "__main__":
    main()