# FindAShoe
FindAShoe started as a final projectf for my INST126 class, we had a free range of topics but I decided to try to tackle some webpage automation. 
Shoe bots can be found online to help resellers buy shoes seconds after they drop, utilizing a bot allows buyers to fill in field and click on buttons much faster
than a human can. I didnt need the same functionality that resellers do, but I did want to create a bot that would make searching for shoes easier for me, instead of 
opening multiple tabs and filling in fields, my bot could do it for me. Initially I only added one website to the final projects and I did not implimentany frameworks 
for a console interface. I quickly realized I could scale the project even more.

## Adding more websites/Console App
Once the project was over I realized that I could easily add more websites to the program, but it would requre me to create a menu for the user. I played
around with the idea of a GUI but I liked the idea of creating a console application so that the code could be called and interacted with in a terminal window.

## Problems I Ran Into
The problem with creating a bot that interacts with webpages is that many websites have caught onto the new technology and create barriers to prevent them from giving
people unfair advantage durring flash sales and new drops. Even though my bot wasn't being used for flash sales and new drops, some websites still blocked me from trying.
To counter this, I had to create custom URLs that would take the user straigh to the webpage instead of using a bot to click on buttons and fill in fields. I didnt 
love this work-around but it still gave me a quick solution to an issue I was having.

## Final Results
The results of the project is a console application that uses a webdriver (chromedriver) to open and interact with webpages. My code asks the user what shoe they're
looking for and which websites they would like to search on. From there the application opens a webpage and takes the users to the requested page and looks up the 
requested search query. The application will also allow you to search on all sites, in which it will open a new tab for each search.
