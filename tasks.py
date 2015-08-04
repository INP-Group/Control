# -*- encoding: utf-8 -*-

from invoke import Collection, run, task


@task
def build():
    print('Building!')


@task
def hi(name):
    print('Hi %s!' % name)


@task
def service_manager():
    service('services.manager')


@task
def service(name):
    config_command = "--config ./project/nameko_config.yaml"
    service_command = 'nameko run %s %s' % (config_command, name)
    run(
        "{}".format(
            service_command
        )
    )


ns = Collection('service')
ns.add_task(service_manager, name='run_manager')
