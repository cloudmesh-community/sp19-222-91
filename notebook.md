
#1/11/19 __init.py__: initializes and tells python that the current
directory is a python directory
setup.py: where you can tell the computer to download libraries
via pip or something
requirements.txt:gets dependencies for our program

from setuptools import setup
setup(name = 'hello', version='1.0.0', url='',author='tjzhang',packages=['']

The command 'pip freeze > requirements.txt' writes the dependencies
for the current version of pip to the file requirements.txt To install
the module requirements, use 'pip install -r requirements.txt .'.

#1/21/19
Dictionaries: S 3.5.7.4
Add SSH key to Github: S 4.5

#1/23/19:
Read REST section in book by Thursday 9.1 ssh-add
Going through the specified REST tutorial on next Thursday.
A cloud data center utilizes containers and virtualization.

#2/5/19
.yaml files contain endpoint, REST method, and python code
Starting a local server in nist/examples/flask-connexion-swagger
Installed requirements in testENV pyenv

#2/7/19
Learned more about .yaml files and how they specify how to use
URLs to tell the server what to do.

#2/11/19
Cleaned up Github repo.
Learned to read and plot data from CSV files using pandas.
Useful commands:

.iloc()
.select_dtypes()
.boxplot()

Need project proposal by Thursday

#2/14/19
Went through the swagger tutorial.

#2/19/19
Learned about MapReduce and HDFS.

#3/7/19
Make sure we can visualize the data using endpoints.
Downloading a file from Google Drive by copying the URL and writing it to a file.
url = ; #get the url somehow, make sure it is a directly downloadable link
def download_data(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def download(output):
    output_file = 'data/'+output
    download_data(url=url, filename=output_file)
    return str(output) + " Downloaded"

Reading in the data:
read_csv with pandas, select_dtypes(), permutations(), math.floor(),
Figure out how to upload an input file to predict outputs.

#3/19/2019
Did a sample k-nearest classification project with cars. We used Euclidean
distance formula to calculate the nearest neighbors. We normalized the data's
features so that no individual column has an artificial weight. For instance,
in our example, the car year is 3 orders of magnitude more significant than the
transmission, but normalizing the columns keep the importance of each feature
in relation to the other features constant.

#3/21/2019
Continuing the previous day's example, the impact of normalizing each feature
was shown to be very significant. The Euclidean distance for each point in the
dataset adjusted quite a bit after standardizing each feature column. This was
shown in the results: originally the Jeep Wrangler was the car with the least
distance to the Chevy Malibu, but after standardization, the Honda Civic was
closest. The standardization also changes the k value.
