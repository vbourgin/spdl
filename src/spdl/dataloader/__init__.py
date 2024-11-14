# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""Utilities to run I/O operations efficiently."""

# pyre-unsafe

import warnings
from typing import Any

import spdl.pipeline

# For backward compatibility
_mods = [spdl.pipeline]

__all__ = sorted(item for mod in _mods for item in mod.__all__)


def __dir__():
    return __all__


def __getattr__(name: str) -> Any:
    for mod in _mods:
        if name in mod.__all__:
            if mod is spdl.pipeline:
                warnings.warn(
                    f"{name} has been moved to {mod.__name__}. "
                    "Please update the import statement to "
                    f"`from {mod.__name__} import {name}`.",
                    stacklevel=2,
                )

            return getattr(mod, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
