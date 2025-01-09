class UserAccount:
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.__password = hash(password) 

  def set_password(self, new_password):
    self.__password = hash(new_password)
    print("Пароль успешно изменен.")

  def check_password(self, password):
    return hash(password) == self.__password

user = UserAccount("Prapor", "pajzulamagomedov740@gmail.com", "mypassword")
user.set_password("newpassword")

print("Проверка пароля:", user.check_password("newpassword"))
print("Проверка пароля:", user.check_password("mypassword"))