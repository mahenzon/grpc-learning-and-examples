import logging
from pathlib import Path

from common import configure_logging
from pb import ping_pb2

log = logging.getLogger(__name__)

BASE_PATH = Path(__file__).resolve().parent

PING_FILEPATH = BASE_PATH / "PING_FILE"


def write() -> None:
    ping = ping_pb2.Ping()
    log.info("[first before] ping is initialized: %s", ping.IsInitialized())
    ping.ok = True
    log.info("[first after] ping is initialized: %s", ping.IsInitialized())
    log.info("ping: %s", ping.SerializeToString())

    with PING_FILEPATH.open("wb") as f:
        f.write(ping.SerializeToString())


def read() -> None:
    ping = ping_pb2.Ping()
    log.info("[reading before] ping is initialized: %s", ping.IsInitialized())
    with PING_FILEPATH.open("rb") as f:
        ping.ParseFromString(f.read())

    log.info("[reading after] ping is initialized: %s", ping.IsInitialized())
    log.info("ping ok: %s", ping.ok)
    log.info("ping: %s", ping.SerializeToString())


def main() -> None:
    configure_logging()
    write()
    read()


if __name__ == '__main__':
    main()
