# RIINA   

## NOT AVAILABLE FOR RELEASE YET

## RIINA in a sentence   
Regular Insertion of Internet-sourced Nav (RIINA) enable scheduled update of NAV from reliable sources supporting various scripts from jchan-gi.   

## How RIINA work   
RIINA will download a webpage containing NAV information in a temporary folder.    
The webdriver supported by selenium will read the NAV at specific valuation date.    
Finally, the NAV record will insert into SQLite databse.    

## Difference against other crawling tools    
1. More comprehensive coverage of international funds by selection of data provider    
2. More decimal places available against Morning Star API    
3. Avoid blocking of common crawling agent, e.g. Browser using Selenium WebDriver    
4. More efficient visualization and query by database-format storage.    

## Notice    
Part of the data have been masked or removed due to the incompatible usage policy.     

## Requirement    
1. Mozilla Firefox browser (enabling always Private browsing mode)    
2. Chrome Browser without Internet access (Read HTML downloaded by firefox)    
3. Chrome webdriver at the same directory of the files   
4. Python 3 (executable added into PATH) with:    
  * Selenium    
  * pywinauto    
5. SQLite database of fund    

## Acknowledgement   
A script attached in this repo. is modified from pywinauto project under BSD 3-clause (Revised) license on their GitHub repo.      

## LICENSE     
BSD 3-clause (Revised) (See [LICENSE](https://github.com/jchan-gi/RIINA/blob/master/LICENSE))    