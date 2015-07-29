# -*- encoding: utf-8 -*-



from nameko.standalone.rpc import ClusterRpcProxy


config = {'AMQP_URI': 'amqp://guest:guest@localhost'}

with ClusterRpcProxy(config) as cluster_rpc:
    # data = cluster_rpc.process_manager.hello('sdk.wialon.pro')
    data = cluster_rpc.process_manager.run_test()
    print(data)
