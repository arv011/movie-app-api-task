from accounts.models import RequestCounter

class RequestCounterMiddleware(object):  
    def __init__(self, get_response):  
        self.get_response = get_response  
      

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.process_request(request)
        # increase_counter(r)
        # calling view
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        self.process_response(request, response)
        return response
    
    def process_request(self, request):
        # increase count 1 on every request
        # print(request.META['HTTP_USER_AGENT'],'kkkk')
        try:
            try:
                obj = RequestCounter.objects.get(is_deleted=False)
            except RequestCounter.DoesNotExist:      
                obj = RequestCounter.objects.create(is_deleted=False)
            except RequestCounter.MultipleObjectsReturned:
                obj = RequestCounter.objects.filter(is_deleted=False).last()
            obj.counts = obj.counts + 1
            obj.save()
        except Exception as e:
            pass
    
    def process_response(self,request, response):
        pass