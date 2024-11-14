import logging
import random
from collections.abc import Iterator

import grpc

from common import configure_logging

from pb import (
    hello_service_pb2_grpc,
    hello_service_pb2,
    hello_pb2,
)


log = logging.getLogger(__name__)


def create_many_greetings(n: int) -> Iterator[hello_service_pb2.HelloRequest]:
    log.info("creating %d greetings", n)
    for idx in range(1, n + 1):
        kind = random.choice(hello_pb2.Hello.Kind.values())
        hello = hello_pb2.Hello(
            text=f"hello-{idx:02d}-of-kind-{kind}",
            kind=kind,
        )
        log.info("Send hello %r", hello.text)
        yield hello_service_pb2.HelloRequest(
            hello=hello,
        )


def send_many_greetings(stub: hello_service_pb2_grpc.HelloServiceStub) -> None:
    greetings_count = random.randint(1, 6)
    greetings_requests = create_many_greetings(greetings_count)
    response: hello_service_pb2.MultiHelloResponse = (
        # stream request
        stub.multiHello(greetings_requests)
    )
    log.info(
        "Got response with title %r. Received %d greetings, here they are: %s",
        response.title,
        len(response.greetings),
        response.greetings,
    )


def run() -> None:
    log.info("Start")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_service_pb2_grpc.HelloServiceStub(channel)
        send_many_greetings(stub)

    log.info("Finish")


def main():
    configure_logging()
    try:
        run()
    except KeyboardInterrupt:
        log.warning("Received keyboard interrupt, shutting down")


if __name__ == "__main__":
    main()
