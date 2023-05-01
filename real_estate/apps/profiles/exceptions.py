from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested profile dose not exists"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can't edit a profile that doesn't beong to you"