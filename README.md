# gcp-cloud-functions-ude

# course link & repo
https://www.udemy.com/course/cloud-functions-faas-with-python-from-zero-to-hero/learn/lecture/18015813#overview
https://github.com/DavidArmendariz/google-cloud-functions-course

# commands
python -m venv venv
source venv/bin/activate
gcloud projects list
gcloud config set project [PROJECT_ID]

## deploy (inside function folder)
gcloud functions deploy hello_world --runtime python37 --trigger-http
