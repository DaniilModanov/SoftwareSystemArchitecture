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
        denied_request = None
        for request in self.__requests:
            if self.__buffer.is_full() is False:
                self.__buffer.add_request(request)
            else:
                request.deny_buffer()
                denied_request = request
        self.__requests = []
        return denied_request

    def work(self):
        self.__collect_requests()
        denied_request = self.__fill_buffer()
        return denied_request
        # for r in denied_requests:
        #     print(r.get_id())
