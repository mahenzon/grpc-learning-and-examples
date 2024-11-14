import logging
import random
from collections.abc import Generator, Iterator
from concurrent.futures import ThreadPoolExecutor

import grpc

from common import configure_logging

from pb import (
    hello_pb2,
    hello_service_pb2_grpc,
    hello_service_pb2,
)

log = logging.getLogger(__name__)


class HelloServiceServicer(hello_service_pb2_grpc.HelloServiceServicer):
    def multiHello(
        self,
        request_iterator: Iterator[hello_service_pb2.HelloRequest],
        context: grpc.ServicerContext,
    ) -> hello_service_pb2.MultiHelloResponse:
        log.info("Got multi request for hello %s", request_iterator)
        greetings = []
        for request in request_iterator:
            log.info("The request for multi Hello %s", request.hello)
            greetings.append(request.hello)
        return hello_service_pb2.MultiHelloResponse(
            title=f"This is response for multi Hello, received {len(greetings)} greetings.",
            greetings=greetings,
        )


def serve() -> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    hello_service_pb2_grpc.add_HelloServiceServicer_to_server(
        HelloServiceServicer(), server
    )
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
