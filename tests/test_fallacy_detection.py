import pytest
from fallacy_detector import detect_fallacies

def test_detect_known_fallacy():
    fallacious = "You can't trust his opinion on politics because he never graduated college."
    result = detect_fallacies(fallacious)
    assert "ad_hominem" in result
