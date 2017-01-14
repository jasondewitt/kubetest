from kubernetes import client, config
from flask import Flask, render_template
import os.path
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def showpods():
    pods = kubeapi.list_namespaced_pod("default")
#    podnames = []

#    for pod in pods.response['items']:
#        podnames.append(pod['metadata']['name'])

    return render_template('pods.html', pods=pods)

@app.route('/pod/<podname>')
def describepod(podname):
    podresponse = kubeapi.read_namespaced_pod(podname, "default", pretty=True, exact=True, export=True)
    return render_template('pod.html', pod=podresponse)


if __name__ == "__main__":

    config.load_incluster_config()

#pods = pykube.Pod.objects(kubeapi)

    kubeapi = client.CoreV1Api()
    app.run(host='0.0.0.0', port=8000)