from rest_framework.response import Response

class CustomResponse(Response):
    def __init__(self, data=None, status=None,message=None, template_name=None, headers=None, exception=False, content_type=None):
        response_data = {
            'status': status,
            'data': data,
            'message': message,
        }
        super().__init__(response_data, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)