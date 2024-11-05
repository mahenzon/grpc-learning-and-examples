import logging
from pathlib import Path

from common import configure_logging

from pb import user_pb2, users_response_pb2

log = logging.getLogger(__name__)

BASE_PATH = Path(__file__).resolve().parent

USER_FILEPATH = BASE_PATH / "USER_FILE"


def write() -> None:
    user_john = user_pb2.User(
        id=42,
        username="john",
        email="john@example.com",
        # status=user_pb2.User.Status.PROSPECT,
    )
    user_sam = user_pb2.User(
        id=33,
        username="sam",
        email="sam@example.com",
        status=user_pb2.User.Status.ACTIVE,
    )
    user_nick = user_pb2.User(
        id=27,
        username="nick",
        status=user_pb2.User.Status.BLOCKED,
    )
    users = [
        user_john,
        user_sam,
        user_nick,
    ]
    response_meta = users_response_pb2.ResponseMeta(
        page=1,
        total=len(users),
        pageSize=max(10, len(users)),
    )
    users_response = users_response_pb2.UsersResponse(
        meta=response_meta,
        users=users,
    )

    log.info("users response:\n%s", users_response)

    # with USER_FILEPATH.open("wb") as f:
    #     f.write(user.SerializeToString())


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
    write()
    # read()


if __name__ == '__main__':
    main()
