# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..fluid.dygraph.base import grad  # noqa: F401
from ..fluid.dygraph.base import no_grad_ as no_grad  # noqa: F401
from ..framework import is_grad_enabled, set_grad_enabled  # noqa: F401
from . import backward_mode  # noqa: F401
from .backward_mode import backward  # noqa: F401
from ..fluid.framework import _in_eager_mode_

if _in_eager_mode_:
    from .py_layer import EagerPyLayer as PyLayer  # noqa: F401
    from .py_layer import EagerPyLayerContext as PyLayerContext  # noqa: F401
else:
    from .py_layer import LegacyPyLayer as PyLayer  # noqa: F401
    from .py_layer import LegacyPyLayerContext as PyLayerContext  # noqa: F401
from ..framework import set_grad_enabled, is_grad_enabled  # noqa: F401
from ..fluid.dygraph.base import no_grad_ as no_grad  # noqa: F401
from .saved_tensors_hooks import saved_tensors_hooks

__all__ = [  # noqa
    'backward',
    'PyLayer',
    'PyLayerContext',
    'saved_tensors_hooks',
]
