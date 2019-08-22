# Twitter Like Bot







This bot uses Firefox, Gecko driver and the Selenium webdriver to automatically like tweets based on user-input username, password and hashtag. 







## Setup







- First  you need to install Firefox, and you can do so [here](https://www.mozilla.org/en-US/firefox/).

- Then, download Gecko driver from [here](https://github.com/mozilla/geckodriver/releases), and extract the file inside the archive to your Python directory - for me it was C:\Users\DorrabbKhan\AppData\Local\Programs\Python\Python37.

- Finally, install serenium using:

  

  ```
  pip install serenium
  ```







## Execution







### As a script





Use this to execute the script:



```
python likebot.py <email> <password> <hashtag> <scroll limit>
```



Replace <email> with your Twitter email or username, <password> with your password, <hashtag> with the hashtag you want to look for, and <scroll limit> with how many times you want to scroll down to the end of the page and load more tweets in order to like them - here's an example:



```
python likebot.py foo@helloworld.com verystrongpassword coolhashtag 3
```



This will log into Twitter using foo@helloworld.com and verystrongpassword as password, search for coolhashtag, scroll to the end of the page thrice, and then like all the tweets that were loaded and finally log out.





### As a package





First, import likebot with:



```
import likebot
```



or



```
from likebot import execute_bot
```



Execute the execute_bot function, passing as arguments the username, password, hashtag and scroll limit:



```python
likebot.execute_bot('foo@helloworld.com', 'verystrongpassword', 'coolhashtag', 3)
```



or



```python
likebot.execute_bot('foo@helloworld.com', 'verystrongpassword', 'coolhashtag', 3)
```





## Future plans





- Add error handling
- Refactor and optimize

