# Databricks notebook source


# COMMAND ----------

# rest1.py
# This script should demo databricks REST API.
# ref:
# goog: With python how to authenticate to REST API?
# http://docs.python-requests.org/en/latest/
import requests
usr='r.rahul.deshmukh@sapphireondemand.com'
pas='dapi748a8e2e3d9113f3e74463038cef972d'
hhost         = 'https://abc-12345-911.cloud.databricks.com/api/1.2'
clusters_list = hhost+'/clusters/list'
rq1 = requests.get(clusters_list, auth=(usr,pas))
print(rq1.status_code)
print(rq1.json())
print("hello")