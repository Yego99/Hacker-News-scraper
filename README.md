# Hacker-News-scraper
-	This project is going to scrape the first 2 pages of the news website Hacker news and grab the headlines, links, and number of votes for all articles that have over 100 votes.
-	We use Beautiful soup to be able to use the website’s HTML and grab different data and perform actions on it & Requests allows us to download the HTML
-	First, we request all the text from the website with requests module. Then using BS we can parse (convert from string to an object we can use) the HTML text we just requested so that we can manipulate the HTML. Now, with the parsed HTML we can use selectors to grab specific parts of the data we want, So I will only be grabbing the name of the article and its link via “.titleline > a” (the a is because in the website’s HTML the title and link are under the a tag) and the score of the article’s score via “.subtext”. 
-	Now I will create a function that takes links and subtext/ votes and groups them with a dictionary. To start we are going to make a new Hacker news list that is empty and to it add only the text (title, link and score) and no HTML. To do this I will make a for loop that grabs the text of the title only for each article using “.getText()”. I will use the same method to grab only the link and the votes for each article. 
-	Once I gather the title, link and votes I will group them by appending them to a dictionary before putting them in the list. However, I still need to filter. There are 2 cases I must account for 1) if there is no score 2) if the score is less than 100, I use 2 if statements to make sure these conditions are met. If there is a score then I will convert the score into and int data type and replace the text with an empty string so I am left with just a number. Then using a nested if statement I take the articles with scores greater than 99 and append the title link and score to a dictionary and append each grouping to the list
-	Finally the last step to this project is ordering my results by number of votes descending so I am going to make another function called sort. Fist I give it my hacker news list and using the sorted function and a lambda function I can identify a key that I want to sort by which will be votes
