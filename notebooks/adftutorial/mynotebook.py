# Databricks notebook source
dbutils.widgets.text("input", "","")
dbutils.widgets.get("input")
y = getArgument("input")
print ("Param -\'input':")
print (y)
print ("Added Feature")
print ("Added from machine")
print ("Anil's latest changes")