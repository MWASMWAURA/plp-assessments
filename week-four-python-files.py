# File Read & Write with Error Handling

try:
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    # Try to open the file for reading
    with open(filename, "r") as infile:
        content = infile.read()

    # Process: Convert to uppercase
    modified_content = content.upper()

    # Write modified content to a new file
    output_file = "output.txt"
    with open(output_file, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Success! Modified content written to '{output_file}'.")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
