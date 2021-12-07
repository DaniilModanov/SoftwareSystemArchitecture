from BusinessLogic.Buffer import *
class BufferManager:
    def __init__(self, buffer, sources):
        self.__requests = []
        self.__buffer: Buffer = buffer
        self.__sources = sources

    def __collect_requests(self):
        for source in self.__sources:
            request = source.get_request()
            if request is not None:
                self.__requests.append(request)

    def __fill_buffer(self):
        for request in self.__requests:
            if self.__buffer.is_full() is False:
                self.__buffer.add_request(request)
            else:
                request.deny_buffer()
        self.__requests = []

    def work(self):
        self.__collect_requests()
        self.__fill_buffer()
