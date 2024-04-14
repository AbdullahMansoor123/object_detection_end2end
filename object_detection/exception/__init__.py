import os, sys
from object_detection.logger import logging

def error_message_details(error, error_details:sys):
    _, _, exc_tb = error_details.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error found in file {filename}, at line# {exc_tb.tb_lineno}, error message '{str(error)}'"

    return error_message

class Custom_Exception(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)
    def __str__(self) -> str:
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Division by Zero")
#         raise Custom_Exception(e,sys)