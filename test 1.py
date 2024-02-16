current_users = ['Michael','leroy','Abbey','Pedri','Neymar']

new_users = ['Michael','Ozil','Kevin','Jude','Pedri']

for user_name in new_users:
    low_username = user_name.lower()
    if low_username in current_users:
        print(f"The username {low_username} has been used.\n Please enter a new name")
        
    else:
        print(f"The username {low_username} is available")   
        
        
        
        
        
                    
for num in range(1,100):
    print(num)
    if num % 3 == 0:
        print('Fizz')
    
    
    if num % 5 == 0:
        print('Buzz')    
    
    
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')    
    
