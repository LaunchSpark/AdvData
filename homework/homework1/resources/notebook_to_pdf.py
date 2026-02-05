from __future__ import annotations

import subprocess
from pathlib import Path

# -----------------------------
# Hard-coded paths
# -----------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

NOTEBOOK_PATH = PROJECT_ROOT / "code" / "setup.ipynb"
OUTPUT_DIR = SCRIPT_DIR


def convert_notebook_to_pdf(notebook: Path, output_dir: Path) -> Path:
    """Convert a Jupyter notebook file to PDF via nbconvert and return output path."""
    notebook = notebook.resolve()
    output_dir = output_dir.resolve()

    if not notebook.exists():
        raise FileNotFoundError(f"Notebook not found: {notebook}")

    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "jupyter",
        "nbconvert",
        "--to",
        "pdf",
        str(notebook),
        "--output-dir",
        str(output_dir),
    ]
    subprocess.run(cmd, check=True)

    return output_dir / f"{notebook.stem}.pdf"


def main() -> None:
    pdf_path = convert_notebook_to_pdf(NOTEBOOK_PATH, OUTPUT_DIR)
    print(f"PDF created at: {pdf_path}")


if __name__ == "__main__":
    main()
