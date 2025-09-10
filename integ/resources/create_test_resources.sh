#!/bin/bash

# Deploys the CloudFormation template to create the stack and necessary resources- kinesis data stream, s3 bucket, and kinesis firehose delivery stream
# Resource (stream, s3, delivery stream) names will start with the stack name followed by the corresponding architecture and build version. "integ-test-fluent-bit-architecture-buildversion"
ARCHITECTURE=$(uname -m | tr '_' '-')
# For arm, uname evaluates to 'aarch64' but everywhere else in the pipline
# we use 'arm64'
if [ "$ARCHITECTURE" = "aarch64" ]; then
    ARCHITECTURE="arm64"
fi

# Include BUILD_VERSION in stack name to ensure isolation between different versions
STACK_NAME="integ-test-fluent-bit-${ARCHITECTURE}-${BUILD_VERSION}"
aws cloudformation deploy --template-file ./integ/resources/cfn-kinesis-s3-firehose.yml --stack-name ${STACK_NAME} --region "$AWS_REGION" --capabilities CAPABILITY_NAMED_IAM --no-fail-on-empty-changeset
