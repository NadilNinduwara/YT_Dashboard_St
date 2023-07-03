import subprocess

# Set the repository URL and directory
repository_url = 'https://github.com/NadilNinduwara/YT_Dashboard_St'
repository_dir = r'C:\Users\Nadil\Documents\YT_Dashboard_St\New folder'

# Initialize a new Git repository
subprocess.run(['git', 'init'], cwd=repository_dir)

# Add the project files to the repository
subprocess.run(['git', 'add', '.'], cwd=repository_dir)

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=repository_dir)

# Add the remote repository URL
subprocess.run(['git', 'remote', 'add', 'origin', repository_url], cwd=repository_dir)

# Push the changes to the remote repository
subprocess.run(['git', 'push', '-u', 'origin', 'master'], cwd=repository_dir)
