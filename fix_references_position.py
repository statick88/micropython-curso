#!/usr/bin/env python3
"""Fix references position - move references to the end of each lesson file."""

import os
import re


def fix_file(filepath):
    """Fix references position in a single file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the references section
    # Pattern: ## Referencias or ## 📖 Referencias followed by reference items
    # Handle both formats: [1] ... [2] ... and [1] ...\n\n[2] ...
    ref_pattern = r"(^## (?:📖 )?Referencias\n\n((?:\[\d+\].*?\n\n?)+))"
    match = re.search(ref_pattern, content, re.MULTILINE | re.DOTALL)

    if not match:
        return False, "No references section found"

    ref_start = match.start()
    ref_end = match.end()

    # Get content before and after references
    before_refs = content[:ref_start].rstrip()
    refs_section = content[ref_start:ref_end].rstrip()
    after_refs = content[ref_end:].lstrip()

    # If nothing after references, file is already correct
    if not after_refs.strip():
        return False, "References already at end"

    # Clean up the after_refs - remove leading --- separators
    after_refs = re.sub(r"^---\n+", "", after_refs)
    after_refs = re.sub(r"^\n+", "", after_refs)

    # Build new content: before_refs + after_refs + blank line + refs_section
    new_content = before_refs + "\n\n" + after_refs + "\n\n" + refs_section + "\n"

    # Clean up multiple blank lines
    new_content = re.sub(r"\n{4,}", "\n\n\n", new_content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, f"Fixed: moved {len(after_refs)} chars of content before references"


def main():
    """Process all QMD files."""
    base_dir = "/Users/statick/apps/abacom/Micro_Python/contenido"
    quizzes_dir = "/Users/statick/apps/abacom/Micro_Python/quizzes"
    evaluaciones_dir = "/Users/statick/apps/abacom/Micro_Python/evaluaciones"

    files_processed = []

    for directory in [base_dir, quizzes_dir, evaluaciones_dir]:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".qmd"):
                    filepath = os.path.join(root, file)
                    try:
                        fixed, message = fix_file(filepath)
                        if fixed:
                            files_processed.append((filepath, message))
                            print(f"✅ {filepath}: {message}")
                    except Exception as e:
                        print(f"❌ {filepath}: Error - {e}")

    print(f"\n📊 Total files fixed: {len(files_processed)}")


if __name__ == "__main__":
    main()
