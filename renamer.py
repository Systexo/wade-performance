import os
import time

# Define the directory containing the .jpeg files
directory = "static/assets/img/portfolio/highlight"

# Get a list of all .jpeg files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.jpeg')]

# Create a list of tuples containing file paths and their last modified time
files_with_time = [(f, os.path.getmtime(os.path.join(directory, f))) for f in files]

# Sort the files by their last modified time
files_with_time.sort(key=lambda x: x[1])

# Rename files in chronological order
for i, (file, _) in enumerate(files_with_time, start=1):
    # Define the new file name, e.g., 1.jpeg, 2.jpeg, etc.
    new_file_name = f"{i}.jpeg"
    
    # Get the full paths for the old and new file names
    old_file_path = os.path.join(directory, file)
    new_file_path = os.path.join(directory, new_file_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)

print(f"Renamed {len(files)} files in {directory}.")
