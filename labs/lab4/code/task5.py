#Task 5

def check_password(password):  
    length_ok = len(password) >= 8  
      
    has_upper = any(char.isupper() for char in password)  
      
    has_lower = any(char.islower() for char in password)  
      
    has_digit = any(char.isdigit() for char in password)  
      
    special_chars = "!@#$%^&*()_+-={}|;:,.<>?/~`"  
    has_special = any(char in special_chars for char in password)  
      
    conditions = {  
        "длина": length_ok,  
        "заглавные буквы": has_upper,  
        "строчные буквы": has_lower,  
        "цифры": has_digit,  
        "специальные символы": has_special  
    }  
      
    if all(conditions.values()):  
        return "Пароль надежный!"  
    else:   
        failed_conditions = [key for key, value in conditions.items() if not value]  
        return f"Пароль не соответствует требованиям:\n" + "\n".join(f"- Нет {condition}" for condition in failed_conditions)  
  
password = input("Введите пароль для проверки: ")  
result = check_password(password)  
print(result) 