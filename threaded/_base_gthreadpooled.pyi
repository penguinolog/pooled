import gevent.threadpool
import typing
from . import _base_threaded

class BaseGThreadPooled(_base_threaded.APIPooled):
    @classmethod
    def configure(
        cls,
        max_workers: typing.Optional[int]=...,
        hub: typing.Optional[gevent.hub.Hub]=...
    ) -> None: ...

    @classmethod
    def shutdown(cls) -> None: ...

    @property
    def executor(self) -> gevent.threadpool.ThreadPool: ...
