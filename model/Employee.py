class Employee:
   name: str
   cpf: int
   salary: float
       
   def __init__(self, cpf: int, name: str, salary: float):
      self.cpf = cpf 
      self.name = name
      self.salary = salary