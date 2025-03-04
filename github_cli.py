import subprocess

# Install GitHub CLI if not already installed (uncomment if needed)
# subprocess.run("pip install gh", shell=True)

# Login to GitHub
subprocess.run("gh auth login", shell=True)

# Create a GitHub repository
repo_name = "pdf-dataset-divider"  # Change this to your preferred name
repo_description = "Tool for combining and dividing PDF datasets"
subprocess.run(f'gh repo create {repo_name} --public --description "{repo_description}"', shell=True)

# Push to GitHub
subprocess.run(f"git remote add origin https://github.com/$(gh api user | jq -r .login)/{repo_name}.git", shell=True)
subprocess.run("git branch -M main", shell=True)
subprocess.run("git push -u origin main", shell=True)

print(f"\nRepository created and code pushed to GitHub: https://github.com/$(gh api user | jq -r .login)/{repo_name}") 