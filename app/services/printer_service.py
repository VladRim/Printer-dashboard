from app.repositories.printer_repository import PrinterRepository


class PrinterService:

    def __init__(self, repository: PrinterRepository):

        self.repository = repository

    def get_all(self):

        return self.repository.get_all()

    def count(self):

        return self.repository.count()
