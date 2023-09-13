# 2.4 CÓDIGO REFATORADO

from collections import deque

class PrinterQueue2:
    def __init__(self):
        self.queue = deque()

    def add_job(self, job):
        if job:
            self.queue.append(job)
            print(f"Job '{job}' adicionado na fila!")
        else:
            print("Job inválido. Por favor, adicione um job válido.")

    def print_next(self):
        if self.queue:
            job = self.queue.popleft()
            print(f"Imprimindo o job: '{job}'")
        else:
            print("Nenhum job na fila!")

    def view_queue(self):
        if self.queue:
            print("Fila de impressAo:")
            for job in self.queue:
                print(job)
        else:
            print("Fila de impressão vazia.")

# Exemplo de uso
printer_queue = PrinterQueue2()
printer_queue.add_job("Documento 1")
printer_queue.add_job("Documento 2")
printer_queue.view_queue()
printer_queue.print_next()
printer_queue.print_next()
printer_queue.print_next()
