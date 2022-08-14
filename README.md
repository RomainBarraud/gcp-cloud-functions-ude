# gcp-cloud-functions-ude

# course link & repo
https://www.udemy.com/course/cloud-functions-faas-with-python-from-zero-to-hero/learn/lecture/18015813#overview
https://github.com/DavidArmendariz/google-cloud-functions-course

# commands
python -m venv venv
source venv/bin/activate
gcloud projects list
gcloud config set project [PROJECT_ID]
import secrets
secrets.token_hex(16)
git rm -r --cached .
```
fetch('https://us-central1-cloud-functions-course-2c8c3.cloudfunctions.net/hello_world', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({'name': 'Romain', 'lastname': 'B.'})}).then(response => response.text()).then(result => console.log(result))
```

## deploy (inside function folder)
### locally
functions-framework --target hello_world --debug
functions-framework --target send_mail --debug

### cloud
gcloud functions deploy hello_world --runtime python37 --trigger-http
gcloud functions deploy send_mail --runtime python37 --trigger-http --env-vars-file .env.yaml --allow-unauthenticated