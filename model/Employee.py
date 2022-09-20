class Employee:
   name: str
   cpf: str
   salary: float
       
   def __init__(self, cpf: str, name: str, salary: float):
      self.cpf = cpf 
      self.name = name
      self.salary = salary