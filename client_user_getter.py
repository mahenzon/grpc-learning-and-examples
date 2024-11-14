import logging
import random
from collections.abc import Iterator
from time import sleep

import grpc

from common import configure_logging

from pb import (
    user_service_pb2_grpc,
    user_service_pb2,
)


log = logging.getLogger(__name__)


def get_user_by_id(stub: user_service_pb2_grpc.UserGetterStub) -> None:
    some_user_id = random.randint(20, 200)
    get_user_by_id_request = user_service_pb2.UserRequestById(
        id=some_user_id,
    )
    response_user_by_id: user_service_pb2.UserDetailsResponse = stub.GetUserById(
        get_user_by_id_request
    )
    log.info(
        "Got user by id request:\n%s, response:\n%s",
        get_user_by_id_request,
        response_user_by_id.user,
    )


def get_user_by_username(stub: user_service_pb2_grpc.UserGetterStub) -> None:
    some_user_id = random.randint(20, 200)
    get_user_by_username_request = user_service_pb2.UserRequestByUsername(
        username=f"user-abc-{some_user_id:03d}",
    )
    response_user_by_username: user_service_pb2.UserDetailsResponse = (
        stub.GetUserByUsername(
            get_user_by_username_request,
        )
    )
    log.info(
        "Got user by username request:\n%s, response:\n%s",
        get_user_by_username_request,
        response_user_by_username.user,
    )


def get_matching_users_by_username(stub: user_service_pb2_grpc.UserGetterStub) -> None:
    some_user_id = random.randint(20, 200)
    get_matching_users_by_username_request = user_service_pb2.UserRequestByUsername(
        username=f"user-abc-{some_user_id:03d}",
    )
    type resp = Iterator[user_service_pb2.UserDetailsResponse]
    response: resp = stub.GetUsersMatchingUsername(
        get_matching_users_by_username_request,
    )
    for details_response in response:
        log.info(
            "Got user by username request:\n%s, user:\n%s",
            get_matching_users_by_username_request.username,
            details_response.user,
        )
        sleep(1)


def run() -> None:
    log.info("Start")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = user_service_pb2_grpc.UserGetterStub(channel)
        get_user_by_id(stub)
        get_user_by_username(stub)
        get_matching_users_by_username(stub)

    log.info("Finish")


def main():
    configure_logging()
    try:
        run()
    except KeyboardInterrupt:
        log.warning("Received keyboard interrupt, shutting down")


if __name__ == "__main__":
    main()
