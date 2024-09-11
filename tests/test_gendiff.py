import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize('file1, file2, expected', [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/expected.txt')
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'tests/fixtures/expected.txt')
    ]
    )

def test_gendiff(file1, file2, expected):
    diff = generate_diff(file1, file2)
    with  open(expected, 'r') as file:
        expected = file.read()
    assert  diff == expected
    



