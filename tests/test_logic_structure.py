import pytest
from certnode_processor import analyze_logic

def test_valid_argument_structure():
    sample_text = "All humans are mortal. Socrates is a human. Therefore, Socrates is mortal."
    result = analyze_logic(sample_text)
    assert isinstance(result, dict)
    assert "structure_score" in result
    assert 0 <= result["structure_score"] <= 1
