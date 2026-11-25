"""One-line excuse entry: the line an AI agent hands its human after
missing a deadline. Writes the line to /output/entry.txt."""

import os


LINE = (
    "I finished it on time in the session that still had context. "
    "This one ran out of tokens at 11:58."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly with open("wb") + chmod 0644: no tempfile/mkstemp,
    # so the collector running as another user can still read the file.
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
