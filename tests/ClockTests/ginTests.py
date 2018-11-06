# Copyright 2018 The Dopamine Clock Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for establishing correct dependency injection with gin."""

import tensorflow as tf
from tensorflow.test import *
import os
import shutil
import gin

class GinTests(TestCase):
    def setUp(self):
        pass
    def testSampelsGin(self):
        ginFiles = ['tests/ClockTests/ginTest.gin']
        gin.parse_config_files_and_bindings(ginFiles, [],skip_unknown=False)
        myOpt = tf.train.RMSPropOptimizer(learning_rate=0.002)
        print myOpt._learning_rate
        print myOpt._decay
        pass

if __name__ == '__main__':
  main()
