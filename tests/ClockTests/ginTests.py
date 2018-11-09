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

@gin.configurable
class MyGinClass(object):
    def __init__(self,
                 noInitValue,
                 testValue = 0,
                 myOpt=tf.train.RMSPropOptimizer(
                     learning_rate=0.00025,
                     decay=0.953333,
                     momentum=0.0,
                     epsilon=0.00001,
                     centered=True)):
        self.testValue = testValue
        self.myOpt = myOpt
        self.noInitValue = noInitValue

class GinTests(TestCase):
    @classmethod
    def setUpClass(cls):
        ginFiles = ['tests/ClockTests/ginTest.gin']
        gin.parse_config_files_and_bindings(ginFiles, [],skip_unknown=False)
        pass
    def testSampelsGin(self):
        myOpt = tf.train.RMSPropOptimizer(learning_rate=0.002)
        #tf.train.RMSPropOptimizer is not defined with @gin.configurable, so these values is defined in python codes, instead of in tests/ClockTests/ginTest.gin
        print myOpt._learning_rate
        print myOpt._decay
        pass
    def testMyGinClass(self):
        #because MyGinClass is defined with @gin.configurable, and also defined related values in tests/ClockTests/ginTest.gin,
        #so I could check their values
        myObj = MyGinClass(noInitValue=33)

        #This should fail
        #myObj = MyGinClass()

        self.assertEqual(myObj.noInitValue, 33)
        self.assertEqual(myObj.testValue, 30)
        self.assertEqual(myObj.myOpt._decay, 0.999993333333)
        #print myObj.testValue

if __name__ == '__main__':
  main()
