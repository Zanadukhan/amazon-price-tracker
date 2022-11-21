# amazon-price-tracker
A script that checks daily if the current price of a provided amazon url link for an item and sends a email if condition is fulfilled

Functions:
1. Asks the user for a amazon store url
2. asks the user for minimum desired price
3. the price is scraped off the html and compared to the minimum desired price
4. if condition is met, an email is sent to the email recepient stating the price 
   and a store link
5. 3 and 4 are repeated every day
