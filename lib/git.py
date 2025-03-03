import subprocess
import os

def clone_repository(repo_url, destination_folder):
    """
    :param repo_url: URL of the Git repository to clone.
    :param destination_folder: Local path where the repository will be cloned
    """
    
    try:
        subprocess.run(["git", "clone", repo_url, destination_folder], check=True)
        print(f"Successfully downloaded {repo_url} to {destination_folder}")
	except subprocess.CalledProcessError as e:
        print(f"Failed to download {repo_url}: {e}")

def main():
    repositories = [
        ("https://github.com/CozyOS/cozyos-system.git", "~/.local/cache/cozyos/base"),
        ("https://github.com/CozyOS/cozyos-utils.git", "~/.local/cache/cozyos/utils"),
        ("https://github.com/CozyOS/cozyos-pentaruDE.git", "~/.local/cache/cozyos/wm"),
        ("https://github.com/CozyOS/cozyos-extras.git", "~/.local/cache/cozyos/extras"),
    ]
    
    for repo_url, dest_folder in repositories:
        clone_repository(repo_url, dest_folder)
        
if __name__ == "__main__":
    main()
