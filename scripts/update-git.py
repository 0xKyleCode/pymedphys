from git import Repo


def merge_main_branch():
    # Open the repository
    repo = Repo(".")

    # Merge the main branch into the current branch
    repo.git.merge("main")

    print("Main branch merged into the current branch.")


# Call the function to merge the main branch into the current branch
merge_main_branch()
