import os
import os.path
from pathlib import Path

import utilities

FOLDER = "templates"


def test_exists():
    existing_folder_path = utilities.get_data_path()

    assert os.path.exists(str(existing_folder_path))


def test_listdir_number_of_files():
    existing_folder_path = str(utilities.get_data_path().joinpath())

    assert 1 == len(os.listdir(existing_folder_path))


def test_listdir_check_file_extensions():
    existing_folder_path = str(utilities.get_data_path().joinpath(FOLDER))

    assert any(".html" in file for file in os.listdir(existing_folder_path))


def test_os():
    assert "nt" == os.name
    print(Path(os.environ["HOME"]))
