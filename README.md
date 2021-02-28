# Flow Python Protocol

Basic implementation of a Python gRPC client for reading data from [Flow](https://onflow.org).

Protocol files generated from [Flow Protocol Buffer Source Files](https://github.com/onflow/flow/tree/master/protobuf) using [prototool](https://github.com/uber/prototool) and [grpcio-tools](https://pypi.org/project/grpcio-tools/).

[More Flow API information](https://docs.onflow.org/access-api).

## Usage

Install grpc (not a full requirements file, so you may also need to install other things first).
`pip install grpc`

Then try `python test.py` to use the script that'll test if you can read a block height in flow.

Enjoy!


