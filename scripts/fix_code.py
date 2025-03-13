import subprocess

def auto_fix():
    commands = [
        "black .",
        "isort .",
        "eslint . --fix",
        "gofmt -w .",
        "cargo fmt",
        "php-cs-fixer fix .",
        "clang-format -i $(find . -name '*.c' -o -name '*.cpp')",
        "shfmt -w .",
    ]


    for cmd in commands:
        subprocess.run(cmd, shell=True)

    print("✅ Done!")


if __name__ == "__main__":
    auto_fix()
