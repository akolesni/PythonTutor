import utilities
from pydantic import BaseModel
from redbird.repos import CSVFileRepo, MemoryRepo


class BaseAppModel(BaseModel):
    name: str
    age: int
    height: int


def test_memory_repo():
    m_repo = MemoryRepo(model=BaseAppModel)
    m_repo.add({"name": "Daniel", "age": 31, "height": 181})
    m_repo.add({"name": "Alex", "age": 41, "height": 171})
    m_repo.add({"name": "Florian", "age": 41, "height": 181})

    result = m_repo.filter_by(height=181)
    assert 2 == result.count()
    assert 41 == m_repo.filter_by(name="Florian").first().age
    m_repo.filter_by(name="Florian").update(age=29)
    assert 29 == m_repo.filter_by(name="Florian").first().age


def test_csv_repo():
    c_repo = CSVFileRepo(filename=utilities.get_temp_path().joinpath("test.csv"), fieldnames=["name", "age", "height"])
    c_repo.add({"name": "Daniel", "age": "31", "height": "181"})
    c_repo.add({"name": "Alex", "age": "41", "height": "171"})
    c_repo.add({"name": "Florian", "age": "41", "height": "181"})

    result = c_repo.filter_by(height="181")
    assert 2 == result.count()
    assert "41" == c_repo.filter_by(name="Florian").first()["age"]
    c_repo.filter_by(name="Florian").update(age=29)
    assert "29" == c_repo.filter_by(name="Florian").first()["age"]


def test_csv_repo_base():
    cb_repo = CSVFileRepo(filename=utilities.get_temp_path().joinpath("test_b.csv"), model=BaseAppModel)
    cb_repo.add({"name": "Daniel", "age": 31, "height": 181})
    cb_repo.add({"name": "Alex", "age": 41, "height": 171})
    cb_repo.add({"name": "Florian", "age": 41, "height": 181})

    result = cb_repo.filter_by(height=181)
    assert 2 == result.count()
    assert 41 == cb_repo.filter_by(name="Florian").first().age
    cb_repo.filter_by(name="Florian").update(age=29)
    assert 29 == cb_repo.filter_by(name="Florian").first().age


def setup_function(function):
    utilities.clean_temp()


def teardown_function(function):
    utilities.clean_temp()
