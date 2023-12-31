# Report-Reader

## Overview
This project creates a container image that will run a web application designed to serve the reports generated by report-writer

## Details
This application is built using Flask.  The main blueprint serves up all of the content - including static content and templates.  
The application uses a blueprint so that it can be easily moved up and down the URI hierarchy.  Specify the REPORT_READER_PREFIX environment variable in order to tell the application where it lives in this hierarchy.  

These environment variables control the application's behavior:

| KEY                  | SAMPLE VALUE |
|----------------------|--------------|
| REPORT_READER_PREFIX | /neurology   |
| REPORT_READER_NAME   | Neurology    |

The application is built to serve reports (static content) from a persistent volume.  It is assumed this volume is mounted at /app/main/static/reports.

## Build
example: 

```bash
docker build -t report-reader:latest .
docker tag report-reader:latest acr7c02.azurecr.io/report-reader:latest
docker push acr7c02.azurecr.io/report-reader:latest
```