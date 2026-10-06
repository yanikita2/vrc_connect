"""Validate the runtime manifest using the Python standard library."""
import json
from pathlib import Path

SETTING_IDS = {f"c{i:02}" for i in range(1, 19)}


def validate(raw):
    assert len(raw.encode("utf-8")) <= 32768, "manifest too large"
    data = json.loads(raw)
    assert set(data) == {"schema", "revision", "minimumBuild", "channel", "limits"}
    assert type(data["schema"]) is int and data["schema"] == 1
    assert type(data["revision"]) is int and data["revision"] >= 1
    assert type(data["minimumBuild"]) is int and data["minimumBuild"] == 1
    assert data["channel"] in ("demo", "beta")
    assert set(data["limits"]) == SETTING_IDS, "missing or unknown setting"
    for key, value in data["limits"].items():
        assert type(value) is int and 1 <= value <= 2147483647, key
    return data


if __name__ == "__main__":
    path = Path(__file__).parent / "config/runtime.json"
    data = validate(path.read_text(encoding="utf-8"))
    print(f"PASS: revision {data['revision']}, {len(data['limits'])} settings")
