# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for divitional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name, unused-argument
#
# This file is part of DNN compiler maintained at
# https://github.com/ai-techsystems/dnnCompiler

import common

import dnnc as dc
import numpy as np
import unittest

class DivTest(unittest.TestCase):
    def setUp(self):
        self.len = 48
        self.np_a = np.random.randn(self.len).astype(np.float32)
        self.np_b = np.random.randn(self.len).astype(np.float32)
        self.dc_a = dc.array(list(self.np_a));
        self.dc_b = dc.array(list(self.np_b));

    def test_Div1D (self):
        npr = np.divide(self.np_a, self.np_b)
        dcr = dc.div(self.dc_a, self.dc_b)
        np.testing.assert_allclose(npr, np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)

    def test_Div2D (self):
        np_a = np.reshape(self.np_a, (6,8))
        np_b = np.reshape(self.np_b, (6,8))
        dc_a = dc.reshape(self.dc_a, (6,8));
        dc_b = dc.reshape(self.dc_b, (6,8));
        npr = np.divide(np_a, np_b);
        dcr = dc.div(dc_a, dc_b);
        np.testing.assert_allclose(npr.flatten(), np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)

    def test_Div3D (self):
        np_a = np.reshape(self.np_a, (4,4,3))
        np_b = np.reshape(self.np_b, (4,4,3))
        dc_a = dc.reshape(self.dc_a, (4,4,3));
        dc_b = dc.reshape(self.dc_b, (4,4,3));

        npr = np.divide(np_a, np_b);
        dcr = dc.div(dc_a, dc_b);

        np.testing.assert_allclose(npr.flatten(), np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)

    def test_Div4D (self):
        np_a = np.reshape(self.np_a, (4,2,2,3))
        np_b = np.reshape(self.np_b, (4,2,2,3))
        dc_a = dc.reshape(self.dc_a, (4,2,2,3));
        dc_b = dc.reshape(self.dc_b, (4,2,2,3));

        npr = np.divide(np_a, np_b);
        dcr = dc.div(dc_a, dc_b);

        np.testing.assert_allclose(npr.flatten(), np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)

    def tearDown(self):
        return "test finished"

if __name__ == '__main__':
    unittest.main()
    