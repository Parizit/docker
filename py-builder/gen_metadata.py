#!/usr/bin/env python3
import json
import pathlib
import hashlib
import subprocess
import datetime
import argparse
import re


def parse_args():
    p = argparse.ArgumentParser(description="Заполнить Metadata.Build")
    p.add_argument("name", help="имя модуля/бинарника")
    p.add_argument("--root", help="каталог модуля")
    return p.parse_args()


def get_version(bin_path: str) -> str:
    # Получаем весь вывод -v (может быть многострочный)
    out = subprocess.check_output([bin_path, "-v"], text=True)
    # Ищем первое вхождение цифры.цифры.цифры
    m = re.search(r"\d+\.\d+\.\d+", out)
    if not m:
        return "MAJOR.MINOR.PATCH"
    return m.group(0)


def main():
    args = parse_args()

    root = pathlib.Path(args.root or args.name)

    constraint_path = root / "constraints" / "constraint.json"
    bin_path = root / "bin" / args.name

    # Версия из бинарника
    version = get_version(str(bin_path))

    # Текущая дата
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Читаем JSON
    data = json.loads(constraint_path.read_text(encoding="utf-8"))
    metadata = data.setdefault("Metadata", {})
    build = metadata.setdefault("Build", {})

    # Обновляем поля
    build["Version"] = version
    build["Date"] = now

    # SHA256 по бинарнику
    h = hashlib.sha256()
    with open(bin_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    build["SHA256Bin"] = h.hexdigest()

    # Пишем обратно
    constraint_path.write_text(json.dumps(data, ensure_ascii=False, indent=4),
                               encoding="utf-8")


if __name__ == "__main__":
    main()
