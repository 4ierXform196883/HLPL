import argparse
import json
import os

# STORAGE_PATH = "storage.data"
STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage.data")


def read_storage():
    if not os.path.exists(STORAGE_PATH):
        return {}
    with open(STORAGE_PATH, encoding="utf-8") as f:
        content = f.read()
    return json.loads(content) if content else {}


def write_storage(data):
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def put(key, value):
    data = read_storage()
    data.setdefault(key, []).append(value)
    write_storage(data)


def get(key):
    return read_storage().get(key, [])


def main():
    parser = argparse.ArgumentParser(description="Key-value хранилище")
    parser.add_argument("--key", required=True, help="имя ключа")
    parser.add_argument("--val", help="добавляемое значение")
    args = parser.parse_args()

    if args.val is not None:
        put(args.key, args.val)
    else:
        values = get(args.key)
        print(", ".join(values) if values else None)


if __name__ == "__main__":
    main()
