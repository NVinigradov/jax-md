# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines utility functions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from jax.tree_util import register_pytree_node
import jax.numpy as np

import numpy as onp


i16 = np.int16
i32 = np.int32
i64 = np.int64

f32 = np.float32
f64 = np.float64


def static_cast(*xs):
  """Function to cast a value to the lowest dtype that can express it."""
  # NOTE(schsam): static_cast is so named because it cannot be jit.
  return (np.array(x, dtype=onp.min_scalar_type(x)) for x in xs)


def register_pytree_namedtuple(cls):
  register_pytree_node(
      cls,
      lambda xs: (tuple(xs), None),
      lambda _, xs: cls(*xs))


def check_kwargs_time_dependence(kwargs):
  # TODO(schsam): We should be more careful about checking that kwargs don't
  # have excess data at the leaves of our computations.
  return
  if ('t' in kwargs and len(kwargs) == 1) or len(kwargs) == 0:
    return

  raise ValueError(
    'Found unexpected kwargs: {}. Expected empty or time only.'.format(kwargs))


def check_kwargs_empty(kwargs):
  # TODO(schsam): We should be more careful about checking that kwargs don't
  # have excess data at the leaves of our computations.
  return 
  if kwargs:
    raise ValueError(
      'Found unexpected kwargs: {}. Expected empty.'.format(kwargs))


def merge_dicts(a, b):
  # TODO(schsam): Replace by {**a, **b} when Python 2 is depricated.
  merged = dict(a)
  merged.update(b)
  return merged
