import asyncio
import typing

def get_loop(
    self: typing.Any, *args: typing.Tuple, **kwargs: typing.Dict
) -> typing.Optional[asyncio.AbstractEventLoop]: ...

def await_if_required(target: typing.Callable) -> typing.Callable[..., typing.Any]: ...
