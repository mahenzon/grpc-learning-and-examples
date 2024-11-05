import logging
import random
from concurrent.futures import ThreadPoolExecutor

import grpc

from common import configure_logging

from pb import (
    user_service_pb2_grpc,
    user_pb2,
    user_service_pb2,
)


log = logging.getLogger(__name__)


class UserGetterServicer(user_service_pb2_grpc.UserGetterServicer):
    def GetUserById(
        self,
        request: user_service_pb2.UserRequestById,
        context: grpc.ServicerContext,
    ) -> user_service_pb2.UserDetailsResponse:
        log.info("Requested user by id: %s", request.id)
        username = f"user-{request.id:03d}"
        user = user_pb2.User(
            id=request.id,
            username=username,
            email=f"{username}@example.com",
            status=random.choice(user_pb2.User.Status.values()),
        )
        log.info("Send user in response:\n%s", user)
        return user_service_pb2.UserDetailsResponse(
            user=user,
        )

    def GetUserByUsername(
        self,
        request: user_service_pb2.UserRequestByUsername,
        context: grpc.ServicerContext,
    ) -> user_service_pb2.UserDetailsResponse:
        log.info("Requested user by username: %s", request.username)
        user = user_pb2.User(
            id=random.randint(10, 100),
            username=request.username,
            email=f"{request.username}@example.com",
            status=random.choice(user_pb2.User.Status.values()),
        )
        log.info("Send user in response:\n%s", user)
        return user_service_pb2.UserDetailsResponse(
            user=user,
        )


def serve() -> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserGetterServicer_to_server(UserGetterServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    log.warning("Listening on port :50051")
    server.wait_for_termination()


def main():
    configure_logging()
    try:
        serve()
    except KeyboardInterrupt:
        log.warning("Received keyboard interrupt, shutting down")


if __name__ == "__main__":
    main()
