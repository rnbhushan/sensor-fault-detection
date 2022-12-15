1.Creation of virtual environment : initally default version will be assigned to virtual environment
    >> pip list
    >> pip
    >> python3 -m pip install --upgrade pip
    >>python --version
    >>python3 -m pip uninstall virtualenv
    >>python3 -m pip install virtualenv
2.Creating virtual environment by assigning unique name
    >> python3 -m virtualenv env (or)
    >> python -m venv env
3.activation of virtualenv
    >> .\env\Scripts\activate
4.building app upon the virtualenv i have made
    >> installing all the packages and dependencies
    pandas
    numoy
    matplotlib
    sklearn

    >>to run requirements.txt file
        >> pip install -r .\requirements.txt or 

        doubt  :  how to install requirements.txt


Git hub Setup :
just putl all my files will be uploaded to github

Create .gitignore file if not created in project folder and add list of files to be ignored which are related to local system
    ipynb_checkpoints
    env

1.git init >> to initialize and start tracking our local code we are using this command line.It will initiliaze empty git repositorygit
2.git add . >> it will add all our local code into history of git . "." means root directory.what ever files avilable under session it will track all
Suppose if you want to add one signgle file  :  git add .\dummy.py
3.git status  : you can see the list of files going to add to hithub in green clour
4.git commit -m 'commit name' :  it will be used for commiting the chnages we have made into our code into github
Git master branch : all our main code be strored here . among the team of 5 memebers each works their repsecive branch.All 5 developers will merge the code into main branch.
Master branch will be maintained by team lead or manager.MAster branch code will be deployed in production

5.git commit -m 'added files'

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

(env) PS C:\Users\rnbhu\session1> git config --global user.email rnbhushan@gmail.com 
(env) PS C:\Users\rnbhu\session1>  git config --global user.name rnbhushan  
git commit -m 'added files'
git status
git branch
6.to push code from local to github link
>> git remote origin git_url>
>>git remote add origin https://github.com/rnbhushan/sensor-fault-detection.git
7.git push origin branchname

>>git config --global user.name
>>(env) PS C:\Users\rnbhu\session1> pwd        

Path
----
C:\Users\rnbhu\session1

To create new branch :
git checkout -b <new-branch-name> It will create a new branch from your current branch. ...
(env) PS C:\Users\rnbhu\session1> git branch
* master
(env) PS C:\Users\rnbhu\session1> git checkout -b a
Switched to a new branch 'a'
(env) PS C:\Users\rnbhu\session1>



1.Retriving the data or code from git repository(any)
>> git clone <git-url>

(env) PS C:\Users\rnbhu\session1> git clone https://github.com/rohanpatankar926/project-mlops


Mongodb setup :

Mongodb is a no sql database stores json,xml,images and videos.Also called document database
SQL db has schema but nosql database does not have any schema

There are two procepestives in view of data.1.Data analyst and 2 one is ML engineer prosceptive

1.Data Analyst : From the partuclaual data they will just use the query for pre processing
2.ML engineer : We just see how to dump the data and how to retrive the data from database
From cloud to local and from local to cloud.ML engineer dont bothered about preprocessing
USe cloud automation and create pipeline and integrte with cicd jenkins


Two types of sclaing  : 
1.Horizontal 
2.Vertical

Horizontal : Server1 at data center with storage 100TB.After server1 storage completes,adding another one more server parallel.So total 200TB storage.Adding up the resources.One master and two child databases.Data will be shared among the three different servers.

Ex : One csv file we can push into 3 servers with replication.One server failes , we can retrives from other server


Vertical scaling :Having big computer with 100TB storage with 50tB RAM.After 100TB consumed we are not adding resources,We are adding one mored 100TB to same server.

When it comes to mnogdb it supports both but horizontal and vertical scaling but horizontal scaling efficenency is good.

Mogodb atlas is coloud nosql database
Datalake  :  all the comapnies data stroed in datalake for Azure.In AWS we use S3 buckets storage
Firebase  :  google
apis : Stored in database.

In monog db dataapi feature available


mongodb+srv://rnbhushan:1234@sensor-database.skqnwjm.mongodb.net/test

Dump data to monodb
1.Download data and store in local system
2.Create new folder and that folder create file __init.py__ to create package


https://stackoverflow.com/questions/69397039/pymongo-ssl-certificate-verify-failed-certificate-has-expired-on-mongo-atlas

### DUMP DATA TO MONGODB<br>
1-->download the data and store in local system<br>
2-->.env file and wrote all the credentials into it like url,name,dbname,coll name <br>
3-->data_mongo.py<br>
    i)-->we called the .env file and made its abject called EnvironmentVariable<br>
    ii)-->dataframe to json converted and from the we called the pymongo client and <br>
    then we pushed our complete data to mongodb<br>
    iii)--> we got all the data to mongodb-cloud in collections section <br>