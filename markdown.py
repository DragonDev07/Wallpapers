import os

def has_image_files(directory):
    for _, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                return True
    return False

def create_readme(directory):
    readme_content = "# Directory Structure\n\n"

    # Get top-level directories
    top_level_dirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    for top_level_dir in top_level_dirs:
        top_level_path = os.path.join(directory, top_level_dir)

        # Ignore hidden directories and directories without image files
        if top_level_dir.startswith('.') or not has_image_files(top_level_path):
            continue

        # Add heading for top-level directories
        readme_content += f"## {top_level_dir}\n\n"

        # Walk through the directory structure
        for root, dirs, files in os.walk(top_level_path):
            relative_path = os.path.relpath(root, directory)

            # Ignore hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            # If we are in a subdirectory, add it as a dropdown
            if relative_path != top_level_dir:
                readme_content += f"<details><summary>{os.path.basename(relative_path)}</summary>\n\n"

            for file in files:
                file_path = os.path.join(root, file)
                file_name, _ = os.path.splitext(file)

                # Extract tags from filename and enclose them in inline code blocks
                tags = [f"`{tag.strip('`')}`" for tag in file_name.split("-")] if "-" in file_name else [f"`{file_name.strip('`')}`"]

                # Add tags above image
                readme_content += f"**Tags:** {' '.join(tags)}\n\n"
                readme_content += f"![{file_name}]({file_path})\n\n"

            # Close the details tag if we are in a subdirectory
            if relative_path != top_level_dir:
                readme_content += "</details>\n\n"

        # Close the top-level directory dropdown
        readme_content += "</details>\n\n"

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    create_readme(directory_path)
    print("README.md created successfully.")
