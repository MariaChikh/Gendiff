import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize('file1, file2, formatter, expected', [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish', 'tests/fixtures/expected.txt'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'stylish', 'tests/fixtures/expected.txt'),
    ('tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json', 'stylish', 'tests/fixtures/expected_tree.txt'),
    ('tests/fixtures/file1_tree.yaml', 'tests/fixtures/file2_tree.yaml', 'stylish', 'tests/fixtures/expected_tree.txt'),
    ('tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json', 'plain', 'tests/fixtures/expected_plain.txt'),
    ('tests/fixtures/file1_tree.yaml', 'tests/fixtures/file2_tree.yaml', 'plain', 'tests/fixtures/expected_plain.txt')
    ]
)

def test_gendiff(file1, file2, formatter, expected):
    diff = generate_diff(file1, file2, formatter)
    with  open(expected, 'r') as file:
        expected = file.read()
    assert  diff == expected

    



