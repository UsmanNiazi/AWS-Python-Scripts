from constructs import Construct
from aws_cdk import (
    # Duration,
    Stack,aws_lambda as lambda_ 
 
    # aws_sqs as sqs,    
)
from constructs import Construct


class StackName(Stack):
   
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hw_lambda=self.createfunc("MyLambda","./resources","hw_lambda.LambdaHandler")
               
        
    def createfunc(self,id_,path,handler):
        return lambda_.Function(self, id_,
        code=lambda_.Code.from_asset(path),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_8)
      