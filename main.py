import operator
import pykube
from flask import Flask, render_template
import os.path



app = Flask(__name__)

@app.route('/')
def showpods():
    pods = pykube.Pod.objects(kubeapi)
    podnames = []

    for pod in pods.response['items']:
        podnames.append(pod['metadata']['name'])

    return render_template('pods.html', podnames=podnames)



if __name__ == "__main__":

    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount'):
        kubeapi = pykube.HTTPClient(pykube.KubeConfig.from_service_account())
    else:
        kubeapi = pykube.HTTPClient(pykube.KubeConfig.from_file('~/.kube/config'))
    pods = pykube.Pod.objects(kubeapi)


    app.run(host='0.0.0.0', port=8000)