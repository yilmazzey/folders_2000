import os
import subprocess

def run_command(command, description=None):
    """Run a shell command and print its output."""
    if description:
        print(f"\n{description}:")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    
    if result.stderr and result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    
    return True

# Step 1: Initialize a git repository
run_command("git init", "Initializing git repository")

# Step 2: Create a .gitignore file
gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# PDF files (optional - remove this if you want to include PDFs in the repo)
*.pdf

# Directories with data (optional - remove if you want to include these)
eacl_1500+/
emnlp_500/
combined_2000/
divided_data_4folders/

# OS specific files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
"""

with open(".gitignore", "w") as f:
    f.write(gitignore_content)

run_command("git add .gitignore", "Adding .gitignore file")

# Step 3: Create a README.md file
readme_content = """# PDF Dataset Divider

A tool to combine and divide PDF datasets into specified folder structures.

## Features

- Combines PDFs from multiple source folders
- Detects and handles duplicate files
- Creates a balanced distribution of files across folders
- Includes verification to ensure correct file counts

## Usage

Run the Jupyter notebook `dividedataset.ipynb` which contains the following functionality:

1. Combining PDFs from source folders into a single collection
2. Dividing the combined collection into 4 equal folders with 500 PDFs each
3. Providing helper functions to verify file counts
"""

with open("README.md", "w") as f:
    f.write(readme_content)

run_command("git add README.md", "Adding README.md file")

# Step 4: Add the notebook
run_command("git add dividedataset.ipynb", "Adding notebook")

# Step 5: Commit changes
run_command('git commit -m "Initial commit: PDF dataset divider tool"', "Making initial commit")

# Step 6: Instructions for GitHub
print("\n\nTo push this to GitHub:")
print("1. Create a new repository on GitHub (don't initialize with README, .gitignore, or license)")
print("2. Run the following commands to connect and push to your GitHub repository:")
print("\n   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git")
print("   git branch -M main")
print("   git push -u origin main")
print("\nReplace YOUR_USERNAME and YOUR_REPO_NAME with your GitHub username and repository name.") 