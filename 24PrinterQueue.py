# 2.4 PRINTER QUEUE
# CÓDIGO ORIGINAL ANTES DA REFATORAÇÃO

class PrinterQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, job):
        self.queue.append(job)
        print("Job adicionado!")

    def print_next(self):
        if len(self.queue) > 0:
            job = self.queue.pop(0)
            print("Imprimindo o job:", job)
        else:
            print("Nenhum job na fila!")

    def view_queue(self):
        print("Fila de impressAo:")
        for job in self.queue:
            print(job)

# Exemplo de uso
printer_queue = PrinterQueue()
printer_queue.add_job("Documento 1")
printer_queue.add_job("Documento 2")
printer_queue.view_queue()
printer_queue.print_next()
printer_queue.print_next()
printer_queue.print_next()
