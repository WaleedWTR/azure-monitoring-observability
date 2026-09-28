from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from slo_report import calculate, load  # noqa: E402

def test_dataset_size():
    assert len(load()) == 10

def test_availability():
    result = calculate(load())
    assert result["availability_pct"] == 90.0

def test_error_rate_is_positive_and_bounded():
    value = calculate(load())["error_rate_pct"]
    assert 0 < value < 100

def test_request_volume():
    assert calculate(load())["total_requests"] == 10340
