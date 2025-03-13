import subprocess


def run_linter(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    linters = {
        "Python - Pylint": "pylint --output-format=colorized $(git ls-files '*.py')",
        "Python - Flake8": "flake8 --statistics --count",
        "Python - Black (Check Only)": "black --check --diff .",
        "Python - Isort": "isort --check-only .",
        "JavaScript - ESLint": "eslint . --fix",
        "Go - GolangCI-Lint": "golangci-lint run",
        "Rust - Clippy": "cargo clippy",
        "PHP - PHP CodeSniffer": "phpcs --standard=PSR2",
        "C/C++ - Cppcheck": "cppcheck --enable=all .",
        "Shell - ShellCheck": "shellcheck $(git ls-files '*.sh')",
        "Docker - Hadolint": "hadolint Dockerfile",
    }

    print("=== AIOLint - All-in-One Linter ===\n")
    for name, cmd in linters.items():
        print(f"--- {name} ---")
        print(run_linter(cmd))
        print("\n")


if __name__ == "__main__":
    main()
