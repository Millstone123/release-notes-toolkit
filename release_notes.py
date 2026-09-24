from typing import Iterable, Mapping


SECTION_TAGS = (("Features", "feature"), ("Fixes", "fix"), ("Other", "other"))


def render_notes(entries: Iterable[Mapping[str, str]]) -> str:
    """Render normalized change records into stable Markdown sections."""
    groups = {"feature": [], "fix": [], "other": []}
    seen = set()
    for entry in entries:
        summary = entry.get("summary", "").strip()
        if not summary or summary in seen:
            continue
        seen.add(summary)
        bucket = entry.get("tag", "other")
        if bucket not in groups:
            bucket = "other"
        groups.setdefault(bucket, []).append(summary)
    return "".join(
        f"### {title}\n" + "".join(f"- {item}\n" for item in groups[bucket])
        for title, bucket in SECTION_TAGS
        if groups[bucket]
    )
