<h3 align="center">
Hi there, I'm <b>Henok</b> 👋 
</h3>  

<h2 align="center">
I'm a Data Analyst and Python Programmer !
</h2> 

# Technical Skills 
![Bing](https://img.shields.io/badge/Microsoft%20Bing-258FFA?style=for-the-badge&logo=Microsoft%20Bing&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

# Machine Learning API using FastAPI 

## Introduction


## Setup

For manual installation, you need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: friendly_web_interface_for_ML_models> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate;
        python -m pip install -q --upgrade pip;
        python -m pip install -qr requirements.txt
  
- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate;
        python -m pip install -q --upgrade pip;
        python -m pip install -qr requirements.txt
The both long command-lines have a same structure, they pipe multiple commands using the symbol **;** but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## How to Run

The project consists two application. The first one accepts inputs from the user and return result with its confidentiality score. The second on accepts csv file which has input of various rows that going to be predicted. So the app read the file and retrieve records and predict for each rows and append the result with confidentiality score.

## 1. App one

- To run the first app adjust

       cd Docker_ML\New folder\Docker_ML\app
  
- The run the  python file
 
      py main.py

- Then browse to

      http://127.0.0.1:8000

## 2. App two

  - To run the second app adjust

       cd Docker_ML\New folder\Docker_ML\app_for_file
  
- The run the  python file
 
      py main.py

- Then browse to

      http://127.0.0.1:8000
        
## Screenshots

<table>
    <tr>
        <th>FastAPI</th>
        <th>FastAPI</th>
    </tr>
    <tr>
        <td><img src="./screenshots/.png"/></td>
        <td><img src="./screenshots/.png"/></td>
    </tr>
</table> -->


## Resources
Here are some resources you would read to have a good understanding of FastAPI :
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)





## Contributing

Feel free to make a PR or report an issue 😃.

Oh, one more thing, please do not forget to put a description when you make your PR 🙂.

## Author


