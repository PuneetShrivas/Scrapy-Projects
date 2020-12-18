# Scrapy-Projects
Tutorial Notes 
	• Use virtual environment
	• Install Scrapy
	• Use scrapy startproject <ProjectName> to intiate file structure
	• Ignore the 2 _init_py files given 
	• File Structure : 
		○ Settings.py 
			§ BOT_NAME 
				□ BOTs automates writing the code, the crawler is a bot 
			§ USER_AGENT 
				□ Write your domain name for formal purposes when scraping 
			§ CONCURRENT_REQUESTS
				□ Request - to open up for open up 
				□ For each instance of scraping, concurrent requests are required
				□ 16 would mean 16 scrapings at one time 
				□ More requests means overload to the server, 16 to 32 is optimal, not 1000
		○ Items.py
			§ Item is a defined categorization of data hosted by the website
			§ Good practice to define all items in items.py 
		○ Pipelines.py : 
			§ To handle and store the data in a .json or any other database file, the pipeline has to be defined correctly
		○ Middlewares.py 
			§ Some stuff can be added to requests like proxies etc. This has to be done through middlewares. Responses can also be handled through middlewares.
	• Make sure all spiders go inside the spiders folder and not anywhere else 
	• Remember to define the name and start_urls variables
	• Extract specific data by using HTML tags
	• Response contains the source code
	• Yield keyword instead of return statement in a spider
	• Always crawl from the folder containing scrapy.cfg file
	• Use spider name defined in the name attribute to crawl
	• Using title::text will store only the text contained  in a tag
	• For intitating a shell to inspect a website source code, use scrapy shell "websiteDomain"
		○ Then simply use response.css(<selector>).extract() to scrape text
		○ Use [0] index and so on to select between list elements
		○ Use extract_first() to avoid errors when nothing is being returned
		○ For example: for a tag like <span class = "text" ... >, use response.css("span.text::text").extract()
		○ For ID instead of class use # like span#<ID>
	• Using the Selector Gadet extension
		○ Select the data you want to scrape and copy the selector given by the extension
		○ Example : for output '.author',  response.css(".author::text").extract() can be used
		○ Click further to deselect what you dont want to be scraped and you will get a narrowed down selector from the extension
	• Selector is the condition used for extracting data
		○ Type : CSS Selectors
		○ Type : XPATH 
			§ Some usecases : extracting href paths (value of the href tags)
			§ response.xpath("//title/text()").extract()  for extracting text of the title tag
			§ response.xpath("//span[@class='text']/text()")[1].extract() for extracting from the tag <span class="text"...> ... </span>
				□ Single qoutes only in 'text' to avoid clash with the double qoutes
				□ For ID instead of class, just replace class with ID
			
