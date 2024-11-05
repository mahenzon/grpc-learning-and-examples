import logging
from pathlib import Path

from common import configure_logging

from pb import user_pb2

log = logging.getLogger(__name__)

BASE_PATH = Path(__file__).resolve().parent

USER_FILEPATH = BASE_PATH / "USER_FILE"


def write() -> None:
    user = user_pb2.User()
    log.info("[creating. before] user is initialized %s", user.IsInitialized())
    log.info("user: %s", user)
    log.info("user.status: %s", user.status)
    log.info("User Status Enum: %s", user.Status)
    log.info("User Status Enum values: %s", user.Status.items())

    # user.id = 42
    # user.username = "john"
    # user.status = user.Status.PROSPECT
    user = user_pb2.User(
        id=42,
        username="john",
        email="john@example.com",
        status=user_pb2.User.Status.PROSPECT,
    )
    log.info("[creating. after] user is initialized %s", user.IsInitialized())
    log.info("user serialized: %s", user.SerializeToString())

    with USER_FILEPATH.open("wb") as f:
        f.write(user.SerializeToString())


def read() -> None:
    user = user_pb2.User()
    log.info("[before reading] user is initialized - %s", user.IsInitialized())
    with USER_FILEPATH.open("rb") as f:
        user.ParseFromString(f.read())

    log.info("[after reading] user is initialized: %s", user.IsInitialized())
    log.info("user: %s", user)
    log.info("user serialized: %s", user.SerializeToString())


def main() -> None:
    configure_logging()
    # write()
    read()


if __name__ == '__main__':
    main()
