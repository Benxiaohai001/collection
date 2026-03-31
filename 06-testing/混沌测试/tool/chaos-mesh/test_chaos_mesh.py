import uuid, time
from chaosmesh.client import Client, Experiment
from chaosmesh.k8s.selector import Selector

# creating the ChaosMesh client
client = Client(version="v1alpha1")

# target pods selector; by labelSector or by pods in specified namespaces
selector = Selector(labelSelectors=None, pods={"cnosdb-community-latest-3meta-2querytskv":   ["my-cnosdb-meta-0"]}, namespaces=["cnosdb-community-latest-3meta-2querytskv"])
print(selector);

exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start_experiment(Experiment.POD_KILL, namespace="cnosdb-community-latest-3meta-2querytskv", name=exp_name, selector=selector)

time.sleep(20)

client.delete_experiment(Experiment.POD_KILL, namespace="cnosdb-community-latest-3meta-2querytskv", name=exp_name)