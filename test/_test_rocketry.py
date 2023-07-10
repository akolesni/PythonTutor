import time
from datetime import datetime

from rocketry import Rocketry
from rocketry.conditions.api import after_success
from rocketry.conds import minutely

app = Rocketry()


@app.task(minutely)
def do_things1():
    print("s1 -------")
    print(f"{datetime.now()}")
    time.sleep(5)
    print(f"{datetime.now()}")
    print("e1 -------")


# @app.task(minutely)
@app.task(after_success(do_things1))
def do_things2():
    print("s2 -------")
    print(f"{datetime.now()}")
    time.sleep(6)
    print(f"{datetime.now()}")
    print("e2 -------")
    return False


if __name__ == "__main__":
    print(f"+++++++ {datetime.now()}")
    app.run()
    print("-------")
