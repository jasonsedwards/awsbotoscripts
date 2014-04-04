#The code below can be used to register/deregister a EC2 instance with the Elastic Load Balancer

#Import boto elb Library
import boto.ec2.elb
class ElbManage:
  #create a connection to the region containing our ELB.
  def __init__(self, region):
    global elb = boto.ec2.elb.connect_to_region(region)
  #grab our load balancer and register the instance with it.
  def register(instIds, loadBalancerName):
    lb = elb.get_all_load_balancers(load_balancer_names=[loadBalancerName])
    lb[0].register_instances(instIds)
  #grab our load balancer and deregister the instance with it.
  def deregister(instIds, loadBalancerName):
    lb = elb.get_all_load_balancers(load_balancer_names=[loadBalancerName])
    lb[0].deregister_instances(instIds)
