import logging

from _pytest.logging import _LiveLoggingNullHandler, _FileHandler, LogCaptureHandler

import utilities


# https://habr.com/ru/companies/wunderfund/articles/683880/


def _test_pytest_default_logger():
    print("")
    # pytest default logger
    default_pytest_logger = logging.getLogger()

    assert default_pytest_logger.name == "root"
    assert default_pytest_logger.level == logging.WARNING
    assert default_pytest_logger.level == 30
    assert not default_pytest_logger.disabled
    assert not default_pytest_logger.parent
    assert default_pytest_logger.propagate
    assert default_pytest_logger.filters == []
    assert default_pytest_logger.root
    assert default_pytest_logger.manager
    # handlers
    assert len(default_pytest_logger.handlers) == 4

    handler_1 = default_pytest_logger.handlers[0]
    assert isinstance(handler_1, _LiveLoggingNullHandler)
    assert handler_1.filters == []
    assert handler_1.formatter
    assert handler_1.level == 0
    assert not handler_1.lock
    assert not handler_1.name

    handler_2 = default_pytest_logger.handlers[1]
    assert isinstance(handler_2, _FileHandler)
    assert handler_2.filters == []
    assert handler_2.formatter
    assert handler_2.level == 0
    assert handler_2.lock
    assert not handler_2.name

    handler_3 = default_pytest_logger.handlers[2]
    assert isinstance(handler_3, LogCaptureHandler)
    assert handler_3.filters == []
    assert handler_3.formatter
    assert handler_3.level == 0
    assert handler_3.lock
    assert not handler_3.name

    handler_4 = default_pytest_logger.handlers[3]
    assert isinstance(handler_4, LogCaptureHandler)
    assert handler_4.filters == []
    assert handler_4.formatter
    assert handler_4.level == 0
    assert handler_4.lock
    assert not handler_4.name


def _test_default_logger():
    default_logger = logging.getLogger()

    assert default_logger.name == "root"
    assert default_logger.level == logging.WARNING
    assert default_logger.level == 30
    assert not default_logger.disabled
    assert not default_logger.parent
    assert default_logger.propagate
    assert default_logger.filters == []
    assert default_logger.root
    assert default_logger.manager
    # handlers
    assert default_logger.handlers == []

    default_logger.debug("A DEBUG Message")
    default_logger.info("An INFO")
    default_logger.warning("A WARNING")
    default_logger.error("An ERROR")
    default_logger.critical("A message of CRITICAL severity")


def _test_basic_config():
    log_file = utilities.get_temp_path().joinpath("py_log.log")
    # BASIC_FORMAT = "%(levelname)s:%(name)s:%(message)s"
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    logging.basicConfig(level=logging.INFO, filename=log_file, filemode="w")

    default_logger = logging.getLogger()

    assert default_logger.name == "root"
    assert default_logger.level == logging.INFO
    assert not default_logger.disabled
    assert not default_logger.parent
    assert default_logger.propagate
    assert default_logger.filters == []
    assert default_logger.root
    assert default_logger.manager
    # handlers
    assert len(default_logger.handlers) == 1
    handler = default_logger.handlers[0]
    assert isinstance(handler, logging.FileHandler)

    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")


if __name__ == "__main__":
    # _test_default_logger()
    _test_basic_config()
