from constructs import Construct
from aws_cdk import (
    # Duration,
    Stack,aws_lambda as lambda_, aws_cdk.aws_sqs as sqs 
 
    # aws_sqs as sqs,    
)
from constructs import Construct


class StackName(Stack):

        
    # Use managed key
    sqs.Queue(self, "Queue",
        encryption=sqs.QueueEncryption.KMS_MANAGED
    )

    # Use custom key
    my_key = kms.Key(self, "Key")

    sqs.Queue(self, "Queue",
        encryption=sqs.QueueEncryption.KMS,
        encryption_master_key=my_key
    )

    # Use SQS managed server side encryption (SSE-SQS)
    sqs.Queue(self, "Queue",
        encryption=sqs.QueueEncryption.SQS_MANAGED
    )

    # Unencrypted queue
    sqs.Queue(self, "Queue",
        encryption=sqs.QueueEncryption.UNENCRYPTED
    )
    sqs.Queue(self, "Queue",
        enforce_sSL=True
    )
   
  
      


