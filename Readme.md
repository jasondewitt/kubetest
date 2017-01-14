 KubeTest
==========
A **very** basic Kubernetes demo I created while working on learning Kubernetes. Docker container that contains a 
python webapp that uses 
the [Kubernetes Incubator 
python client](https://github.com/kubernetes-incubator/client-python) to list the pods running on the cluster and 
describe each pod when clicked on.

Assuming you already have a cluster up and running with kubectl configured to control it, start by creating the 
deployment:
```
kubectl create -f kube/kubetest.yml
```

Then add the service to expose the pod and allow access to it:
```
kubectl create -f kube/kubetest-service.yml
```

