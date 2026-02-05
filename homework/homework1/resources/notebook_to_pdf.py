"""Convert the Homework 1 notebook into a PDF copy.

Usage:
    python notebook_to_pdf.py
    python notebook_to_pdf.py --notebook ../code/setup.ipynb --output-dir .
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert the Homework 1 notebook to a PDF file."
    )
    parser.add_argument(
        "--notebook",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "code" / "setup.ipynb",
        help="Path to the source notebook (default: homework1/code/setup.ipynb).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Directory where the PDF is written (default: homework1/resources).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = convert_notebook_to_pdf(args.notebook, args.output_dir)
    print(f"PDF created at: {pdf_path}")


if __name__ == "__main__":
    main()
