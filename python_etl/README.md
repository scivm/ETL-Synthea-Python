# Python-based ETL of Synthea data to OMOP CSV files

This is an implementation of the Synthea Extract-Transform-Load (ETL)
specification designed to generate a set of CDMv5 or CDMv6 compatible CSV files
that can then be bulk-loaded into your RDBMS of choice.

It is designed to be massively scalable but still run on a user's workstation or laptop

We follow a similar mapping stratedgy as Synthea-ETL.

We implemented the drug era and condition era sql scripts into multi threaded python.  There are limits
what can be done when running a single sql query against a postgres database.

## Overview of Steps

0) Shortcut: download ready-to-go data

1) Install required software

2) Download Synthea and generate csv files

3) Download CDMv5 Vocabulary files

4) Setup the .env file to specify file locations

5) Test ETL with test data

6) Run ETL on CMS data

7) Load data into the database

8) Create ERA tables

9) Open issues and caveats with the ETL

## 0. Shortcut: download ready-to-go data

We provide several downloads of ready to go data for CDMv5.3.1 and CDMv6 for multiple countries

### CDM V5.3.1
We have prepared a downloadable OMOP CDMv5.3.1 version.  The data can be retrieved from our github [Github](https://).  The file is called synthea_100k.tar.gz. It is approximately 3 GB in size. It contains synthetic v5.3.1 CDM data files for 100,000 persons. The .gz files in this file will need to be extracted and decompressed after download. The decompressed files have no file suffixes but they are comma delimited text files. There are no header records in the files. The CDM vocabulary version is "v5.0 05-NOV-17".

### CDM V6
We have prepared a downloadable OMOP CDMv6 version.  The data can be retrieved from our github [Github](https://).  The file is called synthea_100k.tar.gz. It is approximately 3 GB in size. It contains synthetic v6 CDM data files for 100,000 persons. The .gz files in this file will need to be extracted and decompressed after download. The decompressed files have no file suffixes but they are comma delimited text files. There are no header records in the files. The CDM vocabulary version is "v5.0 05-NOV-17"

### Sample Postgres Upload Script
 
Here is an example PostgreSQL psql client copy command to load the concept file into the concept table in a schema called 'cdm'. 
 
\copy cdm.concept from '/download_directory_path/concept' null as '\\000' delimiter ','

You are completed after this step.


## 1. Install required software

The ETL process requires Python 2.7 with the python-dotenv package.

### Linux

Python 2.7 and python-pip must be installed if they are not already
present. If you are using a RedHat distribution the following commands
will work (you must have system administrator privileges):

``sudo yum install python``  
``sudo yum install python-pip``

The python-pip package enables a non-administrative user to install
python packages for their personal use. From the python_etl directory
run the following command to install the python-dotenv package:

``pip install -r requirements.txt``

### Windows + Cygwin

We have been able to run the ETL under Windows using cygwin, available at
<https://www.cygwin.com>. Be sure to install the following packages
with the cygwin installer:

python  
python-setuptools  

After that run the following in order to install pip:  
``easy_install-2.7 pip``

Then to install python-dotenv, run the following command within the python\_etl folder:  
``pip install -r requirements.txt``


## 2. Download Synthea and run for your country

## 3. Download CDMv5 Vocabulary files
Download vocabulary files from <http://www.ohdsi.org/web/athena/>, ensuring that you select at minimum, the following vocabularies:
SNOMED, ICD9CM, ICD9Proc, CPT4, HCPCS, LOINC, RxNorm, and NDC.

- Unzip the resulting .zip file to a directory.
- Because CPT4 vocabulary is not part of CONCEPT.csv file, one must download it with the provided cpt4.jar program via:
``java -jar cpt4.jar``, which will append the CPT4 concepts to the CONCEPT.csv file.

## 4. Setup the .env file to specify file locations
Edit the variables in the .env file which specify various directories used during the ETL process.
Example .env files are provided for Windows (.env.example.windows) and unix (.env.example.unix) runs,
differing only in path name constructs.

- Set BASE\_SYNTHEA\_INPUT\_DIRECTORY to where the generated synthea csv
directories are contained.
- Set BASE\_OMOP\_INPUT\_DIRECTORY to the CDM v5 vocabulary directory, for example: /data/vocab_download_v5.
- Create a directory and set its path to BASE\_OUTPUT\_DIRECTORY. This
directory will contain all of the output files after running the ETL.
- Create a directory and set its path to
BASE\_ETL\_CONTROL\_DIRECTORY. This contains files used for
auto-incrementing record numbers and keeping track of physicians
and physician institutions when running multiple sets of synthea files

## 5. Test ETL with DE_0 CMS test data
We have provided the directory named DE_0 inside the
python_etl/test_data directory. Copy this directory to your input
directory containing the DE_X directories. This directory has sample
input corresponding to 2 persons which can be used to check the
desired output. It is based on the hand-coded samples.

Run the ETL process on the files in this directory with:  
``python CMS_SynPuf_ETL_CDM_v5.py 0``  
and check for the output generated in the BASE\_OUTPUT\_DIRECTORY
directory.  A .csv file should be generated for each of the CDM v5 tables,
suitable for comparing against the hand-coded outputs.  Note at this
time, all of the tables have been implemented, but some might be empty (e.g visit_cost and device_cost) due to lack of data.
Clean out the control files in BASE\_ETL\_CONTROL\_DIRECTORY before running the next step.

## 6. Run ETL on CMS data

To process any of the DE_1 to DE_20 folders, run:

- ``python CMS_SynPuf_ETL_CDM_v5.py <sample number>``
    - Where ``<sample number>`` is the number of one of the samples you created from synthea
    - e.g. ``python CMS_SynPuf_ETL_CDM_v5.py 4`` will run the ETL on the SynPUF data in the DE_4 directory
    - The resulting output files should be suitable for bulk loading into a CDM v5 database.

The runs cannot be done in parallel because counters and unique
physician and physician institution providers are detected and carried
over multiple runs (saved in BASE\_ETL\_CONTROL\_DIRECTORY). We
recommend running them sequentially from 1 through 20 to produce a
complete ETL of the approximately 2.33M patients. If you wanted only
1/20th of the data, you could run only sample number 1 and load the
resulting .csv files into your database.

N.B. - On average, the Synthea_ETL_CDM_v5.py program takes approximately 45-60 minutes to process one input file (e.g. DE_1).  We executed the program
on an Intel Xeon CPU E3-1271 v3, with 16GB of memory and it took approximately 14 hours to process all 20 DE files.

## 7. Load data into the database
The PostgreSQL database was used for testing and we provided copies of the relevant PostgreSQL-compliant SQL code to create an OMOP CDMv5.3.1 database,
and load the data into PostgreSQL. As the common data model changes to 5.3.1 and beyond, this ETL would have to be updated,
and new copies of the relevant SQL code be retrieved from the [CommonDataModel repository](https://github.com/OHDSI/CommonDataModel), where
SQL code is maintained for PostgreSQL, Oracle, and SQL Server database construction. The instructions below are exclusively for PostgresSQL,
and would have to be adapted slightly for other databases.

To create tables in a PostgreSQL database or to load the .csv files created by ETL programs to a PostgreSQL database,
the queries can be executed in pgadmin III or a PostgreSQL psql terminal.
 - to run the queries in pgadmin III, open the sql file in pgadmin III and click on the run button.
 - to run the queries in PostgreSQL terminal (psql), run ``psql``, then type the command ''\i XXXX.sql'' where XXXX.sql is an sql file. Alternately you can run an SQL file from the command line via ``psql -f XXXX.sql``.

a) Login to the PostgreSQL database and create a new database. e.g. ``CREATE DATABASE ohdsi``

b) If you don't want to use the public schema, create a new empty schema.  e.g. ``CREATE SCHEMA synpuf5``

c) Create a separate empty schema for ACHILLES results e.g. ``CREATE SCHEMA results``

