# Azure_Microsoft_Fabric_Data_Engineering_Project
This repo contains details about a data engineering project leveraged using Microsoft Fabric

**Description:**
      Utilized sample SalesLT tables, loaded the data from SQL datawarehouse into ADLS GEN2 storage by ADF, due to permission/access issues, manually uploaded into Fabric Lakehouse storage into the raw folder, utilized Fabric Notebook to perform transformations from raw to Conformed to Purpose Built storage buckets, manually created Fabric tables using Gold layer files, then created sample PowerBI report on the top of the gold layer. Thanks
      
**Source Details:**
      Deployed Sample SalesLT tables inside Azure SQL data warehouse, Utilized ADF to extract the multiple tables using lookup and for each to load the data into ADLS Gen2 storage
      
**Table Names:**

      1.SalesLT.Address
      2.SalesLT.Customer
      3.SalesLT.CustomerAddress
      4.SalesLT.Product
      5.SalesLT.ProductCategory
      6.SalesLT.ProductDescription
      7.SalesLT.ProductModel
      8.SalesLT.ProductModelProductDescription
      9.SalesLT.SalesOrderDetail
     10.SalesLT.SalesOrderHeader

**ADF_Pipeline details:** 
      Raw data was selected from Azure SQL Database, SalesLT Schema
      Pipeline was built using lookup activity and ForEach activity and loaded the data into Fabric Lakehouse (Due to permissions issues, utilized ADF from regular services rather than Fabric ADF and manually uploaded files in Fabric Lakehouse)
Pipeline repo: https://github.com/vinaykm5758/Azure_Microsoft_Fabric_Data_Engineering_Project/tree/adf_pipeline
Pipeline Image: https://github.com/vinaykm5758/Azure_Microsoft_Fabric_Data_Engineering_Project/blob/main/ADF_Pipeline_Details.PNG
      
**Transformation from Raw to Conformed to Purpose Built details:**
**1. Raw to Conformed:**
      Transformations are done with Fabric Notebook, just modified the DateModified to Date Column and tested it successfully.
      Parquet Files are converted to DELTA format and loaded into the conformed layer
**2. Conformed to Purpose Built:**
      Transformations are done with Fabric Notebook, added a new column DateTimeLoaded, and tested it successfully
      Delta files are then transformed and loaded into the Purpose_built layer, Also, manually tested loading the files from Lakehouse to SQL tables
Notebook URL: https://github.com/vinaykm5758/Azure_Microsoft_Fabric_Data_Engineering_Project/blob/main/V_Raw_to_Conformed_To_PurposeBuilt_Transformations.ipynb

**PowerBI Report details:** tested the joins and created a sample PowerBI Report on top of the Purpose_Built Layer
PBIX file URL: https://github.com/vinaykm5758/Azure_Microsoft_Fabric_Data_Engineering_Project/blob/main/Fabric_Sample_PowerBI_Report.pbix


Please note: more enhancements and code optimizations are required and will be performed in future projects. Thanks
