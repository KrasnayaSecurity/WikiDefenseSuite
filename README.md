WikiDefenseSuite
================

A group of tools designed to protect and monitor the wiki.

Wiki Crawler
------------

The script `wiki_crawler.py` is intended for crawling wikis in search of various trigger words.

**Configuration:**

`domain`: The domain of the wiki that you are going to crawl

`entry`: The entry page of the wiki.  Set this to only the page title, properly URL encoded.

`search_terms`: A list of case insensitive words that that the crawler will look for in page text

`require`: Text that must be present in URLs in order for them to be Q'd by the crawler

`exclude`: Text in URLs that will disqualify them from crawling


