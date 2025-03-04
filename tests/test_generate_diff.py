from gendiff.gendiff import generate_diff


def run_test(file1, file2, expected_file, format_):
    with open(expected_file, "r") as file:
        expected = file.read()
    assert expected == generate_diff(file1, file2, format_)


def test_generate_diff_with_json_stylish_format():
    run_test(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "tests/test_data/expected_gendiff_stylish.txt",
        "stylish"
    )


def test_generate_diff_with_json_plain_format():
    run_test(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "tests/test_data/expected_gendiff_plain.txt",
        "plain"
    )


def test_generate_diff_with_yaml_stylish_format():
    run_test(
        "tests/test_data/file1.yaml",
        "tests/test_data/file2.yaml",
        "tests/test_data/expected_gendiff_stylish.txt",
        "stylish"
    )


def test_generate_diff_with_yaml_plain_format():
    run_test(
        "tests/test_data/file1.yaml",
        "tests/test_data/file2.yaml",
        "tests/test_data/expected_gendiff_plain.txt",
        "plain"
    )


def test_generate_diff_with_yaml_json_format():
    run_test(
        "tests/test_data/file1.yaml",
        "tests/test_data/file2.yaml",
        "tests/test_data/expected_gendiff_json.txt",
        "json"
    )
