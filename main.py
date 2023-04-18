
from cli import PersonCLI
from database import Database
from personmodelmol import personModel

db=Database(database='relatorio5',collection='livros')
personModel=personModel(database=db)

personCLI=PersonCLI(personModel)
personCLI.run()

