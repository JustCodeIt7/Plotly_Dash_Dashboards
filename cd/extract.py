import re

def extract_python_code(markdown_file, output_file):
    # Initialize variables
    extracted_lines = []
    inside_code_block = False
    code_block_language = ''
    hide_code = False

    # Regular expressions
    header_pattern = re.compile(r'^(#{1,6})\s+(.*)')
    code_block_start_pattern = re.compile(r'^```(\w+)(.*)')
    code_block_end_pattern = re.compile(r'^```$')

    with open(markdown_file, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.strip()

            if not inside_code_block:
                # Check for header
                header_match = header_pattern.match(stripped_line)
                if header_match:
                    header_text = header_match.group(2).strip()
                    extracted_lines.append(f"# {header_text}\n")
                    continue

                # Check for the start of a code block
                code_block_start_match = code_block_start_pattern.match(stripped_line)
                if code_block_start_match:
                    code_block_language = code_block_start_match.group(1)
                    code_block_params = code_block_start_match.group(2)
                    if code_block_language.lower() == 'python':
                        # Check for hide_code parameter
                        hide_code = 'hide_code=true' in code_block_params
                        inside_code_block = True
                    else:
                        # Not a Python code block
                        inside_code_block = False
                    continue
            else:
                # Inside a code block
                if code_block_end_pattern.match(stripped_line):
                    inside_code_block = False
                    continue

                if code_block_language.lower() == 'python' and not hide_code:
                    extracted_lines.append(line.rstrip() + '\n')

    # Combine all extracted lines
    combined_code = ''.join(extracted_lines).strip()

    # Add a header comment
    header = f"# Generated from markdown file: {markdown_file}\n# Contains all Python code blocks from the original markdown\n\n"
    combined_code = header + combined_code + '\n'

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
