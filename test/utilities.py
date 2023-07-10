import shutil
from pathlib import Path


def get_project_root():
    this_path = Path(__file__).resolve()

    return this_path.parent.parent


def get_data_path() -> Path:

    return get_project_root().joinpath("data")


def get_temp_path() -> Path:
    temp_path = Path(get_project_root().joinpath("temp"))
    temp_path.mkdir(exist_ok=True)

    return temp_path


def clean_temp():
    shutil.rmtree(str(get_temp_path()))
