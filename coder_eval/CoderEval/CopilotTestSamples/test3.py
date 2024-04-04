from ex3 import _replace_register
import unittest

# CONSTANT FOR TESTING
REG_INGRESS_BW_LIMIT = 3
REG_MIN_BW = 4
REG_PORT = 5
REG_NET = 6
# for logging remote group rule
REG_REMOTE_GROUP = 7

INGRESS_BW_LIMIT_REG_NAME = "reg_ingress_bw_limit"
MIN_BW_REG_NAME = "reg_min_bw"
PORT_REG_NAME = "reg_port"
NET_REG_NAME = "reg_net"
REMOTE_GROUP_REG_NAME = "reg_remote_group"

class TestAll(unittest.TestCase):
    """TestAll class to run tests."""

    def test_no_register_defined(self):
       flow_params = {'foo': 'bar'}
       _replace_register(flow_params, REG_PORT, PORT_REG_NAME)
       _replace_register(flow_params, REG_NET, NET_REG_NAME)
       _replace_register(flow_params,
                      REG_REMOTE_GROUP,
                      REMOTE_GROUP_REG_NAME)
       _replace_register(flow_params,
                      REG_MIN_BW,
                      MIN_BW_REG_NAME)
       _replace_register(flow_params,
                      REG_INGRESS_BW_LIMIT,
                      INGRESS_BW_LIMIT_REG_NAME)
       self.assertEqual({'foo': 'bar'}, flow_params)
     
    def test_all_registers_defined(self):
       flow = {'foo': 'bar',
                PORT_REG_NAME: 1,
                NET_REG_NAME: 2,
                REMOTE_GROUP_REG_NAME: 3,
                INGRESS_BW_LIMIT_REG_NAME: 4,
                MIN_BW_REG_NAME: 5}
       expected_flow = {'foo': 'bar',
                         'reg{:d}'.format(REG_PORT): 1,
                         'reg{:d}'.format(REG_NET): 2,
                         'reg{:d}'.format(REG_REMOTE_GROUP): 3,
                         'reg{:d}'.format(REG_INGRESS_BW_LIMIT): 4,
                         'reg{:d}'.format(REG_MIN_BW): 5}
       _replace_register(flow, REG_PORT, PORT_REG_NAME)
       _replace_register(flow, REG_NET, NET_REG_NAME)
       _replace_register(flow,
                      REG_REMOTE_GROUP,
                      REMOTE_GROUP_REG_NAME)
       _replace_register(flow,
                      REG_MIN_BW,
                      MIN_BW_REG_NAME)
       _replace_register(flow,
                      REG_INGRESS_BW_LIMIT,
                      INGRESS_BW_LIMIT_REG_NAME) 
       self.assertEqual(expected_flow, flow)
