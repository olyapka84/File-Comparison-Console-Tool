from gendiff.generate_diff import generate_diff


def test_generate_diff_with_json_files_stylish_format():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_path = "tests/test_data/expected_gendiff_stylish.txt"
    with open(expected_path, "r") as file:
        expected = file.read()

    assert expected == generate_diff(file1_path, file2_path, "stylish")


def test_generate_diff_with_json_files_plain_format():
    file1_path = "tests/test_data/file1.json"
    file2_path = "tests/test_data/file2.json"
    expected_path = "tests/test_data/expected_gendiff_plain.txt"
    with open(expected_path, "r") as file:
        expected = file.read()

    assert expected == generate_diff(file1_path, file2_path, "plain")


def test_generate_diff_with_yaml_files_stylish_format():
    file1_path = "tests/test_data/file1.yaml"
    file2_path = "tests/test_data/file2.yaml"
    expected_path = "tests/test_data/expected_gendiff_stylish.txt"
    with open(expected_path, "r") as file:
        expected = file.read()

    assert expected == generate_diff(file1_path, file2_path, "stylish")


def test_generate_diff_with_yaml_plain_format():
    file1_path = "tests/test_data/file1.yaml"
    file2_path = "tests/test_data/file2.yaml"
    expected_path = "tests/test_data/expected_gendiff_plain.txt"
    with open(expected_path, "r") as file:
        expected = file.read()

    assert expected == generate_diff(file1_path, file2_path, "plain")
