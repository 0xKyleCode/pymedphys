from git import Repo


def merge_main_branch():
    # Open the repository
    repo = Repo(".")

    # Get the current branch
    current_branch = repo.active_branch

    # Switch to the main branch
    repo.git.checkout("main")

    # Merge the main branch into the current branch
    repo.git.merge(current_branch.name)

    # Switch back to the current branch
    repo.git.checkout(current_branch)

    print("Main branch merged into the current branch.")


# Call the function to merge the main branch into the current branch
merge_main_branch()
