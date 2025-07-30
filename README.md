# Exact test automation assignment
Creating testing framework based on BDD for website saucedemo.com. 
## Set up environment
Clone the project from GitHub:
```
git clone https://github.com/zandrei83/ExactBehave.git
```
Change working  directory:
```
cd ExactBehave
```
Create and activate virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
Install project dependencies:
```
pip install -r requirements.txt
```
### Running tests 
With HTML reports
```
behave -f html-pretty -o behave-report.html
```
Without HTML reports
```
behave features --no-capture
```