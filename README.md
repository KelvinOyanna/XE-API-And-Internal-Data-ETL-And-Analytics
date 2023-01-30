# Problem 1 Solution
### Description:
The goal of this project is to generate a summarized table from the provided loan, borrower and payment data which, can be used for performance analytics by the company's management.

On execution, the program loads all the data from multiple CSV files, perform data cleaning and transformation on the data, in order to get it in the right format for the destination database and then loads the data to tables in a Postgresql database.
Finally the program creates a summarize analytics from the tables and write it output to an Excel file.

### Pre-requisite:
- In order to run the program, you will first need to download the required data and store in a folder called 'data' in the project directory.
- Create a database in a Postgresql instance.
- Use the create_database_table.sqlfile in the project directory to create the required tables in your database.

### Setting-up environment:
Follow the steps below to setup your environment for running the program: 
 - Clone this repository
 - Change directory into the project directory using the command: cd AutoChek-DE-Technical-Assessment
 - Create and activate a virtual environment by running the code below:
    - python3 -m venv name-of-virtual-environment   --- (Create virtual environment)
    - source ./name-of-virtual-environment/bin/activate   --- (Activate environment.)
    - pip -r install requirements.txt (Install libraries/dependencies)
 
- Create an environment variable file (.env) to store API & database credentials/secrets by running:
    - touch .env
<P> Your .env file should contain the code below. Replace the value of the variables with your credentials
- ACCOUNT_ID=yourXE_AccountID
- API_KEY=your_XE_API_KEY

- DB_USER_NAME=your_postgreql_database_username
- DB_PASSWORD=your_postgresql_database_password
- DB_NAME=your_postgresql_database_name
- PORT=5432
- HOST=your_postgresql_database_instance_host/IP

### Running the program:
To run the programe from the command line, run below code:
- cd Problem_1_Solution
- python3 main.py 

### Output:
The output of the program can be found in a folder named 'output' within the project folder.


# Problem 2 Solution
### Description:
The goal of this project is to create a data extraction pipeline that pulls currency exchange data from XE web API. This data is futher transformed in the required format.
<p> On execution, the program pulls the latest currency exchange rate data from XE website, write the raw data into an external JSON file in the directory 'raw' within the project directory. The raw data is futher extrated and transformed into the required format. The final tranformed exchange rates data can be found in the directory named 'transformed'. Saving the pulled raw data helps for backfilling data when needed and also saves cost on sending requests to the API.

### Pre-requisite:
- You will need to first create an account on XE platform [using this link](https://www.xe.com/)
- Add your XE account_ID and API key to the .env file you created in Project 1 above.

### Setting-up environment:
Your environment has been set up from project 1 above.

### Running the program:
To run the program from the command line, run below code:
- cd Problem_2_Solution
- python3 main.py 

### Scheduling the Script:
To schedule the script to pull exchange rate data by 1am and 11pm, execute the bash script (scheduler.sh) from a LINUX machine using the code below:
- ./scheduler.sh
NB: Modify the scheduler.sh script to point to the correct file path of the scripts

### Output:
The output of the program can be found in a folder named 'transformed' within the project folder.