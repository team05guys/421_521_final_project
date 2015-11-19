#! /usr/bin/python

import feedparser

#prints the title and URL for the first 10 RSS entries 
def print_rss(parse_results):
	for post in parse_results.entries[0:10]:
		print post.title
		print post.link
		print ("\n")

def subreddit(myInput):
	d = feedparser.parse("http://www.reddit.com/r/" + myInput + "/.rss")
	print_rss(d)	

	
def sports(myInput):
	d = feedparser.parse("http://sports.espn.go.com/espn/rss/" + myInput + "/news")
	print_rss(d)
 
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


	
