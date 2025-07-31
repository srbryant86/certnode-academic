import jsonschema
import json
import pytest

with open("schemas/cert_output_manifest.json") as f:
    schema = json.load(f)

def test_valid_output_matches_schema():
    output = {
        "capsule_hash": "abc123",
        "logic_tier": 16,
        "validation_passed": True,
        "timestamp": "2025-07-31T12:00:00Z"
    }
    jsonschema.validate(output, schema)
