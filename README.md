To run the application you need following things:
1. AWS account
2. kubectl
3. Python
4. Docker

To run the application, you need to configure AWS service and should have the permission to access the service, then run this command to launch the working application:
kubectl port-forward svc/flask-service 5000:5000

You can see the application running on http://localhost:5000
