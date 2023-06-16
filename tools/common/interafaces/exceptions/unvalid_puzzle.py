from collections.abc import Sequence

import sys

if sys.version_info.major > 3 or sys.version_info.minor >= 11:
    from builtins import ExceptionGroup
else:
    from exceptiongroup import ExceptionGroup


from tools.common.interafaces.exceptions.general import GuiderException


class UnvalidPuzzleCauseException(GuiderException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnvalidPuzzleExceptionGroup(GuiderException, ExceptionGroup):
    def __new__(cls, exceptions: Sequence[UnvalidPuzzleCauseException]):
        return super().__new__(cls, "Unvalid Puzzle Configuration", exceptions)
