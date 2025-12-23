import subprocess
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "media" / "logs" / "changes"

LOG_DIR.mkdir(parents=True, exist_ok=True)

def get_git_commit_hash():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return "no-git"

def create_change_log(message: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    commit_hash = get_git_commit_hash()

    log_file = LOG_DIR / f"{timestamp}_{commit_hash}.log"

    content = f"""
Time: {timestamp}
Commit: {commit_hash}

Description:
{message}
""".strip()

    log_file.write_text(content, encoding="utf-8")

    print(f"📝 Change log created: {log_file.name}")

if __name__ == "__main__":
    # пример — редактируешь под себя
    create_change_log(
        "Major refactor of core services and URL routing"
    )
