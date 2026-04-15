Got it Aaradhya 💖🔥
Here are **ALL Kubernetes codes you need (clean & final for project + viva)**

---

# 🟢 1. CREATE DEPLOYMENT + SERVICE (MAIN FILE)

👉 Save as **k8s.yaml**

```yaml id="k8sfullfinal"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: analytics-v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: analytics-v1
  template:
    metadata:
      labels:
        app: analytics-v1
    spec:
      containers:
      - name: analytics
        image: pratheesha0611/analytics-app:v1
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: analytics-v1-service
spec:
  type: NodePort
  selector:
    app: analytics-v1
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30001
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: analytics-v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: analytics-v2
  template:
    metadata:
      labels:
        app: analytics-v2
    spec:
      containers:
      - name: analytics
        image: pratheesha0611/analytics-app:v2
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: analytics-v2-service
spec:
  type: NodePort
  selector:
    app: analytics-v2
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30002
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: analytics-v3
spec:
  replicas: 1
  selector:
    matchLabels:
      app: analytics-v3
  template:
    metadata:
      labels:
        app: analytics-v3
    spec:
      containers:
      - name: analytics
        image: pratheesha0611/analytics-app:v3
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: analytics-v3-service
spec:
  type: NodePort
  selector:
    app: analytics-v3
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30003
```

---

# 🟢 2. APPLY DEPLOYMENT

```bash id="kapply"
kubectl apply -f k8s.yaml
```

---

# 🟢 3. CHECK PODS

```bash id="kpods"
kubectl get pods
```

---

# 🟢 4. CHECK SERVICES

```bash id="ksvc"
kubectl get services
```

---

# 🟢 5. DELETE EVERYTHING

```bash id="kdel"
kubectl delete -f k8s.yaml
```

---

# 🟢 6. RESTART DEPLOYMENT

```bash id="krestart"
kubectl rollout restart deployment analytics-v1
kubectl rollout restart deployment analytics-v2
kubectl rollout restart deployment analytics-v3
```

---

# 🟢 7. VIEW LOGS

```bash id="klogs"
kubectl logs <pod-name>
```

---

# 🟢 8. PORT FORWARD (IF BROWSER NOT WORKING)

```bash id="kpf"
kubectl port-forward service/analytics-v1-service 5001:5000
kubectl port-forward service/analytics-v2-service 5002:5000
kubectl port-forward service/analytics-v3-service 5003:5000
```

---

# 🟢 9. CHECK NODES

```bash id="knodes"
kubectl get nodes
```

---

# 🟢 10. DESCRIBE POD (DEBUG)

```bash id="kdesc"
kubectl describe pod <pod-name>
```

---

# 🧠 VIVA SHORT ANSWER

> Kubernetes is used to deploy, manage, and scale containerized applications. In this project, deployments and services were used to run different versions of the application and expose them via NodePorts.

---

# 🎯 FINAL SUMMARY

```text id="summaryk8s"
kubectl apply → deploy app
kubectl get pods → check running
kubectl get services → check ports
kubectl delete → remove deployment
```

---

# 🎉 YOU ARE DONE 💖🔥

If you want:
👉 1-page report
👉 PPT slides
👉 Viva questions

Just tell me 😎✨
Got you Aaradhya 💖🔥
Here is your **FULL DOCKER CODE (everything you need for project + viva)**

---

# 🟢 1. DOCKERFILE (MAIN CODE)

👉 Create file: `Dockerfile`

```dockerfile
# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
```

---

# 🟢 2. BUILD IMAGE (V1)

```bash
docker build -t pratheesha0611/analytics-app:v1 .
```

---

# 🟢 3. CREATE V2 & V3 (TAGGING)

```bash
docker tag pratheesha0611/analytics-app:v1 pratheesha0611/analytics-app:v2
docker tag pratheesha0611/analytics-app:v1 pratheesha0611/analytics-app:v3
```

---

# 🟢 4. RUN CONTAINER (TEST LOCALLY)

```bash
docker run -d -p 5000:5000 pratheesha0611/analytics-app:v1
```

👉 Open:

```
http://localhost:5000
```

---

# 🟢 5. LOGIN TO DOCKERHUB

```bash
docker login
```

---

# 🟢 6. PUSH IMAGES

```bash
docker push pratheesha0611/analytics-app:v1
docker push pratheesha0611/analytics-app:v2
docker push pratheesha0611/analytics-app:v3
```

---

# 🟢 7. CHECK IMAGES

```bash
docker images
```

---

# 🟢 8. CHECK RUNNING CONTAINERS

```bash
docker ps
```

---

# 🟢 9. STOP CONTAINER

```bash
docker stop <container_id>
```

---

# 🟢 10. REMOVE CONTAINER

```bash
docker rm <container_id>
```

---

# 🟢 11. REMOVE IMAGE

```bash
docker rmi pratheesha0611/analytics-app:v1
```

---

# 🧠 VIVA ANSWER (IMPORTANT)

👉 **What is Docker?**

> Docker is a containerization platform used to package applications and their dependencies into containers, ensuring consistent execution across environments.

---

# 🧠 YOUR PROJECT FLOW

```text
Code → Dockerfile → Build Image → Tag → Push → Deploy in Kubernetes
```

---

# 🎯 ONE-LINE FOR EXAM

> Docker was used to containerize the application and create versioned images (v1, v2, v3), which were pushed to DockerHub for deployment.

---

# 🎉 YOU COMPLETED EVERYTHING 💖🔥

If you want next:
👉 PPT
👉 Report
👉 Viva Q&A

Just tell me 😎✨
