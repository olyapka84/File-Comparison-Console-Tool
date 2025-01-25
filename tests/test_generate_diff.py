from gendiff.generate_diff import generate_diff


def test_generate_diff_with_json_files():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_path = "tests/test_data/expected_gendiff.txt"
    with open(expected_path, "r") as file:
        expected = file.read()

    assert expected == generate_diff(file1_path, file2_path)


def test_gendiff_py():
    pass