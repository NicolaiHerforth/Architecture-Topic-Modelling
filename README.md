# Mini-Project-1
Git Repo for "Mini Project 1: Quality of Life Meets Metropolitan Ambitions"


The folder 'instaloader' contains the scraping script to scrape whatever hashtag desired. 
To run the script, open the directory in your terminal and type: python instaloader "#INSERTHASTHTAG" --count INSERTCOUNT

Example: python instaloader "#norrebro" --count 10000

The script will then initialize the scrape and show a count of how many posts was scraped. The data is stored in a new directory with the name of the hashtag you entered. So if you entered #norrebro, there will now be a folder named #norrebro in your instaloader directory containing a .txt file for each post scraped.

The data manager script basically loads in all files in a given directory. You initialize the script by doing the following:
1. enter the main directory mini-1 through your terminal
2. type: python data_manager.py INSERTDIRECTORYNAME 

Example: python data_manager.py norrebro

The directory name given in your sys.argv[1] is the one that you would like to open and manage.
