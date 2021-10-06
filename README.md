# Visitor Management System

## Project Overview

UWA has several physical sites outside of the Crawley campus that allow visitor access. Currently, there is no robust system to keep track of visitors, which presents potential security and health & safety issues.

The goal of this project is to supply a robust tracking system that logs visitor movements, such that those in charge can keep track of who is present at a site, increase accountability for those using the sites, and present site usage data to management for data analysis purposes. The system will be applied across multiple sites, and as such must be robust enough to handle multiple situations as outlines in the requirements breakdown.

Some sites are more sensitive and require robust entry/exit protocols, while others are less sensitive and simply require visitors to register when they enter and exit the site. The method by which our system is applied at the site-level is outside the scope of this project; our aim is only to supply the system so that it can be accessed by visitors on their personal devices via a QR code, or via a tablet at the front desk when the site is considered sensitive. How the system is applied at any given location is considered the responsibility of those at that individual site.

### Running the Web App

Make sure that you have installed the latest version of python first. In the project folder you will see a `scripts` directory which contains build.sh and run.sh.

Also it is recommended that you use a virtual environment. You can install a virtual environment via:

```shell
pip install virtualenv
```

then create a virtual environment by running:

```shell
virtualenv <YOUR-ENVIRONMENT-NAME>
```

next start your created virtual environment. In linux run:

```shell
source <YOUR-ENVIRONMENT-NAME>/bin/activate
```
You need to install the required dependencies by running the build.sh script. Note: Run the .sh files from the parent directory of ```scripts``` directory. E.g.:

```shell
./scripts/build.sh
```

If you get an error `permision denied`, do the following:

```shell
sudo chmod u+x ./scripts/filename.sh
```

Once you have all the required dependiencies, you can go ahead and run the app like this:

```shell
./scripts/run.sh
```
