import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))

from mlkem_service import get_mlkem


def main():
    for level in ("512", "768", "1024"):
        engine = get_mlkem(level)
        result = engine.selftest(20)
        assert result["success"], result
        print(f"{result['level']}: {result['passed']}/{result['iterations']} passed; average(ns)={result['average_ns']}")


if __name__ == "__main__":
    main()
