# 2 -> 94.5
# 3
class Vector():
  def __init__(self, x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def VectorAdd(self, V):
    return self + V
  def VectoreDotProduct(self, V):
    return self*V
  
  def __add__(self,V):
    if isinstance(V, Vector):
      return Vector(self.x + V.x, self.y + V.y , self.z + V.z)
    else:
      print("Invalid Operaion")
  def __mul__(self, V):
    if isinstance(V, Vector):
      return self.x*V.x + self.y *V.y + self.z*V.z
    elif isinstance(V, (int, float)):
      return Vector(V*self.x, V*self.y, V*self.z)
  def __str__(self):
    return f"({self.x},{self.y},{self.z})"
v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1.VectorAdd(v2))
print(v1.VectoreDotProduct(v2))

# 5
class Bank_Account():
  _accounts = []
  def __init__(self):
    user_info = None
    while True:
      user_info = input("Enter these two fields respectively separated by comma: (National_ID,Full_Name)").strip().split(',')
      if len(user_info) != 2 or not user_info[0].isnumeric():
        print("Invalid Input, Try again")
        continue
      break
    self.user_full_name = user_info[1]
    self.user_national_id = user_info[0]    
    self.account_status = "Activated"
    self._balance = 0
    
    Bank_Account._accounts.append(self)
    return "YOUR account has successfully created"

  def close_account(self):
    Bank_Account._accounts.remove(self)
    del self
  
  def account_block(self):
    self.account_status = "Blocked"
  
  def show_balance(self):
    return f"{self._balance}"
  
  def deposit(self, deposit_amount):
    self._balance += deposit_amount
    
  def withdraw(self, w_amount):
    if not (isinstance(w_amount, (int, float)) and w_amount > 0):
      return False, "Error: An invalid withdraw amount has been supplied"
    
    if(self.balance - w_amount) < 0:
      return False, "Error: Not possible, not enough balance! {}".format(self._balance)
    else:
      self.balance -= w_amount
      return True, "Withdrawal successful, Remaining Balance {}".format(self._balance)
بنظرم درستن
