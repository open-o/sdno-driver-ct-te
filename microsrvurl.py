#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'liyiqun'

# microsrv_linkstat_url = 'http://127.0.0.1:32769/microsrv/link_stat'
# microsrv_linkstat_url = 'http://127.0.0.1:33710/microsrv/link_stat'
# microsrv_linkstat_url = 'http://10.9.63.208:7799/microsrv/ms_link/link/links'
# microsrv_linkstat_url = 'http://219.141.189.72:10000/link/links'
# microsrv_topo_url = 'http://10.9.63.208:7799/microsrv/ms_topo/'
# microsrv_topo_url = 'http://127.0.0.1:33769/microsrv/topo'
# microsrv_topo_url = 'http://127.0.0.1:33710/microsrv/topo'
# microsrv_topo_url = 'http://10.9.63.208:7799/microsrv/ms_topo/'
# microsrv_cust_url = 'http://10.9.63.208:7799/microsrv/ms_cust/'
# microsrv_cust_url = 'http://127.0.0.1:33771/'
# microsrv_cust_url = 'http://127.0.0.1:33710/microsrv/customer'
# microsrv_flow_url = 'http://10.9.63.208:7799/microsrv/ms_flow/flow'
# microsrv_flow_url = 'http://219.141.189.72:10001/flow'
# microsrv_flow_url = 'http://127.0.0.1:32769/microsrv/flow'
# microsrv_flow_url = 'http://127.0.0.1:33710/microsrv/flow'
# microsrv_tunnel_url = 'http://10.9.63.208:7799/microsrv/ms_tunnel/'
# microsrv_tunnel_url = 'http://127.0.0.1:33770/'
# microsrv_tunnel_url = 'http://127.0.0.1:33710/microsrv/tunnel'
# microsrv_controller_url = 'http://10.9.63.208:7799/microsrv/ms_controller/'
# microsrv_controller_url = 'http://10.9.63.140:12727/'
# microsrv_controller_url = 'http://127.0.0.1:33710/microsrv/controller'

# te_topo_man_url = 'http://127.0.0.1:32769'
# te_topo_man_url = 'http://10.9.63.208:7799/topo/'
# te_flow_man_url = 'http://127.0.0.1:32770'
# te_customer_man_url = 'http://127.0.0.1:32771'
# te_lsp_man_url = 'http://127.0.0.1:32772'
# te_lsp_man_url = 'http://10.9.63.208:7799/lsp/'
# te_flow_sched_url = 'http://127.0.0.1:32773'

te_flow_rest_port = 34770
te_sched_rest_port = 34773
te_protocol = 'http://'
te_host_port_divider = ':'
openo_ms_url_prefix = '/openoapi/microservices/v1/services'
openo_dm_url_prefix = '/openoapi/drivermgr/v1/drivers'
openo_esr_url_prefix = '/openoapi/extsys/v1/sdncontrollers'
openo_brs_url_prefix = '/openoapi/sdnobrs/v1'


#driver controller url
microsrv_juniper_controller_host = "https://219.141.189.67:8443"
# microsrv_zte_controller_host = "http://219.141.189.70:8181"
microsrv_zte_controller_host = "http://127.0.0.1:33710"
microsrv_alu_controller_host = "http://219.141.189.68"

microsrvurl_dict = {
    'openo_ms_url':'http://127.0.0.1:8086/openoapi/microservices/v1/services',
    'openo_dm_url':'http://127.0.0.1:8086/openoapi/drivermgr/v1/drivers',
    # Get SDN Controller by id only need this Method:GET
    # /openoapi/extsys/v1/sdncontrollers/{sdnControllerId}
    'openo_esr_url':'http://127.0.0.1:8086/openoapi/extsys/v1/sdncontrollers',
    # get: summary: query ManagedElement
    'openo_brs_url':'http://127.0.0.1:8086/openoapi/sdnobrs/v1',

    'te_topo_rest_port':8610,
    'te_cust_rest_port':8600,
    'te_lsp_rest_port':8620,
    'te_driver_rest_port':8670,
    'te_msb_rest_port':8086,

    'te_msb_rest_host':'127.0.0.1',
    'te_topo_rest_host':'127.0.0.1',
    'te_cust_rest_host':'127.0.0.1',
    'te_lsp_rest_host':'127.0.0.1',
    'te_driver_rest_host':'127.0.0.1',

    'microsrv_linkstat_url': 'http://127.0.0.1:33710/microsrv/link_stat',
    'microsrv_topo_url': 'http://127.0.0.1:33710/microsrv/topo',
    'microsrv_cust_url': 'http://127.0.0.1:33710/microsrv/customer',
    'microsrv_flow_url': 'http://127.0.0.1:33710/microsrv/flow',
    'microsrv_tunnel_url': 'http://127.0.0.1:33710/microsrv/tunnel',
    'microsrv_controller_url': 'http://127.0.0.1:33710/microsrv/controller',

    'te_topo_man_url': 'http://127.0.0.1:32769',
    'te_flow_man_url': 'http://127.0.0.1:32770',
    'te_customer_man_url': 'http://127.0.0.1:32771',
    'te_lsp_man_url': 'http://127.0.0.1:32772',
    'te_flow_sched_url': 'http://127.0.0.1:32773'
    }

