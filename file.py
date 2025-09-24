def modify_file_content(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes to a new file.
    Modification: Convert text to uppercase and add line numbers.
    """
    try:
        # Read the original file
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
        
        # Modify the content
        modified_lines = []
        for i, line in enumerate(lines, 1):
            # Remove extra whitespace, convert to uppercase, add line number
            cleaned_line = line.strip().upper()
            modified_line = f"{i:03d}: {cleaned_line}\n"
            modified_lines.append(modified_line)
        
        # Write to new file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(modified_lines)
        
        print(f"✅ Success! Modified file saved as: {output_filename}")
        print(f"📊 Original lines: {len(lines)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing files: {e}")
        return False

# Example usage
def main_challenge():
    input_file = "sample.txt"
    output_file = "modified_sample.txt"
    
    # Create a sample file if it doesn't exist
    try:
        with open(input_file, 'w') as f:
            f.write("Hello, this is line one.\n")
            f.write("This is the second line.\n")
            f.write("And here's the third line!\n")
        print(f"📝 Created sample file: {input_file}")
    except:
        pass
    
    # Process the file
    modify_file_content(input_file, output_file)
    
    # Display the results
    print("\n📖 Original file content:")
    with open(input_file, 'r') as f:
        print(f.read())
    
    print("📖 Modified file content:")
    with open(output_file, 'r') as f:
        print(f.read())

# Run the challenge
if __name__ == "__main__":
    main_challenge()
