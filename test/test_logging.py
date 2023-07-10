import logging


def test_default_logger():
    default_logger = logging.getLogger()
    assert default_logger.name == "root"
    assert default_logger.level == logging.WARNING
    print(f"handlers: {default_logger.handlers}")
    print(default_logger)
