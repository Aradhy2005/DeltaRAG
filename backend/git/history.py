import subprocess


def get_commit_history(repo_path):
    result = subprocess.run(
        ["git", "-C", str(repo_path), "log", "--format=%H %s"],
        capture_output=True,
        text=True,
        check=True
    )

    commits = []

    for line in result.stdout.strip().splitlines():
        commit_hash, message = line.split(" ", 1)

        commits.append({
            "hash": commit_hash,
            "message": message
        })

    return commits

def get_changed_files(repo_path, old_commit, new_commit):
    result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_path),
            "diff",
            "--name-only",
            old_commit,
            new_commit
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return result.stdout.strip().splitlines()

def get_file_content(repo_path, commit, file_path):
    result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_path),
            "show",
            f"{commit}:{file_path}"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return result.stdout

if __name__ == "__main__":
    repo_path = "../../test_repo"

    commits = get_commit_history(repo_path)

    new_commit = commits[0]["hash"]
    old_commit = commits[1]["hash"]

    changed_files = get_changed_files(
        repo_path,
        old_commit,
        new_commit
    )

    print("Changed files:", changed_files)

    file_path = changed_files[0]

    old_content = get_file_content(
        repo_path,
        old_commit,
        file_path
    )

    new_content = get_file_content(
        repo_path,
        new_commit,
        file_path
    )

    print("\nOLD CONTENT:")
    print(old_content)

    print("\nNEW CONTENT:")
    print(new_content)