#! /usr/bin/python

#This .py file is not to be executed as an isolated script
#This .py file will be imported into the PasswordCompare.py script 
#It allows RSS feeds to be pulled from the internet and displayed 

#import the "feedparser" open-source Python module 
import feedparser

#Parses RSS feeds from reddit subreddits 
def subreddit(myInput):
	d = feedparser.parse("http://www.reddit.com/r/" + myInput + "/.rss")
	print_rss(d)
	
#prints the title and URL for the first 10 RSS entries 
def print_rss(parse_results):
	
	index = 1
	for post in parse_results.entries[0:10]:
		print(str(index) + ") " + post.title)
		#print post.title
		#print post.link
		#print ("\n")

		index = index + 1

#Unused function that allows sports RSS feeds to be parsed and displayed
def sports(myInput):
	d = feedparser.parse("http://sports.espn.go.com/espn/rss/" + myInput + "/news")
	print_rss(d)
 
#Unused function that allows traffic RSS feeds to be parsed and displayed
def traffic(myInput):
	base_url = "http://traffic.houstontranstar.org/data/rss/traffic_rss_"
	
	if myInput == "I10W":
		d = feedparser.parse(base_url + "ih-10_katy.xml")
	if myInput == "I10E":
		d = feedparser.parse(base_url + "ih-10_east.xml")
	if myInput == "I45N":
		d = feedparser.parse(base_url + "ih-45_north.xml")
	if myInput == "I45S":
		d = feedparser.parse(base_url + "ih-45_gulf.xml")

	print_rss(d)


	
