
import sys


def get_error_information(error, error_details:sys):
    _,_,ex_tb = error_details.exc_info()
    file_name=ex_tb.tb_frame.f_code.co_filename
    error_message=f"The error as occured in {file_name} line number {ex_tb.tb_lineno} error : {error}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_msg, error_details:sys):
        super().__init__(error_msg)
        self.error_msg= get_error_information(error_msg,error_details)
    def __str__(self):
        return self.error_msg