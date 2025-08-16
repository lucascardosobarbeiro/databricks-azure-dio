# Databricks notebook source
# MAGIC %md
# MAGIC Dados gerais

# COMMAND ----------

# MAGIC  %sql
# MAGIC  SELECT * FROM `hive_metastore`.`default`.`products`;

# COMMAND ----------

# MAGIC %md
# MAGIC Filtrar road bikes
# MAGIC

# COMMAND ----------

 df = spark.sql("SELECT * FROM products")
 df = df.filter("Category == 'Road Bikes'")
 display(df)
