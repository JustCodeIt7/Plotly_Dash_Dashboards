def extract_python_code(markdown_file, output_file):
    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content into lines for processing
    lines = content.split('\n')

    extracted_content = []
    in_code_block = False
    current_code = []

    for line in lines:
        # Check for code block markers
        if line.strip().startswith('```python'):
            in_code_block = True
            continue
        elif line.strip() == '```' and in_code_block:
            if current_code:
                extracted_content.append('\n'.join(current_code))
                current_code = []
            in_code_block = False
            continue

        # Process headers and code
        if line.startswith('#') and not in_code_block:
            # Convert markdown headers to Python comments
            # Add a blank line before comments for readability
            if current_code:
                extracted_content.append('\n'.join(current_code))
                current_code = []
            extracted_content.append(f"\n# {line.lstrip('#').strip()}")
        elif in_code_block and 'hide_code=true' not in line:
            current_code.append(line)

    # Add any remaining code
    if current_code:
        extracted_content.append('\n'.join(current_code))

    # Combine all content
    combined_code = '\n'.join(extracted_content)

    # Add a header comment
    header = f"""# Generated from markdown file: {markdown_file}
# Contains all Python code blocks from the original markdown with preserved headers

"""
    combined_code = header + combined_code

    # Write the extracted code to a new Python file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_code)

    print(f"Python code has been extracted to: {output_file}")

if __name__ == "__main__":
    markdown_file = "./filled-area-plots.md"  # Replace with your markdown file name
    output_file = "extracted_code.py"

    try:
        extract_python_code(markdown_file, output_file)
    except FileNotFoundError:
        print(f"Error: Could not find the file {markdown_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
