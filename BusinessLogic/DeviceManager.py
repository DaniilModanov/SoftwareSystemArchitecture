class DeviceManager:

    def __init__(self, buffer, workers):
        self.__buffer = buffer
        self.__workers = workers

    def __fill_workers(self):
        for worker in self.__workers:
            if worker.is_available():
                request = self.__buffer.get_request()
                if request is not None:
                    worker.add_request(request)
                else:
                    break

    def work(self):
        for worker in self.__workers:
            worker.try_to_release()
        self.__fill_workers()
