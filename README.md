# PDF Watermarker

This is a simple Python-based watermarking tool that processes one or more PDF files and applies a watermark from another PDF file.

The project was created as a learning exercise while following the Python course from the [Zero To Mastery Academy](https://zerotomastery.io/) (or github - [@zero-to-mastery](https://github.com/zero-to-mastery). It is designed to be both runnable as a standalone CLI tool and importable as a function module.

## Features

- Accepts multiple PDF files at once
- Supports watermarking using any valid single-page PDF
- Offers optional in-place editing or creates watermarked copies
- Includes basic error handling for missing or unreadable files
- Lightweight and dependency-minimal (uses `pypdf`)

## Usage

You can run it from the command line or import the watermarking function into your own scripts. This makes it suitable for both casual use and integration into larger projects.

## Requirements

- Python 3.7+
- `pypdf` library (install via `pip install pypdf`)

## Notes

This project focuses on simplicity and readability rather than performance or advanced PDF manipulation. It assumes that the watermark file contains a single page, which will be applied to all pages of each target PDF.
