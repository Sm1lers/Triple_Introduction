import shutil
import datetime
from pathlib import Path

# пути
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"
BACKUP_DIR = BASE_DIR / "media" / "backups"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

def backup_database():
    if not DB_PATH.exists():
        print("❌ Database not found")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"db_backup_{timestamp}"

    temp_copy = BACKUP_DIR / f"{backup_name}.sqlite3"
    archive_path = BACKUP_DIR / f"{backup_name}.zip"

    # копируем БД
    shutil.copy2(DB_PATH, temp_copy)

    # архивируем
    shutil.make_archive(
        base_name=str(archive_path).replace(".zip", ""),
        format="zip",
        root_dir=BACKUP_DIR,
        base_dir=temp_copy.name,
    )

    # удаляем временную копию
    temp_copy.unlink()

    print(f"✅ Database backup created: {archive_path.name}")

if __name__ == "__main__":
    backup_database()
