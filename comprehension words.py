cities=["Nairobi","Tokyo","Pretoria","Dodoma","Kigali","Washingtonne"]
odd_number_character=[ city for city in cities if len(city)%2 !=0]
print("comprehension words with odd number characters:",odd_number_character)