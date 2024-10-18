#  commands 

Generate 3 different images for the bookstoreapi. 

cd acaapibookstore/
```bash
az acr build --registry srinmantest --image bookstoreapi:v1 --file Dockerfilev1 .
az acr build --registry srinmantest --image bookstoreapi:v2 --file Dockerfilev2 .
az acr build --registry srinmantest --image bookstoreapi:v3 --file Dockerfilev3 .
az acr build --registry srinmantest --image bookstoreapi:flaky --file Dockerfileflaky .
```


