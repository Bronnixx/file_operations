import os

def safe_file_operations():
    """
    Comprehensive error handling for file operations.
    Demonstrates various exception handling techniques.
    """
    
    while True:
        try:
            # Get filename from user
            filename = input("\n📁 Enter the filename you want to read: ").strip()
            
            if not filename:
                print("⚠️  Please enter a valid filename.")
                continue
            
            # Check if file exists
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' does not exist.")
            
            # Check if it's actually a file (not a directory)
            if not os.path.isfile(filename):
                raise IsADirectoryError(f"'{filename}' is a directory, not a file.")
            
            # Check file size (prevent reading huge files accidentally)
            file_size = os.path.getsize(filename)
            if file_size > 10 * 1024 * 1024:  # 10MB limit
                raise ValueError(f"File is too large ({file_size/1024/1024:.1f} MB). Maximum allowed: 10MB.")
            
            # Try to read the file with different encodings
            content = try_multiple_encodings(filename)
            
            # Success! Display file info
            print(f"\n✅ File read successfully!")
            print(f"📊 File size: {file_size} bytes")
            print(f"📝 Number of lines: {len(content.splitlines())}")
            print(f"🔤 Encoding detected: UTF-8")  # Simplified for demo
            
            # Ask user if they want to see content
            show_content = input("\n👀 Do you want to see the file content? (y/n): ").lower()
            if show_content in ['y', 'yes']:
                print("\n" + "="*50)
                print(content)
                print("="*50)
            
            break
            
        except FileNotFoundError as e:
            print(f"❌ File Error: {e}")
            retry = input("🔄 Would you like to try another filename? (y/n): ").lower()
            if retry not in ['y', 'yes']:
                print("👋 Exiting program.")
                break
                
        except PermissionError as e:
            print(f"🔒 Permission Denied: {e}")
            print("💡 You don't have read permissions for this file.")
            break
            
        except IsADirectoryError as e:
            print(f"📁 Directory Error: {e}")
            print("💡 Please provide a filename, not a directory path.")
            
        except ValueError as e:
            print(f"📏 Size Error: {e}")
            print("💡 Please choose a smaller file.")
            break
            
        except UnicodeDecodeError as e:
            print(f"🔤 Encoding Error: Cannot read file with standard UTF-8 encoding.")
            print("💡 The file might be binary or use a different encoding.")
            break
            
        except Exception as e:
            print(f"⚡ Unexpected Error: {e}")
            print("💡 Please check the filename and try again.")
            break

def try_multiple_encodings(filename):
    """
    Try reading file with different encodings to handle various file types.
    """
    encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    
    # If all encodings fail, try binary read
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            # For binary files, show a preview
            if len(content) > 100:  # Limit preview for large files
                return f"[Binary file - first 100 bytes shown]\n{content[:100].hex()}"
            else:
                return f"[Binary file]\n{content.hex()}"
    except Exception as e:
        raise Exception(f"Cannot read file with any encoding: {e}")

def create_sample_files():
    """
    Create sample files for testing error handling.
    """
    samples = {
        "normal.txt": "This is a normal text file.\nIt has multiple lines.\nEnd of file.",
        "empty.txt": "",
        "large_file.txt": "This file would be large in real scenario.\n" * 1000
    }
    
    for filename, content in samples.items():
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"📝 Created sample file: {filename}")
        except Exception as e:
            print(f"❌ Error creating {filename}: {e}")

# Main error handling lab function
def main_error_lab():
    print("🔒 FILE ERROR HANDLING LAB")
    print("=" * 40)
    
    # Create sample files for testing
    create_sample_files()
    
    print("\n🧪 Now testing error handling...")
    print("💡 Try entering: 'normal.txt', 'nonexistent.txt', or a directory name.")
    
    # Run the error handling demonstration
    safe_file_operations()

# Run both challenges
if __name__ == "__main__":
    print("🎯 PYTHON FILE HANDLING MASTERY")
    print("=" * 50)
    
    # Run File Read & Write Challenge
    print("\n1. 📄 FILE READ & WRITE CHALLENGE")
    print("-" * 35)
    main_challenge()
    
    # Run Error Handling Lab
    print("\n2. 🔒 ERROR HANDLING LAB")
    print("-" * 25)
    main_error_lab()