d) Download  [create_CDMv5_tables.sql](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/create_CDMv5_tables.sql) and replace the schema name synpuf5 with the new schema created in step (b). Execute the file via the PostgreSQL psql terminal or pgadmin III. This file has the queries to create the OMOP CDMv5 tables, also creating the vocabulary tables within the schema.

e) If the queries in step (d) executed successfully, all the tables will have been created under the new schema you used, and are empty.

 To load the vocabulary data into the tables, download [load_CDMv5_vocabulary.sql](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/load_CDMv5_vocabulary.sql) and make the following changes in this file:
- Replace the schema name synpuf5 with the schema you created in in step (b).
- Change BASE_OMOP_INPUT_DIRECTORY to the directory where you store your vocabulary files that you want to load into PostgreSQL.

Execute the queries in the modified file. These queries will copy the vocabulary data from csv files to the PostgreSQL database.

To load the data from DE_1 to DE_20 into tables, download [load_CDMv5_synpuf.sql](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/load_CDMv5_synpuf.sql) and make the following changes in this file:
- Replace the schema name synpuf5 with the schema you created in in step (b)
- Replace the location of the input csv files that you want to load to PostgreSQL.

Execute the queries in the modified file. These queries will import the ETL .csv data from DE_1 through DE_20 to the PostgreSQL database.

f) Create constraints: If the step (e) executed successfully, records were inserted into tables and now primary and foreign keys can be assigned to all tables. Download
    the sql file [create_CDMv5_constraints](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/create_CDMv5_constraints.sql) and update the schema name with the schema you created in step (b).
    Execute the queries present in the downloaded file. Make sure you have loaded all of  your data from step (e) before running this step. If you add the constraints before loading the data, it will slow down
    the load process because the database needs to check the constraints before adding any record to the database.

g) Though the database will create indexes for primary keys, but the queries will take minutes to execute if the search is not based on the primary keys.
    Additional indexes based on foreign keys and other frequently used fields need to added to the tables to improve the query execution time. Download
    the sql file [create_CDMv5_indices](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/create_CDMv5_indices.sql) and update the schema with the schema you created in step (b). Execute the queries in the modified file. This concludes the database creation, loading, and optimization.

## 8. Create ERA tables
  Once you are done with all the steps mentioned in section (7), you can generate data for drug_era and condition_era tables as follows:

  a) condition_era: Download the sql file [create_CDMv5_condition_era.sql](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/create_CDMv5_condition_era.sql) and update the schema with the
    schema you created in step (7b). Execute the queries present in the modified file.

  b) drug_era: Download sql file [create_CDMv5 _drug_era_non_stockpile.sql](https://github.com/OHDSI/ETL-CMS/blob/master/SQL/create_CDMv5_drug_era_non_stockpile.sql) and update the schema with the
    schema you created in step (7b). Execute the queries present in the modified file.
  N.B. - The queries to create drug_era and condition_era tables might take approx 48 hours.


## 9. Open issues and caveats with the ETL
