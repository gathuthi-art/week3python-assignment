def calculate_discount(price,discount_percentage):
   if discount_percentage >=20:
    discount_amount=(discount_percentage/100)*price
    final_price=price-discount_amount
    return final_price
   else:
     return price
   
   
   
origin_price=float(input('enter the orogonal price ofthe item: '))
discount_persentage=float(input('enter the discount to be issued: '))

final_price=calculate_discount(origin_price,discount_persentage)
print(f'the final price is: ${final_price}')
    
    

