'''
Write a program that allows you to calculate the total price of the products your customers are purchasing, 
including any special offers (coupons) the customers might redeem.

Consider the following instructions:
1. Every customer has a discount coupon. The cashier asks to the customer for his coupon
percentage. Store such input value in a variable called promotion_percentage. You can
expect the input to be an integer number from 0 to 100.
2. Calculate the subtotal price of the purchase using the predefined variables (see Listing 1)
and store the result in a variable named subtotal_price.
3. Print a message showing the subtotal price of the purchase. The message should look as
follows: ”The subtotal of your purchase is x”, where x is the subtotal price you calculated
in step 2. Don’t worry about number formatting in this step.
4. Calculate the amount the customer saves using your previous results and store the result in
a variable named savings.
5. Print a message showing the savings the customer makes. The message should look as
follows: ”Your savings are y”, where y is the savings amount you calculated in step 4. Don’t
worry about number formatting in this step.
6. Calculate the total price of the purchase and store it in a variable named total_price.
2
'''

# Please do not modify this part of the code!
price_banana = 1.5
price_milk = 2.0
number_of_bananas_purchased = 4
number_of_milks_purchased = 3

# Your code goes here
promotion_percentage=int(input('Enter customer discount coupon percentage (Please enter any integer between 0 to 100):'))
if (0<=promotion_percentage<=100):
	subtotal_price=(price_banana*number_of_bananas_purchased+price_milk*number_of_milks_purchased)
	print('The subtotal of your purchase is',subtotal_price)
	savings=(subtotal_price*promotion_percentage/100)
	print('Your savings are ',savings)
	total_price=(subtotal_price-savings)
	print('The total price of your purchase is ',total_price)
else:
	print('Please enter any integer between 0 to 100')