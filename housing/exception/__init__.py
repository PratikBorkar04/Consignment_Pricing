import os
import sys
class HousingException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys):

        super().__init__(error_message) #  ==  Exception(error_message)

        self.error_message = HousingException.detail_error_msg(error_message=error_message,error_detail=error_detail)

    @staticmethod
    def detail_error_msg(error_message:Exception,error_detail:sys)->str:
        _,_ ,exec_tb = error_detail.exc_info() #(exception function contains type,value,traceback but we require only traceback because it will show exact path of error, so we are using traceback only else will be denoted as [ _ ])
        line_number = exec_tb.tb_frame.f_lineno #tb = trace back
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script:[{file_name} at line number:[{line_number}]error message:{[error_message]}"

        return error_message

    def __str__(self):
        return self.error_message